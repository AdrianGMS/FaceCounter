# Welcome to Cloud Functions for Firebase for Python!
# To get started, simply uncomment the below code or create your own.
# Deploy with `firebase deploy`
#firebase emulators:start --only functions
#firebase deploy --only functions

#from firebase_functions import firebase_function, https_fn
from firebase_admin import initialize_app
# initialize_app()
#
#

import face_recognition
import pickle
import cv2
import os
import csv
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import storage
from datetime import datetime
import uuid
from flask import jsonify
import io
import pickle
import numpy as np
from PIL import Image

# Conectar a la base de datos
# Use a service account
cred = credentials.Certificate('C:/Users/USUARIO/AA-ProyectoFACECOUNTER/FaceCounterAPI/facecounter-7bdad-firebase-adminsdk-zdctb-27c9931a03.json')
firebase_admin.initialize_app(cred, {'storageBucket': 'facecounter-7bdad.appspot.com'})
app = firebase_admin.get_app()
print(app.name)

# Get a reference to the Firestore database
db = firestore.client()

# Get a reference to the storage bucket
bucket = storage.bucket()

# Define el nombre de la carpeta en el Storage de Firebase que deseas descargar
folder_name = 'Fotos Subidas/'

# Obtener la lista de nombres de los archivos en la carpeta
blobs = bucket.list_blobs(prefix=folder_name)

'''# Crear una carpeta temporal para almacenar los archivos descargados
temp_folder = 'C:/Users/USUARIO/AA-ProyectoFACECOUNTER/temp_folder'
if not os.path.exists(temp_folder):
    os.makedirs(temp_folder)
print('Carpeta temporal y archivos descargados exitosamente')

# Descargar los archivos de la carpeta y guardarlos en la carpeta temporal
for blob in blobs:
    file_name = blob.name.replace(folder_name, 'temp_0')
    blob.download_to_filename(os.path.join(temp_folder, file_name))
    print(f'{file_name} descargado exitosamente')
# Eliminar el archivo temp_folder
os.remove(os.path.join(temp_folder, 'temp_0'))'''

#UNKNOWN_FACES_DIR = "C:/Users/USUARIO/AA-ProyectoFACECOUNTER/temp_folder"
TOLERANCE = 0.5
FRAME_THICKNESS = 3
FONT_THICKNESS = 2
MODEL = "cnn"

# Establecer el código del curso
c_codigo_curso = "6OnWmcvdlM27usk2U68Q"

def marcar_ausente_todos():
    alumnos_ref = db.collection('curso_alumno').where("c_codigo_curso", "==", c_codigo_curso)
    alumnos = alumnos_ref.get()
    for alumno in alumnos:
        alumno_ref = db.collection('curso_alumno').document(alumno.id)
        alumno_ref.update({'d_asistencia': 'Ausente'})
        alumno_ref.update({'d_modificacion': 'Automatico'})


print("Cargando caras conocidas desde el archivo 'faces.dat'")
# Descarga el archivo faces.dat como bytes desde Firebase Storage
blob_dat = bucket.blob('faces.dat')
faces_data = blob_dat.download_as_string()

# Carga el contenido del archivo en memoria usando io.BytesIO
in_memory_file = io.BytesIO(faces_data)

# Usa pickle para cargar los datos del archivo en un diccionario
data = pickle.load(in_memory_file)
known_faces = data['known_faces']
known_names = data['known_names']

print("Procesando caras desconocidas")
correct_recognitions = 0
total_recognitions = 0

marcar_ausente_todos()

'''for filename in os.listdir(UNKNOWN_FACES_DIR):
    print(filename)
    image=face_recognition.load_image_file(f"{UNKNOWN_FACES_DIR}/{filename}")
    image = cv2.resize(image, (0, 0), fx=0.15, fy=0.15)
    locations = face_recognition.face_locations(image, model=MODEL)
    encoding = face_recognition.face_encodings(image, locations)
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
'''
# Recorrer los blobs en la carpeta y cargar las imágenes en memoria
for blob in blobs:
    print("entre a firebase")
    # Descargar la imagen como bytes
    nombre_archivo = blob.name
    print(nombre_archivo)
    file_name = os.path.basename(blob.name)
    print("nombre imagen: ", file_name)

    file_name = blob.name.replace(folder_name, 'temp_0')
    bytes_data = blob.download_as_bytes()
    
    # Verificar que los datos no estén vacíos
    if len(bytes_data) > 0:
        # Crear un objeto BytesIO a partir de los datos de la imagen
        stream = io.BytesIO(bytes_data)
        
        # Decodificar la imagen y hacer un resize
        image = cv2.imdecode(np.frombuffer(stream.read(), np.uint8), cv2.IMREAD_COLOR)
        image = cv2.resize(image, (0, 0), fx=0.15, fy=0.15)
        
        # Detectar las caras en la imagen
        locations = face_recognition.face_locations(image, model=MODEL)
        encoding = face_recognition.face_encodings(image, locations)
        
        # Procesar los encodings de las caras detectadas
        # ...
        
    else:
        print(f"Error: imagen {blob.name} vacía.")
    
    # Convertir la imagen a formato BGR (si es necesario)
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    # Dibujar los cuadros y los nombres en la imagen
    for face_encoding, face_location in zip(encoding, locations):
        results = face_recognition.compare_faces(known_faces, face_encoding, TOLERANCE)
        match = None
        if True in results:
            match = known_names[results.index(True)]
            print(f"Match Found: {match}")
            # Actualizar la base de datos
            correct_recognitions += 1

            top_left = (face_location[3], face_location[0])
            bottom_right = (face_location[1], face_location[2])
            color = [0, 255, 0]
            cv2.rectangle(image, top_left, bottom_right, color, FRAME_THICKNESS)

            top_left = (face_location[3], face_location[2])
            bottom_right = (face_location[1], face_location[2] + 22)
            cv2.rectangle(image, top_left, bottom_right, color, cv2.FILLED)
            cv2.putText(image, match, (face_location[3] + 10, face_location[2] + 15), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (200,200,200), FONT_THICKNESS)
            
            
            # Actualizar la columna d_asistencia en la tabla asistencia
                        
            alumnos_ref = db.collection('curso_alumno').where("c_codigo_curso", "==", c_codigo_curso).stream()

            for alumno in alumnos_ref:
                if alumno.get('d_nombre') == match:
                    alumno_ref = db.collection('curso_alumno').document(alumno.id)
                    alumno_ref.update({
                        'd_asistencia': 'Presente',
                        'd_fecha': datetime.now().strftime("%d de %B de %Y, %H:%M:%S UTC-5")
                    })
                                
                else:
                    alumno_ref = db.collection('curso_alumno').document(alumno.id)
                    alumno_ref.update({
                        'd_fecha': datetime.now().strftime("%d de %B de %Y, %H:%M:%S UTC-5")
                    })

        
        total_recognitions += 1

    # Sube la imagen a Firebase Storage
    blob = bucket.blob('Registro de fotografias/' + str(uuid.uuid4()) + '.jpg')
    _, buffer = cv2.imencode('.jpg', image)
    blob.upload_from_string(buffer.tobytes(), content_type='image/jpeg')

    print(f"Imagen subida exitosamente a Firebase Storage")

    cv2.imshow(blob.name, image)
    cv2.waitKey(5000)
    #cv2.destroyWindow(filename)


accuracy = correct_recognitions / total_recognitions * 100
print(f"Accuracy: {accuracy:.2f}%")

'''# Eliminar la carpeta temporal y los archivos descargados
for file_name in os.listdir(temp_folder):
    os.remove(os.path.join(temp_folder, file_name))
os.rmdir(temp_folder)
print('Carpeta temporal y archivos descargados eliminados exitosamente')'''

# Obtener los registros de asistencia para el curso
results = []
alumnos_ref = db.collection('curso_alumno').where("c_codigo_curso", "==", c_codigo_curso).stream()
for alumno in alumnos_ref:
    nombre = alumno.get('d_nombre')
    asistencia = alumno.get('d_asistencia')
    fecha = alumno.get('d_fecha')
    modificacion = alumno.get('d_modificacion')
    results.append((nombre, asistencia, fecha, modificacion))
    
# Definir los nombres de los archivos y su ruta en Firebase Storage
filename_txt = 'archivos de asistencia/asistencia.txt'
filename_csv = 'archivos de asistencia/asistencia.csv'

# Guardar resultados en TXT
with open("asistencia.txt", "w") as f:
    for row in results:
        f.write(f"{row[0]}: {row[1]} | {row[2] } | {row[3]} \n")

# Guardar resultados en CSV
with open('asistencia.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Nombre', 'Asistencia', 'Fecha', 'Modificacion'])
    for row in results:
        writer.writerow(row)

# Subir el archivo TXT a Firebase Storage
blob_txt = bucket.blob(filename_txt)
blob_txt.upload_from_filename("asistencia.txt")

# Subir el archivo CSV a Firebase Storage
blob_csv = bucket.blob(filename_csv)
blob_csv.upload_from_filename("asistencia.csv")

print(f"Archivos de asistencia subidos exitosamente a Firebase Storage")

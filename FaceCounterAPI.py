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
# Conectar a la base de datos
# Use a service account
#cred = credentials.Certificate('C:/Users/USUARIO/AA - Proyecto FACE COUNTER/facecounter-7bdad-firebase-adminsdk-zdctb-27c9931a03.json')
cred = credentials.Certificate('E:/AA - FaceCounter/FaceCounter/facecounter-7bdad-firebase-adminsdk-zdctb-27c9931a03.json')
firebase_admin.initialize_app(cred, {'storageBucket': 'facecounter-7bdad.appspot.com'})

app = firebase_admin.get_app()
print(app.name)

# Get a reference to the Firestore database
db = firestore.client()

# Get a reference to the storage bucket
bucket = storage.bucket()

# Define el nombre de la carpeta en el Storage de Firebase que deseas descargar
folder_name = 'Fotos Subidas/'
folder_name2 = 'Registro de fotografías/'

# Obtener la lista de nombres de los archivos en la carpeta
blobs = bucket.list_blobs(prefix=folder_name)

# Crear una carpeta temporal para almacenar los archivos descargados
temp_folder = 'E:/AA - FaceCounter/FaceCounter/temp_folder'
if not os.path.exists(temp_folder):
    os.makedirs(temp_folder)
print('Carpeta temporal y archivos descargados exitosamente')

temp_folder2 = 'E:/AA - FaceCounter/FaceCounter/temp_upload'
if not os.path.exists(temp_folder2):
    os.makedirs(temp_folder2)
print('Carpeta temporal y archivos descargados exitosamente')

# Descargar los archivos de la carpeta y guardarlos en la carpeta temporal
for blob in blobs:
    file_name = blob.name.replace(folder_name, 'temp_0')
    blob.download_to_filename(os.path.join(temp_folder, file_name))
    print(f'{file_name} descargado exitosamente')
# Eliminar el archivo temp_folder
os.remove(os.path.join(temp_folder, 'temp_0'))

UNKNOWN_FACES_DIR = "./temp_folder"
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
with open('faces.dat', 'rb') as f:
    data = pickle.load(f)
    known_faces = data['known_faces']
    known_names = data['known_names']


print("Procesando caras desconocidas")
correct_recognitions = 0
total_recognitions = 0

marcar_ausente_todos()
for filename in os.listdir(UNKNOWN_FACES_DIR):
    print(filename)
    image=face_recognition.load_image_file(f"{UNKNOWN_FACES_DIR}/{filename}")
    #image = cv2.resize(image, (0, 0), fx=0.25, fy=0.25)
    locations = face_recognition.face_locations(image, model=MODEL)
    encoding = face_recognition.face_encodings(image, locations)
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

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
    # Guarda la imagen procesada en una carpeta temporal
    temp_filename = f"{uuid.uuid4()}.jpg"
    temp_filepath = os.path.join(temp_folder2, temp_filename)
    cv2.imwrite(temp_filepath, image)

    # Sube la imagen a Firebase Storage
    blob = bucket.blob('Registro de fotografias/' + temp_filename)
    blob.upload_from_filename(temp_filepath)

    print(f"{temp_filename} subido exitosamente a Firebase Storage")
    cv2.imshow(filename, image)
    cv2.waitKey(5000)
    #cv2.destroyWindow(filename)


accuracy = correct_recognitions / total_recognitions * 100
print(f"Accuracy: {accuracy:.2f}%")

# Eliminar la carpeta temporal y los archivos descargados
for file_name in os.listdir(temp_folder):
    os.remove(os.path.join(temp_folder, file_name))
os.rmdir(temp_folder)
print('Carpeta temporal y archivos descargados eliminados exitosamente')

for file_name in os.listdir(temp_folder2):
    os.remove(os.path.join(temp_folder2, file_name))
os.rmdir(temp_folder2)
print('Carpeta temporal y archivos descargados eliminados exitosamente')

# Obtener los registros de asistencia para el curso
results = []
alumnos_ref = db.collection('curso_alumno').where("c_codigo_curso", "==", c_codigo_curso).stream()
for alumno in alumnos_ref:
    nombre = alumno.get('d_nombre')
    asistencia = alumno.get('d_asistencia')
    fecha = alumno.get('d_fecha')
    modificacion = alumno.get('d_modificacion')
    results.append((nombre, asistencia, fecha, modificacion))
    

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

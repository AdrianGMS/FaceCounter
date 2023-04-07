import face_recognition
import pickle
import cv2
import os
import psycopg2

UNKNOWN_FACES_DIR = "./caras_desconocidas4"
TOLERANCE = 0.5
FRAME_THICKNESS = 3
FONT_THICKNESS = 2
MODEL = "cnn"

# Conectar a la base de datos
conn = psycopg2.connect(
    host="localhost",
    database="facecounter",
    user="postgres",
    password="tesis202301"
)

def marcar_ausente_todos():
    cur = conn.cursor()
    cur.execute("UPDATE asistencia SET d_asistencia = 'Ausente'")
    conn.commit()
    cur.close()

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
            cur = conn.cursor()
            cur.execute("SELECT * FROM asistencia WHERE d_nombre_alumno = %s", (match,))

            # Obtener los resultados de la consulta
            row = cur.fetchone()
            if row:
                print(f"Before: {row[3]}")
                cur.execute("UPDATE asistencia SET d_asistencia = %s WHERE d_nombre_alumno = %s", ("Presente", match))
                conn.commit()
                print(f"After: Presente")
            cur.close()

        total_recognitions += 1
    
    cv2.imshow(filename, image)
    cv2.waitKey(10000)
    #cv2.destroyWindow(filename)

accuracy = correct_recognitions / total_recognitions * 100
print(f"Accuracy: {accuracy:.2f}%")

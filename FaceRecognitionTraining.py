import face_recognition
import os
import cv2
import pickle

KNOWN_FACES_DIR = "./caras_conocidas"
TOLERANCE = 0.5
MODEL = "cnn"

print("Entrenando...")

known_faces = []
known_names = []

for name in os.listdir(KNOWN_FACES_DIR):
    for filename in os.listdir(f"{KNOWN_FACES_DIR}/{name}"):
        print("Entrenando...:", name)

        image = face_recognition.load_image_file(f"{KNOWN_FACES_DIR}/{name}/{filename}")
        image = cv2.resize(image, (0, 0), fx=0.25, fy=0.25)
        encodings = face_recognition.face_encodings(image)
        if len(encodings) > 0:
            encoding = encodings[0]
        else:
            # No se pudo codificar ninguna cara en la imagen
            continue  # O haga algo más apropiado para su caso de uso

        known_faces.append(encoding)
        known_names.append(name)

print("Guardando caras conocidas en el archivo 'faces.dat'")
with open('faces.dat', 'wb') as f:
    pickle.dump({'known_faces': known_faces, 'known_names': known_names}, f)
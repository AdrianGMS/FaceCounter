import face_recognition
import pickle
import cv2
import os

UNKNOWN_FACES_DIR = "./caras_desconocidas2"
TOLERANCE = 0.5
FRAME_THICKNESS = 3
FONT_THICKNESS = 2
MODEL = "cnn"


print("Cargando caras conocidas desde el archivo 'faces.dat'")
with open('faces.dat', 'rb') as f:
    data = pickle.load(f)
    known_faces = data['known_faces']
    known_names = data['known_names']


print("Procesando caras desconocidas")
correct_recognitions = 0
total_recognitions = 0

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

        total_recognitions += 1
    
    cv2.imshow(filename, image)
    cv2.waitKey(3000)
    #cv2.destroyWindow(filename)

accuracy = correct_recognitions / total_recognitions * 100
print(f"Accuracy: {accuracy:.2f}%")
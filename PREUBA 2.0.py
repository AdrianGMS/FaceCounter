import os
import face_recognition

# Directorio de imágenes de entrenamiento
train_dir = "./CARAS/Ake"

# Lista de nombres y sus correspondientes imágenes de entrenamiento
train_names = []
train_encodings = []

# Recorre el directorio de entrenamiento y carga las imágenes de cada persona
for name in os.listdir(train_dir):
    person_dir = os.path.join(train_dir, name)
    if os.path.isdir(person_dir):
        # Carga todas las imágenes de la persona
        person_images = []
        for filename in os.listdir(person_dir):
            image_path = os.path.join(person_dir, filename)
            image = face_recognition.load_image_file(image_path)
            person_images.append(image)

        # Genera el encoding promedio de todas las imágenes de la persona
        person_encoding = face_recognition.face_encodings(person_images)[0]

        # Agrega el nombre y el encoding a las listas de entrenamiento
        train_names.append(name)
        train_encodings.append(person_encoding)
print(train_names)
print(train_encodings)
# Entrena el modelo con los encodings de las imágenes de entrenamiento
model = face_recognition.KDTree()
model.fit(train_encodings)

# Carga la imagen de prueba
test_image = face_recognition.load_image_file("./CARAS/Ake/ake.png")

# Busca todas las caras en la imagen de prueba
face_locations = face_recognition.face_locations(test_image)
face_encodings = face_recognition.face_encodings(test_image, face_locations)

# Compara cada cara encontrada con las caras de entrenamiento
for face_encoding, face_location in zip(face_encodings, face_locations):
    # Compara el encoding de la cara con los encodings de entrenamiento
    distances, indices = model.query([face_encoding])
    if distances[0] < 0.6:
        # Si la distancia es menor a 0.6, se reconoce la persona
        name = train_names[indices[0]]
        print(f"Se reconoció a {name} en la posición {face_location}")
    else:
        # Si la distancia es mayor a 0.6, no se reconoce a la persona
        print("No se reconoció a la persona en la posición", face_location)

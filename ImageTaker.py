import cv2
import os
import requests

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import storage

#os.mkdir(ruta_nueva_carpeta)

key = {
    "type": "service_account",
    "project_id": "facecounter-7bdad",
    "private_key_id": "7c233c617d6066e5e2016f7f5fac1fa8e81c50c5",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCxJV3TcgtpIyz8\nrw+1u7+VObid8RRf90Ti0SbE9wI1/9okm365XHqka5anZDOKa0JilTBbnCcM+Say\nZk3BgTDGE2QR9rOR3+iFi/MI5j0PoRLgzUTZDMl2W7C6cGi8eoIzWHsnjFrdExSb\nSiQp0rV02z2rs4ro/IP6YQIYmp4hlrxxwlkTxRiSyZqLs3l8hHNwtcdFo75m2KGl\n7FFjm0YfmoBojQMKO5VP9eLovEqXDK0uRagd4PKjU53xNuHmIURHCsbtzNZHfMSC\n+CZ5nQuSFOoBfBX9+mlbcho6ikMprLDMODz5Ne88evRQDOSZEhQy9Re3bjnS7UjK\nnuh/Dz+RAgMBAAECggEABU1KgR0dNVDdtFRjAnvzkHpRSbzg8LxcXfOHlwaTlN0r\nAMR8pvybGRe1Qx5PIpnyOzQe5ecHDi7Y1ycTtbJxrMQAzz7Ugg2zDmgxZndJpZGb\nGIpcQKjO0NGOuQ3LPLTn97RyvyzGvW4oRDuUWIIbdztmnaB6jF2eb5x+rRDXocat\n03vd+omgQLnrFMxRkR2zPqSd0VTnbrnzNF9sP3fVXcilD4i9BpgI+4WiAw22JPLT\nJaME4M+WN9Lg132Up9m+KEptBxXwdpIqmvd5BhOCMm08JQoWvApoXVqdJGYShOu6\nd3Uh/byukoHsR3BCVY1FJ9gv42zuO5ZgJHo4GUQw7wKBgQDyYFiHUA0Fn6+zy/IX\n+YI7UgOoDQdtF5Cf1nH5h2jOPheA2HTdu/0uqlDNhi/e1dzGh0+ZroVEJa2pWDUH\nFfRCUt23oJnWOYHFc9zGMDtqTxCQLqsDjZcPg756bKkqAtDyFqSgoBRrftGHqCWM\n9V0sMCVP7QwCUuAV7POoBT5OiwKBgQC7GmS7+z0HOQiRfwjJ7h/dG6WZD6qCTNEe\ni9saNRDAoFHAC5XSQaQwzaHARD2QzJxo1+GxyxzmwNl8emmHGTXyWmvs2EOzDQzJ\nyudu9oB13/eNJPGZXzUICt2E6sKA+as1hDreeDxLZmo4E9UZq7g1EEZiwmF6c2Cy\nVJVyRKjp0wKBgBH0jzpe9MgA32xLZIDgLASm+7xcUruDLmSY51Kb9Giq8uTJpEa0\n4XmuhlPjZ/JzF2rhpUT2R8sXm3jbHvqKZtDvAJvU2vCiy/lLrwRDmHM0rj5wJp0Z\nxSISGW9KU3HYSZBVmxaHJVwdRfptu3JozuEyI+F65xPY/d7B8f71fHsnAoGAPswA\n+0a7mOz/fzXP0VZmw2NAFTs40zrNBR+Tjhw5Xy1vwrEgu8zkOq0JmOpOb4b9CANM\n8MtnC9u2Ix1CxeEkRg8rIfcD4diDbkb3njqFqwpcn7bCj+NwfR6IctAIMBmb6P5U\nc86PDg91nxSo9VC5JrYrqYHsDZkj3zacYhnBR5kCgYEAkoUsrYuetMoT/lC7yAa8\nNAxJme3XyhqKwyYwwz2d9t5af71vADOqSutQY1yk7dQczJXppo1szNB1RGk0neSv\n/JGaH+rH8PcO1RivZbOLKB3oU7EFmmI0ZCsaDoKCJ4hRkXaqB31rmLYbvNODwYw4\n+ob7HqkjGql/bUIbEtSb768=\n-----END PRIVATE KEY-----\n",
    "client_email": "firebase-adminsdk-zdctb@facecounter-7bdad.iam.gserviceaccount.com",
    "client_id": "103057494865791731303",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-zdctb%40facecounter-7bdad.iam.gserviceaccount.com",
    "universe_domain": "googleapis.com"
    }

    # Inicializar la app de Firebase
cred = credentials.Certificate(key)
firebase_admin.initialize_app(cred, {'storageBucket': 'facecounter-7bdad.appspot.com'})
app = firebase_admin.get_app()
print(app.name)
# Get a reference to the Firestore database
db = firestore.client()

# Obtener la referencia a la colección "alumno"
alumno_ref = db.collection('alumno')

# Obtener los documentos de la colección "alumno"
alumnos = alumno_ref.stream()

# Directorio base donde se guardarán los frames extraídos del video
base_frames_dir = "./caras_conocidas/"
videos_dir = "./Videos/"


# Iterar sobre los documentos de la colección "alumno"
for alumno in alumnos:
    # Obtener los datos del documento actual
    d_nombre = alumno.to_dict()['d_nombre']
    d_urlvideo = alumno.to_dict()['d_urlvideo']

    # Crear el directorio para almacenar los frames del alumno
    frames_dir = os.path.join(base_frames_dir, d_nombre)

    # Crear directorio si no existe
    if not os.path.exists(frames_dir):
        os.makedirs(frames_dir)

    # Obtener el nombre del video del URL

    # Ruta completa del video a descargar
    video_path = os.path.join(videos_dir, d_nombre)

    # Descargar el video desde la URL
    response = requests.get(d_urlvideo)
    with open(video_path, 'wb') as f:
        f.write(response.content)

    # Inicializar el objeto VideoCapture
    cap = cv2.VideoCapture(video_path)

    # Obtener la tasa de fotogramas del video
    fps = cap.get(cv2.CAP_PROP_FPS)
    print("fps del video: ", fps)

    # Definir el número máximo de fotogramas a extraer
    max_frames = 550

    # Inicializar el índice de imagen y el contador de imágenes guardadas
    img_index = 0
    saved_images = 0

    # Verificar si el video tiene más de 30 fps
    if fps > 30:
        # Calcular el número máximo de imágenes por segundo
        images_per_second = 30

        # Calcular el intervalo de tiempo para los saltos
        time_interval = 2
    else:
        # Si el video tiene 30 fps o menos, no se aplica ningún intervalo
        images_per_second = fps
        time_interval = 1

    # Bucle para leer cada frame del video
    while cap.isOpened() and saved_images < max_frames:
        ret, frame = cap.read()

        # Si no hay más frames, salir del bucle
        if not ret:
            break

        # Si el índice actual corresponde a un frame que se debe extraer, guardarlo como imagen
        if img_index % time_interval == 0:
            # Guardar el frame actual como imagen en el directorio especificado
            cv2.imwrite(os.path.join(frames_dir, f"frame{saved_images:04d}.jpg"), frame)
            saved_images += 1
        
        img_index += 1

    # Liberar el objeto VideoCapture y destruir las ventanas abiertas
    cap.release()
    cv2.destroyAllWindows()

    # Imprimir la cantidad total de frames extraídos para el alumno actual
    print(f"Se extrajeron {saved_images} frames del video para el alumno {d_nombre}.")

'''
# Ruta del video a procesar
video_path = "./Videos/Riccardo.mp4"

# Directorio donde se guardarán los frames extraídos del video
frames_dir = "./caras_conocidas/Riccardo"


# Crear directorio si no existe
if not os.path.exists(frames_dir):
    os.makedirs(frames_dir)

# Inicializar el objeto VideoCapture
cap = cv2.VideoCapture(video_path)

# Inicializar el índice de imagen
img_index = 0

# Bucle para leer cada frame del video
while cap.isOpened():
    ret, frame = cap.read()

    # Si no hay más frames, salir del bucle
    if not ret:
        break

    # Guardar el frame actual como imagen en el directorio especificado
    cv2.imwrite(os.path.join(frames_dir, f"frame{img_index:04d}.jpg"), frame)

    # Incrementar el índice de imagen
    img_index += 1

# Liberar el objeto VideoCapture y destruir las ventanas abiertas
cap.release()
cv2.destroyAllWindows()

# Imprimir la cantidad total de frames extraídos
print(f"Se extrajeron {img_index} frames del video.")
'''
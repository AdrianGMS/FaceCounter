import cv2
import os
#dirname = 'caras_conocidas_codigo'
#os.mkdir(dirname)
#ruta_carpeta_padre = "./caras_conocidas"
#nombre_nueva_carpeta = "Adrian2jeje"
#ruta_nueva_carpeta = os.path.join(ruta_carpeta_padre, nombre_nueva_carpeta)

#os.mkdir(ruta_nueva_carpeta)

# Ruta del video a procesar
video_path = "./Videos/Natalia.mp4"

# Directorio donde se guardarán los frames extraídos del video
frames_dir = "./caras_conocidas/Natalia"

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

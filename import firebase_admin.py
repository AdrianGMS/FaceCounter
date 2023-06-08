import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from datetime import datetime

# Use a service account
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
firebase_admin.initialize_app(cred)

app = firebase_admin.get_app()
print(app.name)

# Get a reference to the Firestore database
db = firestore.client()
# Crear una nueva instancia de batch
batch = db.batch()

###################################################################
# Definir los datos para CURSO
'''data1 = {'d_nombre': 'Taller de Proyecto 2',
         'd_codigo_seccion': 'CCA1', 
         'd_dia': 'Martes',
         'z_hora': '16:00 - 19:00',
         'id_profesor': '1VQ0uIeowP99qnFa5lEA'
         }

data2 = {'d_nombre': 'Matematica computacional',
         'd_codigo_seccion': 'CS02',
         'd_dia': 'Martes',
         'z_hora': '10:00',
         'id_profesor': 'GDZLcKzxIUpyJeZplKsk'
         }

# Agregar las operaciones de creación de documentos al batch
doc_ref1 = db.collection('curso').document()
batch.set(doc_ref1, data1)

doc_ref2 = db.collection('curso').document()
batch.set(doc_ref2, data2)'''

###################################################################
# Definir los datos para PROFESOR
'''
data1 = {'d_nombre': 'Julio',
         'd_apellido': 'Sanchez', 
         'd_correo': 'juliosanchez@email.com',
         'n_telefono': '123456789',
         'd_contrasena': 'contrasena'
         }
data2 = {'d_nombre': 'Julio',
         'd_apellido': 'Sanchez', 
         'd_correo': 'juliosanchez@email.com',
         'n_telefono': '123456789',
         'd_contrasena': 'contrasena'
         }

doc_ref1 = db.collection('profesor').document()
batch.set(doc_ref1, data1)

doc_ref2 = db.collection('profesor').document()
batch.set(doc_ref2, data2)
'''
###################################################################
# Definir los datos para ALUMNO
'''
data = [
    {'d_nombre': 'Hamill', 'd_codigo': 'DEF755', 'd_urlvideo': 'https://www.youtube.com/watch?v=efgh5678'},
    {'d_nombre': 'Adrian', 'd_codigo': 'GHI123', 'd_urlvideo': 'https://www.youtube.com/watch?v=ijkl9012'},
    {'d_nombre': 'Aldo', 'd_codigo': 'DEF468', 'd_urlvideo': 'https://www.youtube.com/watch?v=efgh5678'},
    {'d_nombre': 'Natalia', 'd_codigo': 'DEF987', 'd_urlvideo': 'https://www.youtube.com/watch?v=efgh5678'},
    {'d_nombre': 'Elvis', 'd_codigo': 'DEF345', 'd_urlvideo': 'https://www.youtube.com/watch?v=efgh5678'},
    {'d_nombre': 'Daniel', 'd_codigo': 'DEF733', 'd_urlvideo': 'https://www.youtube.com/watch?v=efgh5678'},
    {'d_nombre': 'Eduardo', 'd_codigo': 'DEF098', 'd_urlvideo': 'https://www.youtube.com/watch?v=efgh5678'},
    {'d_nombre': 'Macarena', 'd_codigo': 'DEF393', 'd_urlvideo': 'https://www.youtube.com/watch?v=efgh5678'},
    {'d_nombre': 'Mora', 'd_codigo': 'DEF009', 'd_urlvideo': 'https://www.youtube.com/watch?v=efgh5678'},
    {'d_nombre': 'Pauline', 'd_codigo': 'DEF711', 'd_urlvideo': 'https://www.youtube.com/watch?v=efgh5678'},
    {'d_nombre': 'Ake', 'd_codigo': 'DEF191', 'd_urlvideo': 'https://www.youtube.com/watch?v=efgh5678'},
    {'d_nombre': 'Riccardo', 'd_codigo': 'DEF988', 'd_urlvideo': 'https://www.youtube.com/watch?v=efgh5678'},
    {'d_nombre': 'SebastianC', 'd_codigo': 'CCA001', 'd_urlvideo': 'https://firebasestorage.googleapis.com/v0/b/facecounter-7bdad.appspot.com/o/Videos%20caras%2FSebastianC.mp4?alt=media&token=59632982-4e08-4b0c-9f24-3f7fb803123e'},
    {'d_nombre': 'SamuelC', 'd_codigo': 'CCA002', 'd_urlvideo': 'https://firebasestorage.googleapis.com/v0/b/facecounter-7bdad.appspot.com/o/Videos%20caras%2FSamuelC.mp4?alt=media&token=f873150b-8d4a-4787-b387-b7cdd31b4e16'},
    {'d_nombre': 'Puglisevich', 'd_codigo': 'CCA003', 'd_urlvideo': 'https://firebasestorage.googleapis.com/v0/b/facecounter-7bdad.appspot.com/o/Videos%20caras%2FPuglisevich.mp4?alt=media&token=5aef278e-5319-4e21-8966-f861da034f5c'},
    {'d_nombre': 'MauroA', 'd_codigo': 'CCA004', 'd_urlvideo': 'https://firebasestorage.googleapis.com/v0/b/facecounter-7bdad.appspot.com/o/Videos%20caras%2FMauroA.mp4?alt=media&token=bf86a5ec-e74b-4197-8783-c25777a41813'},
    {'d_nombre': 'MarcoF', 'd_codigo': 'CCA005', 'd_urlvideo': 'https://firebasestorage.googleapis.com/v0/b/facecounter-7bdad.appspot.com/o/Videos%20caras%2FMarcoF.mp4?alt=media&token=3ff725f2-3b1b-4081-95de-fd3bbd99341a'},
    {'d_nombre': 'MarceloG', 'd_codigo': 'CCA006', 'd_urlvideo': 'https://firebasestorage.googleapis.com/v0/b/facecounter-7bdad.appspot.com/o/Videos%20caras%2FMarceloG.mp4?alt=media&token=0eec66fc-d69e-42cb-996f-a8d42bbbdebd'},
    {'d_nombre': 'JakC', 'd_codigo': 'CCA007', 'd_urlvideo': 'https://firebasestorage.googleapis.com/v0/b/facecounter-7bdad.appspot.com/o/Videos%20caras%2FJakC.mp4?alt=media&token=f5cb1823-c2d4-4afb-8034-bc1098711abc'},
    {'d_nombre': 'JairR', 'd_codigo': 'CCA008', 'd_urlvideo': 'https://firebasestorage.googleapis.com/v0/b/facecounter-7bdad.appspot.com/o/Videos%20caras%2FJairR.mp4?alt=media&token=345c13d2-9ac3-4642-a38d-67e79b925b09'},
    {'d_nombre': 'GonzaloC', 'd_codigo': 'CCA009', 'd_urlvideo': 'https://firebasestorage.googleapis.com/v0/b/facecounter-7bdad.appspot.com/o/Videos%20caras%2FGonzaloC.mp4?alt=media&token=b6fd05cd-e9a9-44c6-9cde-5695d838998e'},
    {'d_nombre': 'EstebanC', 'd_codigo': 'CCA010', 'd_urlvideo': 'https://firebasestorage.googleapis.com/v0/b/facecounter-7bdad.appspot.com/o/Videos%20caras%2FEstebanC.mp4?alt=media&token=6c15cd64-6c54-49c5-9e54-2e87187cdcb7'},
    {'d_nombre': 'DavidN', 'd_codigo': 'CCA011', 'd_urlvideo': 'https://firebasestorage.googleapis.com/v0/b/facecounter-7bdad.appspot.com/o/Videos%20caras%2FDavidN.mp4?alt=media&token=485d9ada-24bb-430e-84a9-c539b7904998'},
    {'d_nombre': 'AbigailG', 'd_codigo': 'CCA012', 'd_urlvideo': 'https://firebasestorage.googleapis.com/v0/b/facecounter-7bdad.appspot.com/o/Videos%20caras%2FAbigailG.mp4?alt=media&token=94c78c71-6393-475e-99a2-16a9bafb0088'},
    {'d_nombre': 'CamilaG', 'd_codigo': 'MOD001', 'd_urlvideo': 'https://firebasestorage.googleapis.com/v0/b/facecounter-7bdad.appspot.com/o/Videos%20caras%2FCamilaG.mp4?alt=media&token=bb87ee88-1bd2-4f0e-a9ca-4efe43dc3e55'},
    {'d_nombre': 'BrigitteD', 'd_codigo': 'MOD002', 'd_urlvideo': 'https://firebasestorage.googleapis.com/v0/b/facecounter-7bdad.appspot.com/o/Videos%20caras%2FBrigitteD.mp4?alt=media&token=758518d6-ebed-4f7e-97cc-b9631f8a09e0'},
    {'d_nombre': 'Carla', 'd_codigo': 'MOD003', 'd_urlvideo': 'https://firebasestorage.googleapis.com/v0/b/facecounter-7bdad.appspot.com/o/Videos%20caras%2FCarla.mp4?alt=media&token=fb04224a-607e-47d8-96b9-bfc17db84b55'},
    {'d_nombre': 'DianaT', 'd_codigo': 'MOD004', 'd_urlvideo': 'https://firebasestorage.googleapis.com/v0/b/facecounter-7bdad.appspot.com/o/Videos%20caras%2FDianaT.mp4?alt=media&token=2f5f7ead-b18c-476e-9088-16ce3c56ad5c'},
    {'d_nombre': 'AntonellaL', 'd_codigo': 'MOD005', 'd_urlvideo': 'https://firebasestorage.googleapis.com/v0/b/facecounter-7bdad.appspot.com/o/Videos%20caras%2FAntonellaL.mp4?alt=media&token=57e84f42-6fbe-4b3f-b029-84ec512314e5'},
    {'d_nombre': 'EsperanzaB', 'd_codigo': 'MOD006', 'd_urlvideo': 'https://firebasestorage.googleapis.com/v0/b/facecounter-7bdad.appspot.com/o/Videos%20caras%2FEsperanzaB.mp4?alt=media&token=9b7b0d80-e145-4dc2-a079-1b0188ad4d5e'},
    {'d_nombre': 'JoaquinM', 'd_codigo': 'MOD007', 'd_urlvideo': 'https://firebasestorage.googleapis.com/v0/b/facecounter-7bdad.appspot.com/o/Videos%20caras%2FJoaquinM.mp4?alt=media&token=0f429332-f29a-49ca-987a-eee5942f6e89'},
    {'d_nombre': 'RominaS', 'd_codigo': 'MOD008', 'd_urlvideo': 'https://firebasestorage.googleapis.com/v0/b/facecounter-7bdad.appspot.com/o/Videos%20caras%2FRominaS.mp4?alt=media&token=1c65ce53-71dd-4b92-a910-98ce3f7f2547'}
]


for alumno_data in data:
    doc_ref = db.collection('alumno').document()
    batch.set(doc_ref, alumno_data)
'''

###################################################################
# Definir los datos para CURSO_ALUMNO
# Obtener las referencias de las colecciones alumno y curso
'''
alumno_ref = db.collection('alumno')
curso_ref = db.collection('curso')

# Obtener los documentos de las colecciones alumno y curso
alumnos = alumno_ref.stream()

# Crear una lista vacía para guardar los datos de curso_alumno
curso_alumnos = []

# Iterar sobre los documentos de la colección alumno
for alumno in alumnos:
    c_codigo_alumno = alumno.id
    d_nombre = alumno.to_dict()['d_nombre']
    d_codigo = alumno.to_dict()['d_codigo']
    d_asistencia = 'Ausente'
    d_modificacion = 'Automatico'
    d_fecha = datetime.now()

    # Obtener los documentos de la colección curso
    cursos = curso_ref.stream()

    # Iterar sobre los documentos de la colección curso
    for curso in cursos:
        c_codigo_curso = curso.id
        d_nombre_curso = curso.to_dict()['d_nombre']

        # Crear el diccionario de datos del documento curso_alumno
        curso_alumno = {
            'c_codigo_alumno': c_codigo_alumno,
            'c_codigo_curso': c_codigo_curso,
            'd_nombre_curso': d_nombre_curso,
            'd_nombre': d_nombre,
            'd_codigo': d_codigo,
            'd_asistencia': d_asistencia,
            'd_modificacion': d_modificacion,
            'd_fecha': d_fecha
        }
        # Agregar el diccionario a la lista curso_alumnos
        curso_alumnos.append(curso_alumno)

# Agregar los documentos a la colección curso_alumno para ambos cursos
for curso_alumno in curso_alumnos:
    doc_ref = db.collection('curso_alumno').document()
    doc_ref.set(curso_alumno)
'''

# Inscribir TODOS alumnos en un CURSO especifico
'''
alumno_ref = db.collection('alumno')
curso_ref = db.collection('curso')

# Obtener los documentos de la colección alumno
alumnos = alumno_ref.stream()

# Crear una lista vacía para guardar los datos de curso_alumno
curso_alumnos = []

# Curso específico donde se inscribirán los alumnos
c_codigo_curso_manualmente = "Zqd2MSJDZuMavfPSvsMg"
d_nombre_curso_manualmente = "Programacion 2"

# Iterar sobre los documentos de la colección alumno
for alumno in alumnos:
    c_codigo_alumno = alumno.id
    d_nombre = alumno.to_dict()['d_nombre']
    d_codigo = alumno.to_dict()['d_codigo']
    d_asistencia = 'Ausente'
    d_modificacion = 'Automatico'
    d_fecha = datetime.now()

    # Crear el diccionario de datos del documento curso_alumno
    curso_alumno = {
        'c_codigo_alumno': c_codigo_alumno,
        'c_codigo_curso': c_codigo_curso_manualmente,
        'd_nombre_curso': d_nombre_curso_manualmente,
        'd_nombre': d_nombre,
        'd_codigo': d_codigo,
        'd_asistencia': d_asistencia,
        'd_modificacion': d_modificacion,
        'd_fecha': d_fecha
    }
    # Agregar el diccionario a la lista curso_alumnos
    curso_alumnos.append(curso_alumno)

# Agregar los documentos a la colección curso_alumno para el curso específico
for curso_alumno in curso_alumnos:
    doc_ref = db.collection('curso_alumno').document()
    doc_ref.set(curso_alumno)
'''

# Inscribir un alumno especifico en un CURSO especifico
'''
alumno_ref = db.collection('alumno')
curso_ref = db.collection('curso')

# Obtener los datos del alumno específico
d_nombre_alumno = "Ake"  # Nombre del alumno a agregar
d_codigo_alumno = "qOkp5FPsvTTxBdL9p2CF"  # ID del alumno a agregar
d_codigo = "DEF191" # Codigo del alumno

# ID del curso específico
c_codigo_curso = "guD9sBHBQpJ11WmTzTKb"

# Obtener el documento del curso específico
curso_doc = curso_ref.document(c_codigo_curso).get()

if curso_doc.exists:
    curso_data = curso_doc.to_dict()

    # Nombre del curso específico
    d_nombre_curso = "Retail y Ventas"

    # Crear el diccionario de datos del documento curso_alumno
    curso_alumno = {
        'c_codigo_alumno': d_codigo_alumno,
        'c_codigo_curso': c_codigo_curso,
        'd_nombre_curso': d_nombre_curso,
        'd_nombre': d_nombre_alumno,
        'd_codigo': d_codigo,
        'd_asistencia': 'Ausente',
        'd_modificacion': 'Automático',
        'd_fecha': datetime.now()
    }

    # Agregar el documento curso_alumno a la colección curso_alumno
    doc_ref = db.collection('curso_alumno').document()
    doc_ref.set(curso_alumno)
else:
    print("El curso especificado no existe en la base de datos.")
'''


# Ejecutar el batch para crear los documentos
batch.commit()
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from datetime import datetime

# Use a service account
cred = credentials.Certificate('C:/Users/USUARIO/AA - Proyecto FACE COUNTER/facecounter-7bdad-firebase-adminsdk-zdctb-27c9931a03.json')
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
    {'d_nombre': 'Juan Perez', 'd_codigo': 'ABC123', 'd_urlvideo': 'https://www.youtube.com/watch?v=abcd1234'},
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
    {'d_nombre': 'Riccardo', 'd_codigo': 'DEF988', 'd_urlvideo': 'https://www.youtube.com/watch?v=efgh5678'}
]

for alumno_data in data:
    doc_ref = db.collection('alumno').document()
    batch.set(doc_ref, alumno_data)

'''
###################################################################
# Definir los datos para CURSO_ALUMNO
# Obtener las referencias de las colecciones alumno y curso
'''alumno_ref = db.collection('alumno')
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
# Ejecutar el batch para crear los documentos
batch.commit()



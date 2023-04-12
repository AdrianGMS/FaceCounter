CREATE TABLE Profesor (
    c_codigo_profesor SERIAL PRIMARY KEY,
    d_nombre VARCHAR(50) NOT NULL,
    d_apellido VARCHAR(50) NOT NULL,
    d_correo VARCHAR(50) NOT NULL,
    n_telefono VARCHAR(15) NOT NULL
);

CREATE TABLE Curso (
    c_codigo_curso SERIAL PRIMARY KEY,
    d_nombre VARCHAR(50) NOT NULL,
    d_codigo_seccion VARCHAR(10) NOT NULL,
    d_dia VARCHAR(10) NOT NULL,
    z_hora VARCHAR(10) NOT NULL,
    c_codigo_profesor INT NOT NULL,
    CONSTRAINT fk_curso_profesor FOREIGN KEY (c_codigo_profesor)
        REFERENCES Profesor (c_codigo_profesor)
        ON DELETE CASCADE
);

CREATE TABLE Alumno (
    c_codigo_alumno SERIAL PRIMARY KEY,
    d_nombre VARCHAR(50) NOT NULL,
    d_codigo VARCHAR(10) NOT NULL,
    d_urlvideo VARCHAR(255) NOT NULL
);

CREATE TABLE Curso_Alumno (
    c_codigo_curso_alumno SERIAL PRIMARY KEY,
    c_codigo_curso INT NOT NULL,
    c_codigo_alumno INT NOT NULL,
    CONSTRAINT fk_curso_alumno_curso FOREIGN KEY (c_codigo_curso)
        REFERENCES Curso (c_codigo_curso)
        ON DELETE CASCADE,
    CONSTRAINT fk_curso_alumno_alumno FOREIGN KEY (c_codigo_alumno)
        REFERENCES Alumno (c_codigo_alumno)
        ON DELETE CASCADE
);

CREATE TABLE Asistencia (
    c_codigo_asistencia SERIAL PRIMARY KEY,
    d_nombre_alumno VARCHAR(50) NOT NULL,
    c_codigo_curso_alumno INT NOT NULL,
    d_asistencia VARCHAR(50) NOT NULL,
    CONSTRAINT fk_asistencia_curso_alumno FOREIGN KEY (c_codigo_curso_alumno)
        REFERENCES Curso_Alumno (c_codigo_curso_alumno)
        ON DELETE CASCADE
);
ALTER TABLE asistencia ADD COLUMN c_codigo_curso INTEGER;

///////

--Insertar profesores
INSERT INTO profesor (d_nombre, d_apellido, d_correo, n_telefono) 
VALUES
	('Willy', 'Pérez', 'willyperez@email.com', '123456789'),
	('Julio', 'Sanchez', 'juliosanchez@email.com', '123456789'),
	('Riccardo', 'Mora', 'riccardomora@email.com', '123456789');

--	Insertar alumno
INSERT INTO Alumno (d_nombre, d_codigo, d_urlvideo)
VALUES
    ('Juan Perez', 'ABC123', 'https://www.youtube.com/watch?v=abcd1234'),
    ('Hamill', 'DEF755', 'https://www.youtube.com/watch?v=efgh5678'),
    ('Adrian', 'GHI123', 'https://www.youtube.com/watch?v=ijkl9012'),
	('Aldo', 'DEF468', 'https://www.youtube.com/watch?v=efgh5678'),
	('Natalia', 'DEF987', 'https://www.youtube.com/watch?v=efgh5678'),
	('Elvis', 'DEF345', 'https://www.youtube.com/watch?v=efgh5678'),
	('Daniel', 'DEF733', 'https://www.youtube.com/watch?v=efgh5678'),
	('Eduardo', 'DEF098', 'https://www.youtube.com/watch?v=efgh5678'),
	('Macarena', 'DEF393', 'https://www.youtube.com/watch?v=efgh5678'),
	('Mora', 'DEF009', 'https://www.youtube.com/watch?v=efgh5678'),
	('Pauline', 'DEF711', 'https://www.youtube.com/watch?v=efgh5678'),
	('Ake', 'DEF191', 'https://www.youtube.com/watch?v=efgh5678'),
	('Riccardo', 'DEF988', 'https://www.youtube.com/watch?v=efgh5678');

-- Insertar cursos
INSERT INTO curso (d_nombre, d_codigo_seccion, d_dia, z_hora, c_codigo_profesor)
VALUES 
	('Taller de Proyecto 2', '101A', 'Martes', '16:00', 1),
	('Taller de Proyecto 2', '101A', 'Jueves', '16:00', 1),
	('Matematica computacional', '101A', 'Lunes', '9:00', 2);

--Insertar curso alumnos
INSERT INTO curso_alumno (c_codigo_curso, c_codigo_alumno)
VALUES (1, 1),
       (1, 2),
       (1, 3),
       (1, 4),
       (1, 5),
       (1, 6),
	   (2, 2),
	   (2, 3),
	   (2, 4),
	   (1, 7),
	   (1, 8),
	   (2, 9),
	   (1, 10),
	   (2, 11),
	   (1, 12),
	   (2, 13),
	   (1, 13),
	   (2, 12);
	   

INSERT INTO asistencia (d_nombre_alumno, c_codigo_curso_alumno, d_asistencia, c_codigo_curso)
SELECT a.d_nombre, ca.c_codigo_curso_alumno, Ausente, ca.c_codigo_curso
FROM alumno a
JOIN curso_alumno ca ON a.c_codigo_alumno = ca.c_codigo_alumno
WHERE ca.c_codigo_curso = 1 OR ca.c_codigo_curso = 2;

INSERT INTO asistencia (d_nombre_alumno, c_codigo_curso_alumno, d_asistencia, c_codigo_curso)
SELECT a.d_nombre, ca.c_codigo_curso_alumno, 'Ausente', ca.c_codigo_curso
FROM alumno a
JOIN curso_alumno ca ON a.c_codigo_alumno = ca.c_codigo_alumno
WHERE ca.c_codigo_curso IN (SELECT DISTINCT c_codigo_curso FROM curso_alumno);


--Insertar asistencias
INSERT INTO asistencia (d_nombre_alumno, c_codigo_curso_alumno, d_asistencia)
VALUES ('Juan Perez', 1, ausente),
       ('Hamill', 2, ausente),
       ('Adrian', 3, ausente),
	   ('Aldo', 4, ausente),
	   ('Natalia', 5, ausente),
	   ('Elvis', 6, ausente);

--Dejar tablas vacias
DELETE FROM asistencia;

--Eliminar elementos especificos de tablas
DELETE FROM asistencia WHERE d_nombre_alumno = 'Juan Perez';


SELECT d_nombre_alumno, d_asistencia 
FROM asistencia 
WHERE c_codigo_curso = 1

	   
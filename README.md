# Snowflake-Cafe
# clasealumno0777.py

# Definimos la clase alumno0777
class alumno0777:
    # Inicializamos los atributos con valores vacíos o 0
    nombre = ""
    matricula = ""
    edad = 0
    carrera = ""
    fecha_ingreso = ""
    promedio = 0.0
    estado = ""

    # Función para mostrar los datos del alumno
    def mostrar_datos(self):
        print(f"Nombre: {self.nombre}")
        print(f"Matrícula: {self.matricula}")
        print(f"Edad: {self.edad}")
        print(f"Carrera: {self.carrera}")
        print(f"Fecha de Ingreso: {self.fecha_ingreso}")
        print(f"Promedio: {self.promedio}")
        print(f"Estado: {self.estado}")

    # Función para listar 5 alumnos en una lista
    def Listar_alumnos(self):
        lista_alumnos = [
            "Eliseo", 
            "Juan", 
            "Ana", 
            "Luis", 
            "Maria"
        ]
        return lista_alumnos

    # Función para crear una tupla de 5 profesores
    def Tupla_profes(self):
        tupla_profesores = (
            "Prof. Martínez", 
            "Prof. García", 
            "Prof. Pérez", 
            "Prof. López", 
            "Prof. González"
        )
        return tupla_profesores

    # Función para crear un diccionario de materias y calificaciones
    def Dicionario_materia_califa(self):
        diccionario_materias = {
            "Matemáticas": 85,
            "Física": 90,
            "Química": 88,
            "Historia": 92,
            "Biología": 87
        }
        return diccionario_materias

    # Función para dar de alta a un alumno
    def altas(self):
        print("La operación de alta se realizó correctamente.")

    # Función para dar de baja a un alumno
    def bajas(self):
        print("La operación de baja se realizó correctamente.")

# Creación del objeto alumno
alumno = alumno0777()

# Asignación de datos a los atributos
alumno.nombre = "Eliseo"
alumno.matricula = "20230777"
alumno.edad = 20
alumno.carrera = "Ingeniería"
alumno.fecha_ingreso = "2022-09-01"
alumno.promedio = 92.5
alumno.estado = "Activo"

# Utilización de los objetos
# Mostrar datos del alumno
alumno.mostrar_datos()

# Llamadas a las funciones
print("\nLista de alumnos:")
print(alumno.Listar_alumnos())

print("\nTupla de profesores:")
print(alumno.Tupla_profes())

print("\nDiccionario de materias y calificaciones:")
print(alumno.Dicionario_materia_califa())

# Operaciones de alta y baja
alumno.altas()
alumno.bajas()
## Foto:
- 

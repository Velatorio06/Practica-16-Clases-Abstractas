
from abc import ABC, abstractmethod

class Persona(ABC):
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    @abstractmethod
    def presentarse(self):
        pass

    @abstractmethod
    def actividad_diaria(self):
        pass

    def cumplir_años(self):
        self.edad += 1
        return f"{self.nombre} ahora tiene {self.edad} años"


class Alumno(Persona):
    def __init__(self, nombre, edad, curso):
        self.nombre = nombre
        self.edad = edad
        self.curso = curso

    def presentarse(self):
        return f"Hola, soy {self.nombre}, tengo {self.edad} años y estudio {self.curso}"

    def actividad_diaria(self):
        return f"Voy a clase y estudio {self.curso}"


class Profesor(Persona):
    def __init__(self, nombre, edad, asignatura):
        self.nombre = nombre
        self.edad = edad
        self.asignatura = asignatura

    def presentarse(self):
        return f"Hola, soy {self.nombre}, tengo {self.edad} años y soy profesor de {self.asignatura}"

    def actividad_diaria(self):
        return f"Doy clases de {self.asignatura}"


alumno1 = Alumno("Fernando", 20, "Analisis de Datos")
profesor1 = Profesor("Rufino", 45, "Programación")

for persona in [alumno1, profesor1]:
    print(persona.presentarse())
    print(persona.actividad_diaria())
    print(persona.cumplir_años())


# Si intentamos crear una Persona directamente:
# persona1 = Persona("Pepe", 30)

# Da un TypeError porque Persona es una clase abstracta
# y no se puede crear directamente.

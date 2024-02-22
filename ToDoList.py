from Tarea import Tarea

class TodoList:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self):
        while True:
            descripcion = input("Ingrese la descripción de la nueva tarea: ")
            if descripcion:
                break
            else:
                print("La descripción no puede estar vacía. Inténtelo de nuevo.")

        while True:
            prioridad = input("Ingrese la prioridad de la tarea (baja, media, alta): ")
            if prioridad.lower() in ["baja", "media", "alta"]:
                break
            else:
                print("Prioridad inválida. Por favor, elija entre 'baja', 'media' o 'alta'.")

        estado = "sin iniciar"
        self.tareas.append(Tarea(descripcion, estado, prioridad))
        print("Tarea agregada exitosamente.")

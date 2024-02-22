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
    def marcar_estado(self):
        tareas_disponibles = [tarea for tarea in self.tareas if tarea.estado in ["sin iniciar", "en progreso"]]
        if not tareas_disponibles:
            print("No hay tareas en estado 'sin iniciar' o 'en progreso'.")
            return

        print("Tareas disponibles para marcar estado:")
        for indice, tarea in enumerate(tareas_disponibles, start=1):
            print(f"{indice}. {tarea.descripcion} - Estado: {tarea.estado} - Prioridad: {tarea.prioridad}")

        while True:
            opcion = input("Seleccione el número de la tarea que desea marcar: ")
            if not opcion.isdigit():
                print("Debe ingresar un número válido.")
                continue

            indice = int(opcion)
            if 1 <= indice <= len(tareas_disponibles):
                tarea = tareas_disponibles[indice - 1]
                nuevo_estado = input("Ingrese el nuevo estado de la tarea (en progreso, completado): ")
                if nuevo_estado.lower() in ["en progreso", "completado"]:
                    tarea.estado = nuevo_estado.lower()
                    print(f"Tarea '{tarea.descripcion}' marcada como '{nuevo_estado.lower()}'.")
                    break
                else:
                    print("Estado inválido. Por favor, ingrese 'en progreso' o 'completado'.")
            else:
                print("Número de tarea inválido.")
                continue


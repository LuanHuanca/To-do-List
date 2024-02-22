from ToDoList import TodoList

def menu():
    todo_list = TodoList()
    while True:
        print("\n--- TO-DO LIST ---")
        print("1. Agregar nueva tarea")
        print("2. Marcar estado de tarea")
        print("3. Eliminar tarea")
        print("4. Generar reporte de tareas en curso y no iniciadas")
        print("5. Generar reporte de tareas completadas")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            todo_list.agregar_tarea()
        elif opcion == "2":
            todo_list.marcar_estado()
        elif opcion == "3":
            todo_list.eliminar_tarea()
        elif opcion == "4":
            todo_list.reporte_en_curso_no_iniciadas()
        elif opcion == "5":
            todo_list.reporte_completadas()
        elif opcion == "6":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    menu()
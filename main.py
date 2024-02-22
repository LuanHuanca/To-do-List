def menu():
    while True:
        print("\n--- TO-DO LIST ---")
        print("1. Agregar nueva tarea")
        print("2. Marcar tarea como completada")
        print("3. Eliminar tarea")
        print("4. Generar reporte de tareas en curso y no iniciadas")
        print("5. Generar reporte de tareas completadas")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            print("Funcion agregar tarea")
        elif opcion == "2":
            print("Marcar como completado")
        elif opcion == "3":
            print("Eliminar tarea")
        elif opcion == "4":
            print("Generar reporte de faltantes")
        elif opcion == "5":
            print("Generar reporte de completados")
        elif opcion == "6":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    menu()
# Mensaje de bienvenida
print("-----Bienvenidos a la Task List-----\n")

# Creamos una lista de tareas
lista_tareas = []
opcion = 1

# Creamos un bucle para poder ingresar tareas como asi tambien eliminar tareas
while opcion != 0:
    print("""\n\t------------MENÚ------------
    1) Visualizar la lista de tareas
    2) Ingresar una nueva tarea
    3) Eliminar una tarea
    0) Salir
    """)
    
    opcion = int(input("Ingresar opcion(1-4): "))
    
    if opcion == 1:
        if len(lista_tareas) > 0:
            print("\nListando las tareas")
            for indice, tarea in enumerate(lista_tareas, start=1):
                print(f"Tarea {indice}: {tarea}")
        else:
            print("\nLa lista de tareas esta vacía, ingrese nuevas tareas")
            
    elif opcion == 2:
        print("Ingresando nueva tarea")
        nueva_tarea = input("\nIngrese la tarea: ")
        lista_tareas.append(nueva_tarea)
        print(f"\nLa tarea {nueva_tarea} fue incluida a la lista.")
        
    elif opcion == 3:
        print("Eliminando una tarea de la lista")
        tamaño_lista = len(lista_tareas)
        if tamaño_lista > 0:
            indice_tarea = int(input("\nIngrese el indice de la tarea que quiere eliminar: "))
            if indice_tarea < tamaño_lista and indice_tarea >= 0:
                tarea_eliminada = lista_tareas.pop(indice_tarea)
                print(f"\nLa tarea {tarea_eliminada} fue eliminada exitosamente.")
            else:
                print(f"Error!! el indice de tarea no es valido")
        else:
            print("\nLa lista de tareas esta vacía, ingrese nuevas tareas")
        
    elif opcion == 0:
        print("\nSaliendo del programa ☻☻☻\nHasta luego")
        
    else:
        print("\nOpcion incorrecta...\nVolver a ingresar")
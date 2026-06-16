

def validar_numero(lim_inf, lim_sup):
    
    num = -1
    
    while num > lim_sup or num < lim_inf:
        
        try:
            num = int(input(f"ingresar un valor entre ({lim_inf}-{lim_sup}): "))
            if num > lim_sup or num < lim_inf:
                print(f"el valor no esta dentro del rango ({lim_inf}-{lim_sup})")
        except ValueError:
            print("Error se debe ingresar un valor númerico")
            
    return num


def listar_tareas(tareas):
    for indice, tarea in enumerate(tareas, start=1):
        print(f"Tarea {indice}: {tarea}")


def agregar_tarea(lista):
    nueva_tarea = ""
    
    while nueva_tarea == "":
        nueva_tarea = input("\nIngrese la tarea: ").strip().capitalize()
        if nueva_tarea == "":
            print("Error!!! Ingreso un mensaje vacío")
        else:
            lista.append(nueva_tarea)
            print(f"\nLa tarea {nueva_tarea} fue incluida a la lista.")


def eliminar_tarea(tareas):
    indice = len(tareas) + 1
    
    while indice >= len(tareas):
        listar_tareas(tareas)
        try:
            indice = int(input("Ingrese el indice de la tarea a eliminar: "))
            tarea_eliminada = tareas.pop(indice - 1)
            print(f"\nLa tarea {tarea_eliminada} fue eliminada exitosamente.")
        except IndexError:
            print("El indice que quieras acceder no existe")
        except ValueError:
            print("Error!! se requiere un valor númerico")


# Función que va a tener la interfaz
def menu_opciones(opc=1):
    
    # Mensaje de bienvenida
    print("\t-----Bienvenidos a la Task List-----")
    
    # Creamos un bucle para poder ingresar tareas como asi tambien eliminar tareas
    while opc:
        print("""\n\t------------MENÚ------------
        1) Visualizar la lista de tareas
        2) Ingresar una nueva tarea
        3) Eliminar una tarea
        0) Salir
        """)

        # Creamos una lista de tareas
        lista_tareas = []
        opc = validar_numero(0,3)
        
        if opc == 1:
            if len(lista_tareas) > 0:
                print("\nListando las tareas")
                listar_tareas(lista_tareas)
            else:
                print("\nLa lista de tareas esta vacía, ingrese nuevas tareas")
                
        elif opc == 2:
            print("Ingresando nueva tarea")
            agregar_tarea(lista_tareas)
            
        elif opc == 3:
            print("Eliminando una tarea de la lista")
            if len(lista_tareas) > 0:
                eliminar_tarea(lista_tareas)
            else:
                print("\nLa lista de tareas esta vacía, ingrese nuevas tareas")
            
        elif opc == 0:
            print("\nSaliendo del programa ☻☻☻\nHasta luego")
            
        else:
            print("\nOpcion incorrecta...\nVolver a ingresar")
            
            
menu_opciones()
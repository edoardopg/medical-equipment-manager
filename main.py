from models import create_table, insert_initial_data #importo funciones crear tabla e insertar tabla para arrancar bd
from crud.equipos import Equipos # importo la clase Equipos del CRUD
from crud.incidencias import Incidencias #importo la clase Incidencias del CRUD
from datetime import datetime 
def main():
    create_table()
    insert_initial_data()
    equipo = Equipos() #crea instancia de la clase Equipos
    incidencia = Incidencias() #crea instancia de la clase Incidencias
    while True:
        opcion = input('''Elija una opcion:
            1- Insertar nuevo equipo medico
            2- Listar equipos medicos
            3- Actualizar equipo medico
            4- Eliminar equipo medico
            --------------------------
            5- Crear incidencia
            6- Mostrar incidencias
            7- Actualizar incidencia
            8- Eliminar incidencia
            9- salir
            ''')
        if opcion == '1':
            nombre = input('Ingrese el nombre del equipo medico: ')
            tipo = input('Ingrese el tipo del equipo medico: ')
            ubicacion = input('Ingrese la ubicacion del equipo medico: ')
            equipo.insertar(nombre,tipo,ubicacion) #llama a la funcion insertar de la clase Equipos para insertar un nuevo equipo medico en la tabla equipos_medicos
        elif opcion == '2':
            equipos = equipo.listar() #almacena la consulta select * from equipos medicos
            for e in equipos: #muestra equipos medicos
                print(f"ID: {e[0]} | Nombre: {e[1]} | Tipo: {e[2]} | Ubicación: {e[3]}")  #ej: ID: 1 | Nombre: FLUOROCYCLER | Tipo: Termociclador | Ubicación: Microbiologia

        elif opcion == '3':
            equipos = equipo.listar() #almacena la consulta select * from equipos medicos
            for e in equipos: #muestra equipos medicos
                print(f"ID: {e[0]} | Nombre: {e[1]} | Tipo: {e[2]} | Ubicación: {e[3]}")  #ej: ID: 1 | Nombre: FLUOROCYCLER | Tipo: Termociclador | Ubicación: Microbiologia
            try:
                id_equipo = int(input('Ingrese el ID del equipo medico a actualizar: ')) #pide al usuario el id del equipo medico a actualizar
                equipo_actual = equipo.buscar_por_id(id_equipo)
                if equipo_actual is None:
                    print("Por favor ingrese un ID válido.")
                    continue
            except ValueError:
                print("ID no valido, por favor ingrese un numero entero.")
                continue
            nombre = input('Ingrese el nombre del equipo medico (Enter para mantener el mismo nombre): ')
            if nombre == '':
                nombre = equipo_actual[1] #si el usuario no ingresa un nuevo nombre, se mantiene el nombre actual del equipo medico
            tipo = input('Ingrese el tipo del equipo medico (Enter para mantener el mismo nombre): ')
            if tipo == '':
                tipo = equipo_actual[2]#si el usuario no ingresa un nuevo tipo se mantiene el actual
            ubicacion = input('Ingrese la ubicacion del equipo medico (Enter para mantener el mismo nombre): ')
            if ubicacion =='':
                ubicacion = equipo_actual[3]
            equipo.actualizar(nombre,tipo,ubicacion,id_equipo)
            print("Equipo actualizado correctamente.")
        elif opcion == '4':
            equipos = equipo.listar()
            for e in equipos:
                print(f"ID: {e[0]} | Nombre: {e[1]} | Tipo: {e[2]} | Ubicación: {e[3]}")  #ej: ID: 1 | Nombre: FLUOROCYCLER | Tipo: Termociclador | Ubicación: Microbiologia
            try:
                id_equipo = int(input("Ingrese el ID del equipo medico a eliminar: ")) #pide al usuario el id del equipo medico a eliminar
                equipo_actual = equipo.buscar_por_id(id_equipo)
                if equipo_actual is None:
                    print("Por favor ingrese un ID válido.")
                    continue
            except ValueError:
                print("ID no valido, por favor ingrese un numero entero.")
                continue
            equipo.eliminar(equipo_actual[0])
            print("Equipo eliminado correctamente.")  
        elif opcion == '5':
            equipos = equipo.listar()
            for e in equipos:
                print(f'ID: {e[0]} | Nombre: {e[1]} | Tipo: {e[2]} | Ubicacion: {e[3]}')
            try:
                id_equipo = int(input("ID del equipo con INCIDENCIA."))
                equipo_actual = equipo.buscar_por_id(id_equipo)
                if equipo_actual is None:
                    print("Por favor ingrese un ID válido.")
                    continue
            except ValueError:
                print("Introduzca un ID válido.")
                continue
            tipo_error = input("¿Qué Error tiene?: ")
            descripcion = input("Comente el tipo de error: ")
            fecha = datetime.now().strftime("%d/%m/%y")
            incidencia.insertar(id_equipo,fecha,tipo_error,descripcion)
            print("Incidencia creada correctamente.")
        elif opcion =='6':
            incidencias = incidencia.listar()
            if not incidencias:
                print("No hay incidencias activas.")
            for i in incidencias:
                print(f"ID_Incidencia: {i[0]} | Nombre: {i[5]} | Fecha: {i[2]} | Error: {i[3]} | Descripcion: {i[4]}")
        elif opcion == '7':
            incidencias = incidencia.listar()
            for i in incidencias:
                print(f"ID_Incidencia: {i[0]} | Nombre: {i[5]} | Fecha: {i[2]} | Error: {i[3]} | Descripcion: {i[4]}")
            try:
                id_incidencia = int(input("ID de incidencia a actualizar: "))
                incidencia_actual = incidencia.buscar_por_id(id_incidencia)
                if incidencia_actual is None:
                    print("Por favor ingrese un ID válido.")
                    continue
            except ValueError:
                print("ID no valido.")
                continue
            fecha = datetime.now().strftime("%d/%m/%y")
            tipo_error = input('Ingrese el error (Enter para mantener el mismo nombre): ')
            if tipo_error == '':
                tipo_error = incidencia_actual[3]#si el usuario no ingresa un nuevo error se mantiene el actual
            descripcion = input('Ingrese la descripcion del equipo medico (Enter para mantener el mismo nombre): ')
            if descripcion =='':
                descripcion = incidencia_actual[4]
            incidencia.actualizar(fecha,tipo_error,descripcion,id_incidencia)
            print("Incidencia actualizada correctamente.")
        elif opcion == '8': 
            incidencias = incidencia.listar()
            for i in incidencias:
                print(f"ID_Incidencia: {i[0]} | Nombre: {i[5]} | Fecha: {i[2]} | Error: {i[3]} | Descripcion: {i[4]}")
            try:
                id_incidencia = int(input("ID incidencia a eliminar: ")) 
            except ValueError:
                print("ID incorrecto.")
            incidencia_actual = incidencia.buscar_por_id(id_incidencia)
            if incidencia_actual is None:
                print("Por favor ingrese un ID válido.")
                continue
            incidencia.eliminar(id_incidencia)
            print("Incidencia eliminada correctamente.") 
        elif opcion == '9':
            print('Saliendo del programa...')
            break
        else:
            print('Opcion no valida, por favor intente de nuevo.')
        
if __name__== "__main__":
    main()

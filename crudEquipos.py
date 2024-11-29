import pyodbc

# Declarar variables de Conexión
name_server = 'UPOAULA10423'  # Nombre del servidor SQL
database = 'SGCBP'  # Nombre de la base de datos
username = 'Administrador'  # Usuario para la conexión
password = 'sgc2024a'  # Contraseña del usuario
controlador_odbc = 'ODBC Driver 17 for SQL Server'  # Controlador ODBC para SQL Server.

# Crear Cadena de Conexion
connection_string = f'DRIVER={controlador_odbc};SERVER={name_server};DATABASE={database};UID={username};PWD={password}'

# Función para insertar un nuevo equipo
def insertar_equipo(conexion):
    try:
        cursor = conexion.cursor()
        print("\n\tInserción de un nuevo equipo:")
        nombre_equipo = input("Ingrese el nombre del equipo: ")

        query = "INSERT INTO GENERAL.Equipos (NombreEquipo) VALUES (?)"
        cursor.execute(query, (nombre_equipo,))
        conexion.commit()
        print("\nEquipo insertado exitosamente.")
    except Exception as e:
        print("\nOcurrió un error al insertar el equipo:", e)

# Función para consultar todos los equipos
def consultar_equipos(conexion):
    try:
        cursor = conexion.cursor()
        print("\n\tConsulta de equipos:\n")
        query = "SELECT * FROM GENERAL.Equipos"
        cursor.execute(query)
        rows = cursor.fetchall()

        for row in rows:
            print(f"ID Equipo: {row.IDEquipo}, Nombre: {row.NombreEquipo}")
    except Exception as e:
        print("\nOcurrió un error al consultar los equipos:", e)

# Función para actualizar un equipo
def actualizar_equipo(conexion):
    try:
        cursor = conexion.cursor()
        print("\n\tActualización de un equipo:")
        id_equipo = int(input("Ingrese el ID del equipo a actualizar: "))
        nuevo_nombre = input("Ingrese el nuevo nombre del equipo: ")

        query = "UPDATE GENERAL.Equipos SET NombreEquipo = ? WHERE IDEquipo = ?"
        cursor.execute(query, (nuevo_nombre, id_equipo))
        conexion.commit()
        print("\nEquipo actualizado exitosamente.")
    except Exception as e:
        print("\nOcurrió un error al actualizar el equipo:", e)

# Función para eliminar un equipo
def eliminar_equipo(conexion):
    try:
        cursor = conexion.cursor()
        print("\n\tEliminación de un equipo:")
        id_equipo = int(input("Ingrese el ID del equipo a eliminar: "))

        query = "DELETE FROM GENERAL.Equipos WHERE IDEquipo = ?"
        cursor.execute(query, (id_equipo,))
        conexion.commit()

        if cursor.rowcount > 0:
            print("\nEquipo eliminado exitosamente.")
        else:
            print("\nNo se encontró un equipo con ese ID.")
    except Exception as e:
        print("\nOcurrió un error al eliminar el equipo:", e)

# Menú principal
def mostrar_menu_crud():
    print("\n\t** SISTEMA CRUD - EQUIPOS **\n")
    print("\t1. Añadir equipo")
    print("\t2. Consultar equipos")
    print("\t3. Actualizar equipo")
    print("\t4. Eliminar equipo")
    print("\t5. Salir\n")

# Programa principal
if __name__ == "__main__":
    conexion = conectar_bd()
    if conexion:
        print("\nConexión exitosa.\n")
        while True:
            mostrar_menu_crud()
            opcion = input("Seleccione una opción (1-5): ")

            if opcion == '1':
                insertar_equipo(conexion)
            elif opcion == '2':
                consultar_equipos(conexion)
            elif opcion == '3':
                actualizar_equipo(conexion)
            elif opcion == '4':
                eliminar_equipo(conexion)
            elif opcion == '5':
                print("Saliendo del sistema...")
                break
            else:
                print("Opción no válida.")
        conexion.close()
        print("\nConexión cerrada.")

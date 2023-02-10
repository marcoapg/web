from bd import obtener_conexion

#Read Data

def obtener_amenaza():
    conexion = obtener_conexion()
    amenaza = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT AmenazaID, Descripcion FROM amenaza")
        amenaza = cursor.fetchall()
    conexion.close()
    return amenaza

def obtener_amenaza_por_id(id):
    conexion = obtener_conexion()
    amenaza = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT AmenazaID, Descripcion FROM amenaza WHERE AmenazaID = %s", (id,))
        amenaza = cursor.fetchone()
    conexion.close()
    return amenaza

#Modify Data

#(INSERT)
def insertar_amenaza(descripcion):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO amenaza(descripcion) VALUES (%s)",
                       (descripcion))
    conexion.commit()
    conexion.close()    
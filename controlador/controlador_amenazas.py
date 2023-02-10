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

#Modify Data
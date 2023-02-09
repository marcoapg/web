from bd import obtener_conexion

#Lectura

def obtener_amenaza():
    conexion = obtener_conexion()
    amenaza = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT AmenazaID, Descripcion FROM Amenaza")
        amenaza = cursor.fetchall()
    conexion.close()
    return amenaza
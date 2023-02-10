from bd import obtener_conexion

#Read Data
def obtener_vulnerabilidad():
    conexion = obtener_conexion()
    vulnerabilidad = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT VulnerabilidadID, Descripcion FROM vulnerabilidad")
        vulnerabilidad = cursor.fetchall()
    conexion.close()
    return vulnerabilidad

#Modify Data
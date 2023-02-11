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

def obtener_vulnerabilidad_por_id(id):
    conexion = obtener_conexion()
    vulnerabilidad = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT VulnerabilidadID, Descripcion FROM vulnerabilidad WHERE VulnerabilidadID = %s", (id,))
        vulnerabilidad = cursor.fetchone()
    conexion.close()
    return vulnerabilidad

#Modify Data

#(INSERT)
def insertar_vulnerabilidad(descripcion):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO vulnerabilidad(descripcion) VALUES (%s)",
                       (descripcion))
    conexion.commit()
    conexion.close()    

#(UPDATE)
def actualizar_vulnerabilidad(descripcion, id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE vulnerabilidad SET descripcion = %s WHERE VulnerabilidadID = %s",
                       (descripcion, id))
    conexion.commit()
    conexion.close()

#(DELETE)
def eliminar_vulnerabilidad(id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM vulnerabilidad WHERE VulnerabilidadID = %s", (id,))
    conexion.commit()
    conexion.close()
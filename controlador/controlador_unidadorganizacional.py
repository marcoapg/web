from bd import obtener_conexion

#Read Data

def obtener_unidad_organizacional():
    conexion = obtener_conexion()
    unidad_organizacional = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT UnidadOrganizacionalID, Descripcion FROM unidad_organizacional")
        unidad_organizacional = cursor.fetchall()
    conexion.close()
    return unidad_organizacional

def obtener_unidadorganizacional_por_id(id):
    conexion = obtener_conexion()
    unidadorganizacional = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT UnidadOrganizacionalID, descripcion FROM unidad_organizacional WHERE UnidadOrganizacionalID = %s", (id,))
        unidadorganizacional = cursor.fetchone()
    conexion.close()
    return unidadorganizacional

#Modify Data

#(INSERT)
def insertar_unidadorganizacional(descripcion):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO unidad_organizacional(descripcion) VALUES (%s)",
                       (descripcion))
    conexion.commit()
    conexion.close()    

#(UPDATE)
def actualizar_unidadorganizacional(descripcion, id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE unidad_organizacional SET descripcion = %s WHERE UnidadOrganizacionalID = %s",
                       (descripcion, id))
    conexion.commit()
    conexion.close()

#(DELETE)
def eliminar_unidadorganizacional(id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM unidad_organizacional WHERE UnidadOrganizacionalID = %s", (id,))
    conexion.commit()
    conexion.close()



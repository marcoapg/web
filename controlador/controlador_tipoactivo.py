from bd import obtener_conexion

#Read Data
def obtener_tipoactivo():
    conexion = obtener_conexion()
    tipo_activo=[]
    with conexion.cursor() as cursor:
        cursor.execute("SElECT TipoActivoID,Descripcion from tipo_activo")
        tipo_activo = cursor.fetchall()
    conexion.close()
    return tipo_activo

def obtener_tipoactivo_por_id(id):
    conexion = obtener_conexion()
    tipoactivo = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SElECT TipoActivoID,Descripcion from tipo_activo WHERE TipoActivoID = %s", (id,))
        tipoactivo = cursor.fetchone()
    conexion.close()
    return tipoactivo

#Modify Data

#(INSERT)
def insertar_tipoactivo(descripcion):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO tipo_activo(descripcion) VALUES (%s)",
                       (descripcion))
    conexion.commit()
    conexion.close()    

#(UPDATE)
def actualizar_tipoactivo(descripcion, id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE tipo_activo SET descripcion = %s WHERE TipoActivoID = %s",
                       (descripcion, id))
    conexion.commit()
    conexion.close()

#(DELETE)
def eliminar_tipoactivo(id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM tipo_activo WHERE TipoActivoID = %s", (id,))
    conexion.commit()
    conexion.close()
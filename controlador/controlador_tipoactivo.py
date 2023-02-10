from bd import obtener_conexion

#Read Data
def obtener_tipo_activo():
    conexion = obtener_conexion()
    tipo_activo=[]
    with conexion.cursor() as cursor:
        cursor.execute("SElECT TipoActivoID,Descripcion from tipo_activo")
        tipo_activo = cursor.fetchall()
    conexion.close()
    return tipo_activo

#Modify Data
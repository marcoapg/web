from bd import obtener_conexion

#Read Data
def obtener_criterio_probabilidad():
    conexion = obtener_conexion()
    criterio_probabilidad=[]
    with conexion.cursor() as cursor:
         cursor.execute("select criterio_probabilidadID, Descripcion, Valor from criterio_probabilidad")
         criterio_probabilidad=cursor.fetchall()
    conexion.close()
    return criterio_probabilidad

#Modify Data
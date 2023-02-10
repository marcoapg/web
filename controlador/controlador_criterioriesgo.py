from bd import obtener_conexion

#Read Data
def obtener_criterio_riesgo():
    conexion = obtener_conexion()
    criterio_riesgo=[]
    with conexion.cursor() as cursor:
         cursor.execute("select Criterio_RiesgoID, Descripcion, Color, Valor from criterio_riesgo")
         criterio_riesgo=cursor.fetchall()
    conexion.close()
    return criterio_riesgo

#Modify Data
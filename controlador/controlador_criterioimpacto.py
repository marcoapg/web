from bd import obtener_conexion

#Read Data
def obtener_criterio_impacto():
    conexion = obtener_conexion()
    criterio_impacto=[]
    with conexion.cursor() as cursor:
         cursor.execute("select Criterio_ImpactoID, Descripcion, Valor from criterio_impacto")
         criterio_impacto=cursor.fetchall()
    conexion.close()
    return criterio_impacto

#Modify Data
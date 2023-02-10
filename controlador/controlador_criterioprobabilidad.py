from bd import obtener_conexion

#Read Data
def obtener_criterioprobabilidad():
    conexion = obtener_conexion()
    criterio_probabilidad=[]
    with conexion.cursor() as cursor:
         cursor.execute("select criterio_probabilidadID, Descripcion, Valor from criterio_probabilidad")
         criterio_probabilidad=cursor.fetchall()
    conexion.close()
    return criterio_probabilidad

def obtener_criterioprobabilidad_por_id(id):
    conexion = obtener_conexion()
    criterioprobabilidad = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "select criterio_probabilidadID, Descripcion, Valor from criterio_probabilidad WHERE criterio_probabilidadID = %s", (id,))
        criterioprobabilidad = cursor.fetchone()
    conexion.close()
    return criterioprobabilidad

#Modify Data

#(INSERT)
def insertar_criterioprobabilidad(descripcion,valor):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO criterio_probabilidad(Descripcion,Valor) VALUES (%s,%s)",
                       (descripcion,valor))
    conexion.commit()
    conexion.close()    
from bd import obtener_conexion

#Read Data
def obtener_criterioriesgo():
    conexion = obtener_conexion()
    criterio_riesgo=[]
    with conexion.cursor() as cursor:
         cursor.execute("select Criterio_RiesgoID, Descripcion, Color, Valor from criterio_riesgo")
         criterio_riesgo=cursor.fetchall()
    conexion.close()
    return criterio_riesgo

def obtener_criterioriesgo_por_id(id):
    conexion = obtener_conexion()
    criterioriesgo = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "select Criterio_RiesgoID, Descripcion, Color, Valor from criterio_riesgo WHERE Criterio_RiesgoID = %s", (id,))
        criterioriesgo = cursor.fetchone()
    conexion.close()
    return criterioriesgo

#Modify Data

#(INSERT)
def insertar_criterioriesgo(descripcion,valor,color):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO criterio_riesgo(Descripcion,Valor,Color) VALUES (%s,%s,%s)",
                       (descripcion,valor,color))
    conexion.commit()
    conexion.close()    

#(UPDATE)
def actualizar_criterioriesgo(descripcion,valor,color,id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE criterio_riesgo SET Descripcion = %s, Valor=%s, Color= %s  WHERE Criterio_RiesgoID = %s",
                       (descripcion,valor,color, id))
    conexion.commit()
    conexion.close()

#(DELETE)
def eliminar_criterioriesgo(id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM criterio_riesgo WHERE Criterio_RiesgoID = %s", (id,))
    conexion.commit()
    conexion.close()
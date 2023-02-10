from bd import obtener_conexion

#Read Data
def obtener_criterioimpacto():
    conexion = obtener_conexion()
    criterio_impacto=[]
    with conexion.cursor() as cursor:
         cursor.execute("select Criterio_ImpactoID, Descripcion, Valor from criterio_impacto")
         criterio_impacto=cursor.fetchall()
    conexion.close()
    return criterio_impacto

def obtener_criterioimpacto_por_id(id):
    conexion = obtener_conexion()
    criterioimpacto = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "select Criterio_ImpactoID, Descripcion, Valor from criterio_impacto WHERE Criterio_ImpactoID = %s", (id,))
        criterioimpacto = cursor.fetchone()
    conexion.close()
    return criterioimpacto

#Modify Data

#(INSERT)
def insertar_criterioimpacto(descripcion,valor):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO criterio_impacto(Descripcion,Valor) VALUES (%s,%s)",
                       (descripcion,valor))
    conexion.commit()
    conexion.close()    
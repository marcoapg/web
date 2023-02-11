from bd import obtener_conexion

#Read Data
def obtener_causa():
    conexion = obtener_conexion()
    causa=[]
    with conexion.cursor() as cursor:
        cursor.execute("SELECT cau.CausaID,rie.Descripcion as DescripcionRiesgo,cau.Descripcion as DescripcionCausa from causa cau INNER JOIN riesgo rie on rie.RiesgoID =cau.RiesgoID order by cau.CausaID asc")
        causa = cursor.fetchall()
    conexion.close()
    return causa

def obtener_causa_por_id(id):
    conexion = obtener_conexion()
    causa = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT cau.CausaID,rie.RiesgoID,cau.Descripcion as DescripcionCausa from causa cau INNER JOIN riesgo rie on rie.RiesgoID =cau.RiesgoID WHERE cau.CausaID = %s", (id,))
        causa = cursor.fetchone()
    conexion.close()
    return causa

#Modify Data

#(INSERT)
def insertar_causa(riesgoid,descripcion):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO causa(RiesgoID,Descripcion) VALUES (%s,%s)",
                       (riesgoid,descripcion))
    conexion.commit()
    conexion.close()    

#(UPDATE)
def actualizar_causa(riesgoid,descripcion, id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE causa SET RiesgoID= %s, Descripcion = %s WHERE CausaID = %s",
                       (riesgoid,descripcion, id))
    conexion.commit()
    conexion.close()

#(DELETE)
def eliminar_causa(id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM causa WHERE CausaID = %s", (id,))
    conexion.commit()
    conexion.close()
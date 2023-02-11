from bd import obtener_conexion

#Read Data
def obtener_riego():
    conexion = obtener_conexion()
    riesgo=[]
    with conexion.cursor() as cursor:
        cursor.execute("SELECT rie.RiesgoID,rie.Descripcion,act.Descripcion as DescripcionActivo ,vul.Descripcion as DescripcionVulnerabilidad,ame.Descripcion as DescripcionAmenaza FROM riesgo rie INNER JOIN activo act on (act.ActivoID = rie.ActivoID) INNER JOIN vulnerabilidad vul on (vul.VulnerabilidadID = rie.VulnerabilidadID) INNER JOIN amenaza ame on (ame.AmenazaID = rie.AmenazaID)")
        riesgo = cursor.fetchall()
    conexion.close()
    return riesgo

def obtener_riesgo_por_id(id):
    conexion = obtener_conexion()
    riesgo = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT rie.RiesgoID,rie.Descripcion,act.ActivoID ,vul.VulnerabilidadID,ame.AmenazaID FROM riesgo rie INNER JOIN activo act on (act.ActivoID = rie.ActivoID) INNER JOIN vulnerabilidad vul on (vul.VulnerabilidadID = rie.VulnerabilidadID) INNER JOIN amenaza ame on (ame.AmenazaID = rie.AmenazaID) WHERE rie.RiesgoID = %s", (id,))
        riesgo = cursor.fetchone()
    conexion.close()
    return riesgo

#Modify Data

#(INSERT)
def insertar_riesgo(descripcion,activoid,vulnerabilidadid,amenazaid):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO riesgo(Descripcion,ActivoID,VulnerabilidadID,AmenazaID) VALUES (%s,%s,%s,%s)",
                       (descripcion,activoid,vulnerabilidadid,amenazaid))
    conexion.commit()
    conexion.close()    

#(UPDATE)
def actualizar_riesgo(descripcion,activoid,vulnerabilidadid,amenazaid,id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE riesgo SET Descripcion = %s, ActivoID= %s, VulnerabilidadID= %s,AmenazaID= %s WHERE RiesgoID = %s",
                       (descripcion,activoid,vulnerabilidadid,amenazaid, id))
    conexion.commit()
    conexion.close()

#(DELETE)
def eliminar_riesgo(id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM riesgo WHERE RiesgoID = %s", (id,))
    conexion.commit()
    conexion.close()   
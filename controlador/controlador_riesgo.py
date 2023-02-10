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

#Modify Data
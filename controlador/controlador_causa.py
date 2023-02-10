from bd import obtener_conexion

#Read Data
def obtener_causa():
    conexion = obtener_conexion()
    causa=[]
    with conexion.cursor() as cursor:
        cursor.execute("SELECT cau.CausaID,rie.Descripcion as DescripcionRiesgo,cau.Descripcion as DescripcionCausa from causa cau INNER JOIN riesgo rie on rie.RiesgoID =cau.RiesgoID")
        causa = cursor.fetchall()
    conexion.close()
    return causa

#Modify Data
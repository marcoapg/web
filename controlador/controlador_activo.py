from bd import obtener_conexion

#Read Data
def obtener_activo():
    conexion = obtener_conexion()
    activo=[]
    with conexion.cursor() as cursor:
        cursor.execute("SELECT act.ActivoID,act.Descripcion,tip.Descripcion AS DescripcionTipoActivo,org.Descripcion AS DescripcionUnidadOrganizacional FROM activo act INNER JOIN tipo_activo tip on (act.TipoActivoID = tip.TipoActivoID) INNER JOIN unidad_organizacional org on (act.UnidadOrganizacionalID = org.UnidadOrganizacionalID)")
        activo = cursor.fetchall()
    conexion.close()
    return activo

#Modify Data
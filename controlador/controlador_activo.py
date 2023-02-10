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

def obtener_activo_por_id(id):
    conexion = obtener_conexion()
    activo = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT act.ActivoID,act.Descripcion,act.TipoActivoID,act.UnidadOrganizacionalID FROM activo act INNER JOIN tipo_activo tip on (act.TipoActivoID = tip.TipoActivoID) INNER JOIN unidad_organizacional org on (act.UnidadOrganizacionalID = org.UnidadOrganizacionalID) WHERE act.ActivoID = %s", (id,))
        activo = cursor.fetchone()
    conexion.close()
    return activo

#Modify Data

#(INSERT)
def insertar_activo(descripcion,tipoactivoid,unidadorganizacionalid):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO activo(Descripcion,TipoActivoID,UnidadOrganizacionalID) VALUES (%s,%s,%s)",
                       (descripcion,tipoactivoid,unidadorganizacionalid))
    conexion.commit()
    conexion.close() 

#(UPDATE)
def actualizar_activo(descripcion,tipoactivoid,unidadorganizacionalid, id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE activo SET Descripcion = %s, TipoActivoID= %s, UnidadOrganizacionalID= %s WHERE ActivoID = %s",
                       (descripcion,tipoactivoid,unidadorganizacionalid, id))
    conexion.commit()
    conexion.close()

#(DELETE)
def eliminar_activo(id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM activo WHERE ActivoID = %s", (id,))
    conexion.commit()
    conexion.close()   
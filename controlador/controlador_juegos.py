from bd import obtener_conexion


def insertar_juego(nombre, descripcion, precio):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO juegos(nombre, descripcion, precio) VALUES (%s, %s, %s)",
                       (nombre, descripcion, precio))
    conexion.commit()
    conexion.close()

# Tabla Amenaza

def obtener_amenaza():
    conexion = obtener_conexion()
    amenaza = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT AmenazaID, Descripcion FROM Amenaza")
        amenaza = cursor.fetchall()
    conexion.close()
    return amenaza

# Tabla Vulnerabilidad

def obtener_vulnerabilidad():
    conexion = obtener_conexion()
    vulnerabilidad = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT VulnerabilidadID, Descripcion FROM Vulnerabilidad")
        vulnerabilidad = cursor.fetchall()
    conexion.close()
    return vulnerabilidad

# Tabla Unidad_Organizacional

def obtener_unidad_organizacional():
    conexion = obtener_conexion()
    unidad_organizacional = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT UnidadOrganizacionalID, Descripcion FROM Unidad_Organizacional")
        unidad_organizacional = cursor.fetchall()
    conexion.close()
    return unidad_organizacional
    
# Tabla tipo_activo

def obtener_tipo_activo():
    conexion = obtener_conexion()
    tipo_activo=[]
    with conexion.cursor() as cursor:
        cursor.execute("SElECT TipoActivoID,Descripcion from Tipo_Activo")
        tipo_activo = cursor.fetchall()
    conexion.close()
    return tipo_activo

# Tabla Activo

def obtener_activo():
    conexion = obtener_conexion()
    activo=[]
    with conexion.cursor() as cursor:
        cursor.execute("SELECT act.ActivoID,act.Descripcion,tip.Descripcion AS DescripcionTipoActivo,org.Descripcion AS DescripcionUnidadOrganizacional FROM Activo act INNER JOIN Tipo_Activo tip on (act.TipoActivoID = tip.TipoActivoID) INNER JOIN Unidad_Organizacional org on (act.UnidadOrganizacionalID = org.UnidadOrganizacionalID)")
        activo = cursor.fetchall()
    conexion.close()
    return activo

# Tabla Riesgo
def obtener_riego():
    conexion = obtener_conexion()
    riesgo=[]
    with conexion.cursor() as cursor:
        cursor.execute("SELECT rie.RiesgoID,rie.Descripcion,act.Descripcion as DescripcionActivo ,vul.Descripcion as DescripcionVulnerabilidad,ame.Descripcion as DescripcionAmenaza FROM Riesgo rie INNER JOIN Activo act on (act.ActivoID = rie.ActivoID) INNER JOIN Vulnerabilidad vul on (vul.VulnerabilidadID = rie.VulnerabilidadID) INNER JOIN Amenaza ame on (ame.AmenazaID = rie.AmenazaID)")
        riesgo = cursor.fetchall()
    conexion.close()
    return riesgo

# Tabla Causa
def obtener_causa():
    conexion = obtener_conexion()
    causa=[]
    with conexion.cursor() as cursor:
        cursor.execute("SELECT CausaID,RiesgoID,Descripcion from Causa")
        causa = cursor.fetchall()
    conexion.close()
    return causa

# Tabla Criterio_Impacto
def obtener_criterio_impacto():
    conexion = obtener_conexion()
    criterio_impacto=[]
    with conexion.cursor() as cursor:
         cursor.execute("select Criterio_ImpactoID, Descripcion, Valor from criterio_impacto")
         criterio_impacto=cursor.fetchall()
    conexion.close()
    return criterio_impacto
    
# Tabla Criterio_Probabilidad
def obtener_criterio_probabilidad():
    conexion = obtener_conexion()
    criterio_probabilidad=[]
    with conexion.cursor() as cursor:
         cursor.execute("select criterio_probabilidadID, Descripcion, Valor from criterio_probabilidad")
         criterio_probabilidad=cursor.fetchall()
    conexion.close()
    return criterio_probabilidad
    
# Tabla Criterio_Riesgo
def obtener_criterio_riesgo():
    conexion = obtener_conexion()
    criterio_riesgo=[]
    with conexion.cursor() as cursor:
         cursor.execute("select Criterio_RiesgoID, Descripcion, Color, Valor from criterio_riesgo")
         criterio_riesgo=cursor.fetchall()
    conexion.close()
    return criterio_riesgo
    
# Tabla Registro_Impacto_Probabilidad
def obtener_criterio_impacto_probabilidad():
    conexion = obtener_conexion()
    criterio_impacto_probabilidad=[]
    with conexion.cursor() as cursor:
         cursor.execute("select RIP.Registro_Impacto_ProbabilidadID as ID, CI.Descripcion as Criterio_Impacto, CP.Descripcion as Criterio_Probabilidad, CR.Descripcion as Criterio_Riesgo, R.Descripcion as Riesgo, RIP.UID from registro_impacto_probabilidad RIP inner join criterio_riesgo CR on CR.Criterio_RiesgoID = RIP.Criterio_RiesgoID inner join criterio_probabilidad CP on CP.Criterio_ProbabilidadID = RIP.Criterio_ProbabilidadID inner join criterio_impacto CI on CI.Criterio_ImpactoID = RIP.Criterio_ImpactoID inner join riesgo R on R.RiesgoID = RIP.RiesgoID")
         criterio_impacto_probabilidad=cursor.fetchall()
    conexion.close()
    return criterio_impacto_probabilidad


def eliminar_juego(id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM juegos WHERE id = %s", (id,))
    conexion.commit()
    conexion.close()


def obtener_juego_por_id(id):
    conexion = obtener_conexion()
    juego = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT id, nombre, descripcion, precio FROM juegos WHERE id = %s", (id,))
        juego = cursor.fetchone()
    conexion.close()
    return juego


def actualizar_juego(nombre, descripcion, precio, id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE juegos SET nombre = %s, descripcion = %s, precio = %s WHERE id = %s",
                       (nombre, descripcion, precio, id))
    conexion.commit()
    conexion.close()

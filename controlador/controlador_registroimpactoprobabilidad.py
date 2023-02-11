from bd import obtener_conexion

#Read Data
def obtener_registroimpactoprobabilidad():
    conexion = obtener_conexion()
    registro_impacto_probabilidad=[]
    with conexion.cursor() as cursor:
         cursor.execute("select RIP.Registro_Impacto_ProbabilidadID as ID,  R.Descripcion as Riesgo,CI.Descripcion as Criterio_Impacto, CP.Descripcion as Criterio_Probabilidad, CR.Descripcion as Criterio_Riesgo, RIP.UID from registro_impacto_probabilidad RIP inner join criterio_riesgo CR on CR.Criterio_RiesgoID = RIP.Criterio_RiesgoID inner join criterio_probabilidad CP on CP.Criterio_ProbabilidadID = RIP.Criterio_ProbabilidadID inner join criterio_impacto CI on CI.Criterio_ImpactoID = RIP.Criterio_ImpactoID inner join riesgo R on R.RiesgoID = RIP.RiesgoID")
         registro_impacto_probabilidad=cursor.fetchall()
    conexion.close()
    return registro_impacto_probabilidad

def obtener_registroimpactoprobabilidad_por_id(id):
    conexion = obtener_conexion()
    registroimpactoprobabilidad = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "select RIP.Registro_Impacto_ProbabilidadID as ID, R.RiesgoID, CI.Criterio_ImpactoID, CP.Criterio_ProbabilidadID, CR.Criterio_RiesgoID, RIP.UID from registro_impacto_probabilidad RIP inner join criterio_riesgo CR on CR.Criterio_RiesgoID = RIP.Criterio_RiesgoID inner join criterio_probabilidad CP on CP.Criterio_ProbabilidadID = RIP.Criterio_ProbabilidadID inner join criterio_impacto CI on CI.Criterio_ImpactoID = RIP.Criterio_ImpactoID inner join riesgo R on R.RiesgoID = RIP.RiesgoID WHERE RIP.Registro_Impacto_ProbabilidadID = %s", (id,))
        registroimpactoprobabilidad = cursor.fetchone()
    conexion.close()
    return registroimpactoprobabilidad

#Modify Data

#(INSERT)
def insertar_registroimpactoprobabilidad(riesgoid,criterioimpactoid,criterioprobabilidadid,criterioriesgoid,uid):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO registro_impacto_probabilidad(RiesgoID,Criterio_ImpactoID,Criterio_ProbabilidadID,Criterio_RiesgoID,UID) VALUES (%s)",
                       (riesgoid,criterioimpactoid,criterioprobabilidadid,criterioriesgoid,uid))
    conexion.commit()
    conexion.close()    

#(UPDATE)
def actualizar_registroimpactoprobabilidad(riesgoid,criterioimpactoid,critererioprobabilidadid,criterioriesgoid,uid, id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE registro_impacto_probabilidad SET RiesgoID = %s,Criterio_ImpactoID =%s,Criterio_ProbabilidadID =%s, Criterio_RiesgoID =%s, UID =%s WHERE Registro_Impacto_ProbabilidadID = %s",
                       (riesgoid,criterioimpactoid,critererioprobabilidadid,criterioriesgoid,uid, id))
    conexion.commit()
    conexion.close()

#(DELETE)
def eliminar_registroimpactoprobabilidad(id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM registro_impacto_probabilidad WHERE Registro_Impacto_ProbabilidadID = %s", (id,))
    conexion.commit()
    conexion.close()
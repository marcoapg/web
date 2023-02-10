from bd import obtener_conexion

#Read Data
def obtener_registro_impacto_probabilidad():
    conexion = obtener_conexion()
    registro_impacto_probabilidad=[]
    with conexion.cursor() as cursor:
         cursor.execute("select RIP.Registro_Impacto_ProbabilidadID as ID, CI.Descripcion as Criterio_Impacto, CP.Descripcion as Criterio_Probabilidad, CR.Descripcion as Criterio_Riesgo, R.Descripcion as Riesgo, RIP.UID from registro_impacto_probabilidad RIP inner join criterio_riesgo CR on CR.Criterio_RiesgoID = RIP.Criterio_RiesgoID inner join criterio_probabilidad CP on CP.Criterio_ProbabilidadID = RIP.Criterio_ProbabilidadID inner join criterio_impacto CI on CI.Criterio_ImpactoID = RIP.Criterio_ImpactoID inner join riesgo R on R.RiesgoID = RIP.RiesgoID")
         registro_impacto_probabilidad=cursor.fetchall()
    conexion.close()
    return registro_impacto_probabilidad

#Modify Data
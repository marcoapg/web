class Registro_Impacto_Probabilidad:
    registroimpactoprobabilidadid = 0
    riesgoid=0
    criterioimpactoid = 0
    criterioprobabilidadid=0
    criterioriesgoid=0
    uid = ""
    midic = dict()

    def __init__(self, p_registroimpactoprobabilidadid,p_riesgoid,p_criterioimpactoid,p_criterioprobabilidadid,p_criterioriesgoid,p_uid):
        self.registroimpactoprobabilidadid=p_registroimpactoprobabilidadid
        self.riesgoid=p_riesgoid
        self.criterioimpactoid=p_criterioimpactoid
        self.criterioprobabilidadid=p_criterioprobabilidadid
        self.criterioriesgoid=p_criterioriesgoid
        self.uid=p_uid
        self.midic["registroimpactoprobabilidadid"] = p_registroimpactoprobabilidadid
        self.midic["riesgoid"] = p_riesgoid
        self.midic["criterioimpactoid"] = p_criterioimpactoid
        self.midic["criterioprobabilidadid"]=p_criterioprobabilidadid
        self.midic["criterioriesgoid"]=p_criterioriesgoid
        self.midic["uid"]=p_uid
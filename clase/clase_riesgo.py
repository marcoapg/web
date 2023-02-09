class Riesgo:
    riesgoid = 0
    descripcion = ""
    activoid = 0
    vulnerabilidadid = 0
    amenazaid = 0
    midic = dict()

    def __init__(self, p_riesgoid,p_descripcion,p_activoid,p_vulnerabilidadid,p_amenazaid):
        self.riesgoid = p_riesgoid
        self.descripcion = p_descripcion
        self.activoid = p_activoid
        self.vulnerabilidadid = p_vulnerabilidadid
        self.amenazaid = p_amenazaid
        self.midic["riesgoid"]= p_riesgoid
        self.midic["descripcion"] = p_descripcion
        self.midic["activoid"] = p_activoid
        self.midic["vulnerabilidadid"] = p_vulnerabilidadid
        self.midic["amenazaid"] = p_amenazaid
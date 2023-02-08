class Causa:
    causaid = 0
    descripcion = ""
    riesgoid = 0
    midic = dict()

    def __init__(self, p_causaid,p_descripcion,p_riesgoid):
        self.causaid = p_causaid
        self.descripcion = p_descripcion
        self.riesgoid = p_riesgoid
        self.midic["causaid"]= p_causaid
        self.midic["descripcion"] = p_descripcion
        self.midic["riesgoid"] = p_riesgoid
class Vulnerabilidad:
    vulnerabilidadid = 0
    descripcion = ""
    midic = dict()

    def __init__(self, p_vulnerabilidadid,p_descripcion):
        self.vulnerabilidadid = p_vulnerabilidadid
        self.descripcion = p_descripcion
        self.midic["vulnerabilidadid"]= p_vulnerabilidadid
        self.midic["descripcion"] = p_descripcion

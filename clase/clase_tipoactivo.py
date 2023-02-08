class Tipo_Activo:
    tipoactivoid = 0
    descripcion = ""
    midic = dict()

    def __init__(self, p_tipoactivoid,p_descripcion):
        self.tipoactivoid = p_tipoactivoid
        self.descripcion = p_descripcion
        self.midic["tipoactivoid"]= p_tipoactivoid
        self.midic["descripcion"] = p_descripcion

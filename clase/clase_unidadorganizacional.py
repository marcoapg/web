class Unidad_Organizacional:
    unidadorganizacionalid = 0
    descripcion = ""
    midic = dict()

    def __init__(self, p_unidadorganizacionalid,p_descripcion):
        self.unidadorganizacionalid = p_unidadorganizacionalid
        self.descripcion = p_descripcion
        self.midic["unidadorganizacionalid"]= p_unidadorganizacionalid
        self.midic["descripcion"] = p_descripcion

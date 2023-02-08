class Activo:
    activoid = 0
    descripcion = ""
    tipoactivoid = 0
    unidadorganizacional = 0
    midic = dict()

    def __init__(self, p_activoid,p_descripcion,p_tipoactivoid,p_unidadorganizacionalid):
        self.activoid = p_activoid
        self.descripcion = p_descripcion
        self.tipoactivoid = p_tipoactivoid
        self.unidadorganizacionalid = p_unidadorganizacionalid
        self.midic["activoid"]= p_activoid
        self.midic["descripcion"] = p_descripcion
        self.midic["tipoactivoid"] = p_tipoactivoid
        self.midic["unidadorganizacionalid"] = p_unidadorganizacionalid

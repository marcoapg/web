class Criterio_Impacto:
    criterioimpactoid = 0
    descripcion = ""
    valor=0
    midic = dict()

    def __init__(self, p_criterioimpactoid,p_descripcion,p_valor):
        self.tipoactivoid = p_criterioimpactoid
        self.descripcion = p_descripcion
        self.valor = p_valor
        self.midic["criterioimpactoid"]= p_criterioimpactoid
        self.midic["descripcion"] = p_descripcion
        self.midic["valor"] = p_valor

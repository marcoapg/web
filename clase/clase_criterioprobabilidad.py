class Criterio_Probabilidad:
    criterioprobabilidadid = 0
    descripcion = ""
    valor=0
    midic = dict()

    def __init__(self, p_criterioprobabilidadid,p_descripcion,p_valor):
        self.tipoactivoid = p_criterioprobabilidadid
        self.descripcion = p_descripcion
        self.valor = p_valor
        self.midic["criterioprobabilidadid"]= p_criterioprobabilidadid
        self.midic["descripcion"] = p_descripcion
        self.midic["valor"] = p_valor

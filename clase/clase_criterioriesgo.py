class Criterio_Riesgo:
    criterioriesgoid = 0
    descripcion = ""
    valor=0
    color = ""
    midic = dict()

    def __init__(self, p_criterioriesgoid,p_descripcion,p_valor,p_color):
        self.criterioriesgoid = p_criterioriesgoid
        self.descripcion = p_descripcion
        self.valor = p_valor
        self.color = p_color
        self.midic["criterioriesgoid"]= p_criterioriesgoid
        self.midic["descripcion"] = p_descripcion
        self.midic["valor"] = p_valor
        self.midic["color"] = p_color

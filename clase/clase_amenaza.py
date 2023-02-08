class Amenaza:
    amenzaid = 0
    descripcion = ""
    midic = dict()

    def __init__(self, p_amenazaid,p_descripcion):
        self.amenzaid = p_amenazaid
        self.descripcion = p_descripcion
        self.midic["amenazaid"]= p_amenazaid
        self.midic["descripcion"] = p_descripcion

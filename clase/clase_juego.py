class Juego:
    nombre = ""
    descripcion = ""
    precio = 0
    midic = dict()

    def __init__(self, p_nombre, p_descripcion, p_precio):
        self.nombre = p_nombre
        self.descripcion = p_descripcion
        self.precio = p_precio
        self.midic["name"] = p_nombre
        self.midic["description"] = p_descripcion
        self.midic["price"] = p_precio


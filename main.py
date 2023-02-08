import json
from flask import Flask, render_template, request, redirect, flash, jsonify
import controlador.controlador_juegos as controlador_juegos
import clase.clase_juego as clase_juego

app = Flask(__name__)

# APIs - Inicio

@app.route("/api_obtenerjuegos")
def api_obtenerjuegos():
    try:
        juegos = controlador_juegos.obtener_juegos()
        listaserializable = []
        for juego in juegos:
            miobj = clase_juego.Juego(juego[0], juego[1], juego[2])
            listaserializable.append(miobj.midic.copy())
        return jsonify(listaserializable)
    except:
        return jsonify({"Mensaje":"Error interno. Llame al Administrador de sistemas (+51) 969 696 969"})

@app.route("/api_guardarjuego", methods=["POST"])
def api_guardarjuego():
    nombre = request.json["nombre"]
    descripcion = request.json["descripcion"]
    precio = request.json["precio"]
    controlador_juegos.insertar_juego(nombre, descripcion, precio)
    # De cualquier modo, y si todo fue bien, redireccionar
    return jsonify({"Mensaje":"Juego registrado correctamente"})

@app.route("/api_actualizarjuego", methods=["POST"])
def api_actualizarjuego():
    id = request.json["id"]
    nombre = request.json["nombre"]
    descripcion = request.json["descripcion"]
    precio = request.json["precio"]
    controlador_juegos.actualizar_juego(nombre, descripcion, precio, id)
    return jsonify({"Mensaje":"Juego actualizado correctamente"})

@app.route("/api_eliminarjuego", methods=["POST"])
def api_eliminarjuego():
    controlador_juegos.eliminar_juego(request.json["id"])
    return jsonify({"Mensaje":"Juego eliminado correctamente"})

# APIs - Fin

@app.route("/agregar_juego")
def formulario_agregar_juego():
    return render_template("agregar_juego.html")


@app.route("/guardar_juego", methods=["POST"])
def guardar_juego():
    nombre = request.form["nombre"]
    descripcion = request.form["descripcion"]
    precio = request.form["precio"]
    controlador_juegos.insertar_juego(nombre, descripcion, precio)
    # De cualquier modo, y si todo fue bien, redireccionar
    return redirect("/juegos")


@app.route("/")
@app.route("/juegos")
def juegos():
    juegos = controlador_juegos.obtener_juegos()
    return render_template("juegos.html", juegos=juegos)


@app.route("/eliminar_juego", methods=["POST"])
def eliminar_juego():
    controlador_juegos.eliminar_juego(request.form["id"])
    return redirect("/juegos")


@app.route("/formulario_editar_juego/<int:id>")
def editar_juego(id):
    # Obtener el juego por ID
    juego = controlador_juegos.obtener_juego_por_id(id)
    return render_template("editar_juego.html", juego=juego)


@app.route("/actualizar_juego", methods=["POST"])
def actualizar_juego():
    id = request.form["id"]
    nombre = request.form["nombre"]
    descripcion = request.form["descripcion"]
    precio = request.form["precio"]
    controlador_juegos.actualizar_juego(nombre, descripcion, precio, id)
    return redirect("/juegos")


# Iniciar el servidor
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)

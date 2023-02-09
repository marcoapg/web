import json
from flask import Flask, render_template, request, redirect, flash, jsonify
#Controladores
import controlador.controlador_juegos as controlador_juegos
import controlador.controlador_unidadorganizacional as controlador_unidadorganizacional

#Clases
import clase.clase_juego as clase_juego
import clase.clase_unidadorganizacional as clase_unidadorganizacional
import clase.clase_tipoactivo as clase_tipoactivo
import clase.clase_causa as clase_causa
import clase.clase_amenaza as clase_amenaza
import clase.clase_vulnerabilidad as clase_vulnerabilidad
import clase.clase_activo as clase_activo
import clase.clase_riesgo as clase_riesgo


app = Flask(__name__)

# APIs - Inicio

# @app.route("/api_obtenerjuegos")
# def api_obtenerjuegos():
#     try:
#         juegos = controlador_juegos.obtener_juegos()
#         listaserializable = []
#         for juego in juegos:
#             miobj = clase_juego.Juego(juego[0], juego[1], juego[2])
#             listaserializable.append(miobj.midic.copy())
#         return jsonify(listaserializable)
#     except:
#         return jsonify({"Mensaje":"Error interno. Llame al Administrador de sistemas (+51) 969 696 969"})

# @app.route("/api_guardarjuego", methods=["POST"])
# def api_guardarjuego():
#     nombre = request.json["nombre"]
#     descripcion = request.json["descripcion"]
#     precio = request.json["precio"]
#     controlador_juegos.insertar_juego(nombre, descripcion, precio)
#     # De cualquier modo, y si todo fue bien, redireccionar
#     return jsonify({"Mensaje":"Juego registrado correctamente"})

# @app.route("/api_actualizarjuego", methods=["POST"])
# def api_actualizarjuego():
#     id = request.json["id"]
#     nombre = request.json["nombre"]
#     descripcion = request.json["descripcion"]
#     precio = request.json["precio"]
#     controlador_juegos.actualizar_juego(nombre, descripcion, precio, id)
#     return jsonify({"Mensaje":"Juego actualizado correctamente"})

# @app.route("/api_eliminarjuego", methods=["POST"])
# def api_eliminarjuego():
#     controlador_juegos.eliminar_juego(request.json["id"])
#     return jsonify({"Mensaje":"Juego eliminado correctamente"})

# APIs - Fin

# @app.route("/agregar_juego")
# def formulario_agregar_juego():
#     return render_template("agregar_juego.html")


# @app.route("/guardar_juego", methods=["POST"])
# def guardar_juego():
#     nombre = request.form["nombre"]
#     descripcion = request.form["descripcion"]
#     precio = request.form["precio"]
#     controlador_juegos.insertar_juego(nombre, descripcion, precio)
#     # De cualquier modo, y si todo fue bien, redireccionar
#     return redirect("/juegos")

# @app.route("/eliminar_juego", methods=["POST"])
# def eliminar_juego():
#     controlador_juegos.eliminar_juego(request.form["id"])
#     return redirect("/juegos")


# @app.route("/formulario_editar_juego/<int:id>")
# def editar_juego(id):
#     # Obtener el juego por ID
#     juego = controlador_juegos.obtener_juego_por_id(id)
#     return render_template("editar_juego.html", juego=juego)


# @app.route("/actualizar_juego", methods=["POST"])
# def actualizar_juego():
#     id = request.form["id"]
#     nombre = request.form["nombre"]
#     descripcion = request.form["descripcion"]
#     precio = request.form["precio"]
#     controlador_juegos.actualizar_juego(nombre, descripcion, precio, id)
#     return redirect("/juegos")

# @app.route("/")
# @app.route("/juegos")
# def juegos():
#     juegos = controlador_juegos.obtener_juegos()
#     return render_template("juegos.html", juegos=juegos)


#---------------------------------------------------------PROYECTO - Inicio

@app.route("/")
@app.route("/inicio")
def inicio():

    return render_template("maestra.html",title='ControlRiesgos')

#Templates - Inicio

#(Unidad Organizacional)
@app.route("/")
@app.route("/unidadesorganizacionales")
def unidadesorganizacionales():
    unidadesorganizacionales = controlador_unidadorganizacional.obtener_unidad_organizacional()
    return render_template("unidadesorganizacionales.html", unidadesorganizacionales=unidadesorganizacionales)

@app.route("/agregar_unidadorganizacional")
def formulario_agregar_unidadorganizacional():
    return render_template("agregar_unidadorganizacional.html")

@app.route("/formulario_editar_unidadorganizacional/<int:id>")
def editar_unidadorganizacional(id):
    # Obtener el juego por ID
    unidadorganizacional = controlador_unidadorganizacional.obtener_unidadorganizacional_por_id(id)
    return render_template("editar_unidadorganizacional.html", unidadorganizacional=unidadorganizacional)

#(Tipo Activo)
@app.route("/")
@app.route("/tiposactivo")
def tiposactivo():
    tiposactivo = controlador_juegos.obtener_tipo_activo()
    return render_template("tiposactivo.html", tiposactivo=tiposactivo)

#Templates - Fin




#CRUD Templates - Inicio

@app.route("/guardar_unidadorganizacional", methods=["POST"])
def guardar_unidadorganizacional():
    descripcion = request.form["descripcion"]
    controlador_juegos.insertar_unidadorganizacional(descripcion)
    # De cualquier modo, y si todo fue bien, redireccionar
    return redirect("/unidadesorganizacionales")

@app.route("/actualizar_unidadorganizacional", methods=["POST"])
def actualizar_unidadorganizacional():
    id = request.form["id"]
    descripcion = request.form["descripcion"]
    controlador_unidadorganizacional.actualizar_unidadorganizacional(descripcion, id)
    return redirect("/unidadesorganizacionales")

@app.route("/eliminar_unidadorganizacional", methods=["POST"])
def eliminar_unidadorganizacional():
    controlador_unidadorganizacional.eliminar_unidadorganizacional(request.form["id"])
    return redirect("/unidadesorganizacionales")

#CRUD Templates - Fin




#API's CRUD Unidad Organizacional - Inicio

@app.route("/api_obtenerunidadesorganizacionales")
def api_obtenerunidadesorganizacionales():
    try:
        unidadesorganizacionales = controlador_unidadorganizacional.obtener_unidad_organizacional()
        listaserializable = []
        for unidadesorganizacional in unidadesorganizacionales:
            miobj = clase_unidadorganizacional.Unidad_Organizacional(unidadesorganizacional[0], unidadesorganizacional[1])
            listaserializable.append(miobj.midic.copy())
        return jsonify(listaserializable)
    except:
        return jsonify({"Mensaje":"Error interno. Llame al Administrador de sistemas (+51) 969 696 969"})

@app.route("/api_guardar_unidadorganizacional", methods=["POST"])
def api_guardar_unidadorganizacional():
    descripcion = request.json["descripcion"]
    controlador_juegos.insertar_unidadorganizacional(descripcion)
    # De cualquier modo, y si todo fue bien, redireccionar
    return jsonify({"Mensaje":"Unidad Organizacional registrado correctamente"})

#API's CRUD Unidad Organizacional - Fin


#API's CRUD Tipo Activo - Inicio

@app.route("/api_obtenertiposactivo")
def api_obtenertiposactivo():
    try:
        tiposactivo = controlador_juegos.obtener_tipo_activo()
        listaserializable = []
        for tipoactivo in tiposactivo:
            miobj = clase_tipoactivo.Tipo_Activo(tipoactivo[0], tipoactivo[1])
            listaserializable.append(miobj.midic.copy())
        return jsonify(listaserializable)
    except:
        return jsonify({"Mensaje":"Error interno. Llame al Administrador de sistemas (+51) 969 696 969"})

#API's CRUD Tipo Activo - Fin

#API's CRUD Amenaza - Inicio

@app.route("/api_obteneramenazas")
def api_obteneramenazas():
    try:
        amenazas = controlador_juegos.obtener_amenaza()
        listaserializable = []
        for amenaza in amenazas:
            miobj = clase_amenaza.Amenaza(amenaza[0], amenaza[1])
            listaserializable.append(miobj.midic.copy())
        return jsonify(listaserializable)
    except:
        return jsonify({"Mensaje":"Error interno. Llame al Administrador de sistemas (+51) 969 696 969"})

#API's CRUD Amenaza - Fin

#API's CRUD Vulnerabilidad - Inicio

@app.route("/api_obtenervulnerabilidades")
def api_obtenervulnerabilidades():
    try:
        vulnerabilidades = controlador_juegos.obtener_vulnerabilidad()
        listaserializable = []
        for vulnerabilidad in vulnerabilidades:
            miobj = clase_vulnerabilidad.Vulnerabilidad(vulnerabilidad[0], vulnerabilidad[1])
            listaserializable.append(miobj.midic.copy())
        return jsonify(listaserializable)
    except:
        return jsonify({"Mensaje":"Error interno. Llame al Administrador de sistemas (+51) 969 696 969"})

#API's CRUD Vulnerabilidad - Fin

#API's CRUD Vulnerabilidad - Inicio

@app.route("/api_obteneractivos")
def api_obteneractivos():
    try:
        activos = controlador_juegos.obtener_activo()
        listaserializable = []
        for activo in activos:
            miobj = clase_activo.Activo(activo[0], activo[1],activo[2],activo[3])
            listaserializable.append(miobj.midic.copy())
        return jsonify(listaserializable)
    except:
        return jsonify({"Mensaje":"Error interno. Llame al Administrador de sistemas (+51) 969 696 969"})

#API's CRUD Vulnerabilidad - Fin

#API's CRUD Riesgo - Inicio

@app.route("/api_obtenerriesgos")
def api_obtenerriesgos():
    try:
        riesgos = controlador_juegos.obtener_riego()
        listaserializable = []
        for riesgo in riesgos:
            miobj = clase_riesgo.Riesgo(riesgo[0], riesgo[1],riesgo[2],riesgo[3],riesgo[4])
            listaserializable.append(miobj.midic.copy())
        return jsonify(listaserializable)
    except:
        return jsonify({"Mensaje":"Error interno. Llame al Administrador de sistemas (+51) 969 696 969"})

#API's CRUD Riesgo - Fin

#API's CRUD Riesgo - Inicio

@app.route("/api_obtenercausas")
def api_obtenercausas():
    try:
        causas = controlador_juegos.obtener_causa()
        listaserializable = []
        for causa in causas:
            miobj = clase_causa.Causa(causa[0], causa[1],causa[2])
            listaserializable.append(miobj.midic.copy())
        return jsonify(listaserializable)
    except:
        return jsonify({"Mensaje":"Error interno. Llame al Administrador de sistemas (+51) 969 696 969"})

#API's CRUD Riesgo - Fin



# Iniciar el servidor
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)

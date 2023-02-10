import json
from flask import Flask, render_template, request, redirect, flash, jsonify
#Controladores
import controlador.controlador_juegos as controlador_juegos
import controlador.controlador_unidadorganizacional as controlador_unidadorganizacional
import controlador.controlador_activo as controlador_activo
import controlador.controlador_tipoactivo as controlador_tipoactivo
import controlador.controlador_amenaza as controlador_amenaza
import controlador.controlador_vulnerabilidad as controlador_vulnerabilidad
import controlador.controlador_criterioimpacto as controlador_criterioimpacto
import controlador.controlador_criterioprobabilidad as controlador_criterioprobabilidad
import controlador.controlador_criterioriesgo as controlador_criterioriesgo
import controlador.controlador_causa as controlador_causa
import controlador.controlador_riesgo as controlador_riesgo
import controlador.controlador_registroimpactoprobabilidad as controlador_registroimpactoprobabilidad


#Clases
import clase.clase_juego as clase_juego
import clase.clase_unidadorganizacional as clase_unidadorganizacional
import clase.clase_tipoactivo as clase_tipoactivo
import clase.clase_causa as clase_causa
import clase.clase_amenaza as clase_amenaza
import clase.clase_vulnerabilidad as clase_vulnerabilidad
import clase.clase_activo as clase_activo
import clase.clase_riesgo as clase_riesgo
import clase.clase_criterioimpacto as clase_criterioimpacto
import clase.clase_criterioriesgo as clase_criterioriesgo
import clase.clase_criterioprobabilidad as  clase_criterioprobabilidad
import clase.clase_registroimpactoprobabilidad as clase_registroimpactoprobabilidad

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
    tiposactivo = controlador_tipoactivo.obtener_tipoactivo()
    return render_template("tiposactivo.html", tiposactivo=tiposactivo)

@app.route("/agregar_tipoactivo")
def formulario_agregar_tipoactivo():
    return render_template("agregar_tipoactivo.html")

@app.route("/formulario_editar_tipoactivo/<int:id>")
def editar_tipoactivo(id):
    # Obtener el juego por ID
    tipoactivo = controlador_tipoactivo.obtener_tipoactivo_por_id(id)
    return render_template("editar_tipoactivo.html", tipoactivo=tipoactivo)

#(Activo)
@app.route("/")
@app.route("/activos")
def activos():
    activos = controlador_activo.obtener_activo()
    return render_template("activos.html", activos=activos)

@app.route("/agregar_activo")
def formulario_agregar_activo():
    return render_template("agregar_activo.html")

@app.route("/formulario_editar_activo/<int:id>")
def editar_activo(id):
    # Obtener el juego por ID
    activo = controlador_activo.obtener_activo_por_id(id)
    return render_template("editar_activo.html", activo=activo)


#Templates - Fin




#CRUD Templates - Inicio

#(Unidad Organizacional)
@app.route("/guardar_unidadorganizacional", methods=["POST"])
def guardar_unidadorganizacional():
    descripcion = request.form["descripcion"]
    controlador_unidadorganizacional.insertar_unidadorganizacional(descripcion)
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

#(Tipo Activo)
@app.route("/guardar_tipoactivo", methods=["POST"])
def guardar_tipoactivo():
    descripcion = request.form["descripcion"]
    controlador_tipoactivo.insertar_tipoactivo(descripcion)
    # De cualquier modo, y si todo fue bien, redireccionar
    return redirect("/tiposactivo")

@app.route("/actualizar_tipoactivo", methods=["POST"])
def actualizar_tipoactivo():
    id = request.form["id"]
    descripcion = request.form["descripcion"]
    controlador_tipoactivo.actualizar_tipoactivo(descripcion, id)
    return redirect("/tiposactivo")

@app.route("/eliminar_tipoactivo", methods=["POST"])
def eliminar_tipoactivo():
    controlador_tipoactivo.eliminar_tipoactivo(request.form["id"])
    return redirect("/tiposactivo")

#(Activo)
@app.route("/guardar_activo", methods=["POST"])
def guardar_activo():
    descripcion = request.form["descripcion"]
    tipoactivoid = request.form["tipoactivoid"]
    unidadorganizacionalid = request.form["unidadorganizacionalid"]
    controlador_activo.insertar_activo(descripcion,tipoactivoid,unidadorganizacionalid)
    # De cualquier modo, y si todo fue bien, redireccionar
    return redirect("/activos")

@app.route("/actualizar_activo", methods=["POST"])
def actualizar_activo():
    id = request.form["id"]
    descripcion = request.form["descripcion"]
    tipoactivoid = request.form["tipoactivoid"]
    unidadorganizacionalid = request.form["unidadorganizacionalid"]

    controlador_activo.actualizar_activo(descripcion,tipoactivoid,unidadorganizacionalid,id)
    return redirect("/activos")

@app.route("/eliminar_activo", methods=["POST"])
def eliminar_activo():
    controlador_activo.eliminar_activo(request.form["id"])
    return redirect("/activos")

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

@app.route("/api_guardarunidadorganizacional", methods=["POST"])
def api_guardarunidadorganizacional():
    descripcion = request.json["descripcion"]
    controlador_unidadorganizacional.insertar_unidadorganizacional(descripcion)
    # De cualquier modo, y si todo fue bien, redireccionar
    return jsonify({"Mensaje":"Unidad Organizacional registrada correctamente"})

#API's CRUD Unidad Organizacional - Fin


#API's CRUD Tipo Activo - Inicio

@app.route("/api_obtenertiposactivo")
def api_obtenertiposactivo():
    try:
        tiposactivo = controlador_tipoactivo.obtener_tipo_activo()
        listaserializable = []
        for tipoactivo in tiposactivo:
            miobj = clase_tipoactivo.Tipo_Activo(tipoactivo[0], tipoactivo[1])
            listaserializable.append(miobj.midic.copy())
        return jsonify(listaserializable)
    except:
        return jsonify({"Mensaje":"Error interno. Llame al Administrador de sistemas (+51) 969 696 969"})

@app.route("/api_guardartipoactivo", methods=["POST"])
def api_guardartipoactivo():
    descripcion = request.json["descripcion"]
    controlador_tipoactivo.insertar_tipoactivo(descripcion)
    # De cualquier modo, y si todo fue bien, redireccionar
    return jsonify({"Mensaje":"Tipo Activo registrado correctamente"})

#API's CRUD Tipo Activo - Fin

#API's CRUD Amenaza - Inicio

@app.route("/api_obteneramenazas")
def api_obteneramenazas():
    try:
        amenazas = controlador_amenaza.obtener_amenaza()
        listaserializable = []
        for amenaza in amenazas:
            miobj = clase_amenaza.Amenaza(amenaza[0], amenaza[1])
            listaserializable.append(miobj.midic.copy())
        return jsonify(listaserializable)
    except:
        return jsonify({"Mensaje":"Error interno. Llame al Administrador de sistemas (+51) 969 696 969"})

@app.route("/api_guardaramenaza", methods=["POST"])
def api_guardaramenaza():
    descripcion = request.json["descripcion"]
    controlador_amenaza.insertar_amenaza(descripcion)
    # De cualquier modo, y si todo fue bien, redireccionar
    return jsonify({"Mensaje":"Amenaza registrada correctamente"})

#API's CRUD Amenaza - Fin

#API's CRUD Vulnerabilidad - Inicio

@app.route("/api_obtenervulnerabilidades")
def api_obtenervulnerabilidades():
    try:
        vulnerabilidades = controlador_vulnerabilidad.obtener_vulnerabilidad()
        listaserializable = []
        for vulnerabilidad in vulnerabilidades:
            miobj = clase_vulnerabilidad.Vulnerabilidad(vulnerabilidad[0], vulnerabilidad[1])
            listaserializable.append(miobj.midic.copy())
        return jsonify(listaserializable)
    except:
        return jsonify({"Mensaje":"Error interno. Llame al Administrador de sistemas (+51) 969 696 969"})

@app.route("/api_guardarvulnerabilidad", methods=["POST"])
def api_guardarvulnerabilidad():
    descripcion = request.json["descripcion"]
    controlador_vulnerabilidad.insertar_vulnerabilidad(descripcion)
    # De cualquier modo, y si todo fue bien, redireccionar
    return jsonify({"Mensaje":"Vulnerabilidad registrada correctamente"})

#API's CRUD Vulnerabilidad - Fin

#API's CRUD Vulnerabilidad - Inicio

@app.route("/api_obteneractivos")
def api_obteneractivos():
    try:
        activos = controlador_activo.obtener_activo()
        listaserializable = []
        for activo in activos:
            miobj = clase_activo.Activo(activo[0], activo[1],activo[2],activo[3])
            listaserializable.append(miobj.midic.copy())
        return jsonify(listaserializable)
    except:
        return jsonify({"Mensaje":"Error interno. Llame al Administrador de sistemas (+51) 969 696 969"})

@app.route("/api_guardaractivo", methods=["POST"])
def api_guardaractivo():
    descripcion = request.json["descripcion"]
    tipoactivoid = request.json["tipoactivoid"]
    unidadorganizacionalid = request.json["unidadesorganizacionalid"]
    controlador_activo.insertar_activo(descripcion,tipoactivoid,unidadorganizacionalid)
    # De cualquier modo, y si todo fue bien, redireccionar
    return jsonify({"Mensaje":"Activo registrado correctamente"})

#API's CRUD Vulnerabilidad - Fin

#API's CRUD Riesgo - Inicio

@app.route("/api_obtenerriesgos")
def api_obtenerriesgos():
    try:
        riesgos = controlador_riesgo.obtener_riego()
        listaserializable = []
        for riesgo in riesgos:
            miobj = clase_riesgo.Riesgo(riesgo[0], riesgo[1],riesgo[2],riesgo[3],riesgo[4])
            listaserializable.append(miobj.midic.copy())
        return jsonify(listaserializable)
    except:
        return jsonify({"Mensaje":"Error interno. Llame al Administrador de sistemas (+51) 969 696 969"})

@app.route("/api_guardarriesgo", methods=["POST"])
def api_guardarriesgo():
    descripcion = request.json["descripcion"]
    activoid = request.json["activoid"]
    vulnerabilidadid = request.json["vulnerabilidadid"]    
    amenazaid = request.json["amenazaid"]
    controlador_riesgo.insertar_riesgo(descripcion,activoid,vulnerabilidadid,amenazaid)
    # De cualquier modo, y si todo fue bien, redireccionar
    return jsonify({"Mensaje":"Riesgo registrado correctamente"})

#API's CRUD Riesgo - Fin

#API's CRUD Riesgo - Inicio

@app.route("/api_obtenercausas")
def api_obtenercausas():
    try:
        causas = controlador_causa.obtener_causa()
        listaserializable = []
        for causa in causas:
            miobj = clase_causa.Causa(causa[0], causa[1],causa[2])
            listaserializable.append(miobj.midic.copy())
        return jsonify(listaserializable)
    except:
        return jsonify({"Mensaje":"Error interno. Llame al Administrador de sistemas (+51) 969 696 969"})

@app.route("/api_guardarcausa", methods=["POST"])
def api_guardarcausa():
    riesgoid = request.json["riesgoid"]
    descripcion = request.json["descripcion"]
    controlador_causa.insertar_causa(riesgoid,descripcion)
    # De cualquier modo, y si todo fue bien, redireccionar
    return jsonify({"Mensaje":"Causa registrada correctamente"})

#API's CRUD Riesgo - Fin

#API's CRUD Criterio Impacto - Inicio

@app.route("/api_obtenercriteriosimpacto")
def api_obtenercriteriosimpacto():
    try:
        criteriosimpacto = controlador_criterioimpacto.obtener_criterioimpacto()
        listaserializable = []
        for criterioimpacto in criteriosimpacto:
            miobj = clase_criterioimpacto.Criterio_Impacto(criterioimpacto[0], criterioimpacto[1],criterioimpacto[2])
            listaserializable.append(miobj.midic.copy())
        return jsonify(listaserializable)
    except:
        return jsonify({"Mensaje":"Error interno. Llame al Administrador de sistemas (+51) 969 696 969"})

@app.route("/api_guardarcriterioimpacto", methods=["POST"])
def api_guardarcriterioimpacto():
    descripcion = request.json["descripcion"]
    valor = request.json["valor"]
    controlador_criterioimpacto.insertar_criterioimpacto(descripcion,valor)
    # De cualquier modo, y si todo fue bien, redireccionar
    return jsonify({"Mensaje":"Criterio Impacto registrado correctamente"})

#API's CRUD Criterio Impacto - Fin

#API's CRUD Criterio Probabilidad - Inicio

@app.route("/api_obtenercriteriosprobabilidad")
def api_obtenercriteriosprobabilidad():
    try:
        criteriosprobabilidad = controlador_criterioprobabilidad.obtener_criterioprobabilidad()
        listaserializable = []
        for criterioprobabilidad in criteriosprobabilidad:
            miobj = clase_criterioprobabilidad.Criterio_Probabilidad(criterioprobabilidad[0], criterioprobabilidad[1],criterioprobabilidad[2])
            listaserializable.append(miobj.midic.copy())
        return jsonify(listaserializable)
    except:
        return jsonify({"Mensaje":"Error interno. Llame al Administrador de sistemas (+51) 969 696 969"})
        
@app.route("/api_guardarcriterioprobabilidad", methods=["POST"])
def api_guardarcriterioprobabilidad():
    descripcion = request.json["descripcion"]
    valor = request.json["valor"]
    controlador_criterioprobabilidad.insertar_criterioprobabilidad(descripcion,valor)
    # De cualquier modo, y si todo fue bien, redireccionar
    return jsonify({"Mensaje":"Criterio Probabilidad registrado correctamente"})


#API's CRUD Criterio Probabilidad - Fin

#API's CRUD Criterio Riesgo - Inicio

@app.route("/api_obtenercriteriosriesgo")
def api_obtenercriteriosriesgo():
    try:
        criteriosriesgo = controlador_criterioriesgo.obtener_criterioriesgo()
        listaserializable = []
        for criterioriesgo in criteriosriesgo:
            miobj = clase_criterioriesgo.Criterio_Riesgo(criterioriesgo[0], criterioriesgo[1],criterioriesgo[2],criterioriesgo[3])
            listaserializable.append(miobj.midic.copy())
        return jsonify(listaserializable)
    except:
        return jsonify({"Mensaje":"Error interno. Llame al Administrador de sistemas (+51) 969 696 969"})

@app.route("/api_guardarcriterioriesgo", methods=["POST"])
def api_guardarcriterioriesgo():
    descripcion = request.json["descripcion"]
    valor = request.json["valor"]
    color = request.json["color"]

    controlador_criterioriesgo.insertar_criterioriesgo(descripcion,valor,color)
    # De cualquier modo, y si todo fue bien, redireccionar
    return jsonify({"Mensaje":"Criterio Riesgo registrado correctamente"})

#API's CRUD Criterio Riesgo - Fin

#API's CRUD Registro Impacto Probabilidad - Inicio

@app.route("/api_obtenerregistrosimpactoprobabilidad")
def api_obtenerregistrosimpactoprobabilidad():
    try:
        registrosimpactoprobabilidad = controlador_registroimpactoprobabilidad.obtener_registroimpactoprobabilidad()
        listaserializable = []
        for registroimpactoprobabilidad in registrosimpactoprobabilidad:
            miobj = clase_registroimpactoprobabilidad.Registro_Impacto_Probabilidad(registroimpactoprobabilidad[0], registroimpactoprobabilidad[1],registroimpactoprobabilidad[2],registroimpactoprobabilidad[3],registroimpactoprobabilidad[4],registroimpactoprobabilidad[5])
            listaserializable.append(miobj.midic.copy())
        return jsonify(listaserializable)
    except:
        return jsonify({"Mensaje":"Error interno. Llame al Administrador de sistemas (+51) 969 696 969"})

@app.route("/api_guardarregistroimpactoprobabilidad", methods=["POST"])
def api_guardarregistroimpactoprobabilidad():
    riesgoid = request.json["riesgoid"]
    criterioimpactoid = request.json["criterioimpactoid"]
    criterioprobabilidadid = request.json["criterioprobabilidadid"]
    criterioriesgoid = request.json["criterioriesgoid"]
    uid = request.json["uid"]
    controlador_registroimpactoprobabilidad.insertar_registroimpactoprobabilidad(riesgoid,criterioimpactoid,criterioprobabilidadid,criterioriesgoid,uid)
    # De cualquier modo, y si todo fue bien, redireccionar
    return jsonify({"Mensaje":"Registro Impacto Probabilidad registrado correctamente"})
#API's CRUD Registro Impacto Probabilidad - Fin


# Iniciar el servidor
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)

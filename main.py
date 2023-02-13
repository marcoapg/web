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

#(Vulnerabilidad)
@app.route("/")
@app.route("/vulnerabilidades")
def vulnerabilidades():
    vulnerabilidades = controlador_vulnerabilidad.obtener_vulnerabilidad()
    return render_template("vulnerabilidades.html", vulnerabilidades=vulnerabilidades)

@app.route("/agregar_vulnerabilidad")
def formulario_agregar_vulnerabilidad():
    return render_template("agregar_vulnerabilidad.html")

@app.route("/formulario_editar_vulnerabilidad/<int:id>")
def editar_vulnerabilidad(id):
    # Obtener el juego por ID
    vulnerabilidad = controlador_vulnerabilidad.obtener_vulnerabilidad_por_id(id)
    return render_template("editar_vulnerabilidad.html", vulnerabilidad=vulnerabilidad)

#(Criterio Impacto)
@app.route("/")
@app.route("/criteriosimpacto")
def criteriosimpacto():
    criteriosimpacto = controlador_criterioimpacto.obtener_criterioimpacto()
    return render_template("criteriosimpacto.html", criteriosimpacto=criteriosimpacto)

@app.route("/agregar_criterioimpacto")
def formulario_agregar_criterioimpacto():
    return render_template("agregar_criterioimpacto.html")

@app.route("/formulario_editar_criterioimpacto/<int:id>")
def editar_criterioimpacto(id):
    # Obtener el juego por ID
    criterioimpacto = controlador_criterioimpacto.obtener_criterioimpacto_por_id(id)
    return render_template("editar_criterioimpacto.html", criterioimpacto=criterioimpacto)

#(Criterio Probabilidad)
@app.route("/")
@app.route("/criteriosprobabilidad")
def criteriosprobabilidad():
    criteriosprobabilidad = controlador_criterioprobabilidad.obtener_criterioprobabilidad()
    return render_template("criteriosprobabilidad.html", criteriosprobabilidad=criteriosprobabilidad)

@app.route("/agregar_criterioprobabilidad")
def formulario_agregar_criterioprobabilidad():
    return render_template("agregar_criterioprobabilidad.html")

@app.route("/formulario_editar_criterioprobabilidad/<int:id>")
def editar_criterioprobabilidad(id):
    # Obtener el juego por ID
    criterioprobabilidad = controlador_criterioprobabilidad.obtener_criterioprobabilidad_por_id(id)
    return render_template("editar_criterioprobabilidad.html", criterioprobabilidad=criterioprobabilidad)

#(Criterio Riesgo)
@app.route("/")
@app.route("/criteriosriesgo")
def criteriosriesgo():
    criteriosriesgo = controlador_criterioriesgo.obtener_criterioriesgo()
    return render_template("criteriosriesgo.html", criteriosriesgo=criteriosriesgo)

@app.route("/agregar_criterioriesgo")
def formulario_agregar_criterioriesgo():
    return render_template("agregar_criterioriesgo.html")

@app.route("/formulario_editar_criterioriesgo/<int:id>")
def editar_criterioriesgo(id):
    # Obtener el juego por ID
    criterioriesgo = controlador_criterioriesgo.obtener_criterioriesgo_por_id(id)
    return render_template("editar_criterioriesgo.html", criterioriesgo=criterioriesgo)

#(Amenaza)
@app.route("/")
@app.route("/amenazas")
def amenazas():
    amenazas = controlador_amenaza.obtener_amenaza()
    return render_template("amenazas.html", amenazas=amenazas)

@app.route("/agregar_amenaza")
def formulario_agregar_amenaza():
    return render_template("agregar_amenaza.html")

@app.route("/formulario_editar_amenaza/<int:id>")
def editar_amenaza(id):
    # Obtener el juego por ID
    amenaza = controlador_amenaza.obtener_amenaza_por_id(id)
    return render_template("editar_amenaza.html", amenaza=amenaza)

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

#(Causa)
@app.route("/")
@app.route("/causas")
def causas():
    causas = controlador_causa.obtener_causa()
    return render_template("causas.html", causas=causas)

@app.route("/agregar_causa")
def formulario_agregar_causa():
    return render_template("agregar_causa.html")

@app.route("/formulario_editar_causa/<int:id>")
def editar_causa(id):
    # Obtener el juego por ID
    causa = controlador_causa.obtener_causa_por_id(id)
    return render_template("editar_causa.html", causa=causa)

#(Riesgo)
@app.route("/")
@app.route("/riesgos")
def riesgos():
    riesgos = controlador_riesgo.obtener_riego()
    return render_template("riesgos.html", riesgos=riesgos)

@app.route("/agregar_riesgo")
def formulario_agregar_riesgo():
    return render_template("agregar_riesgo.html")

@app.route("/formulario_editar_riesgo/<int:id>")
def editar_riesgo(id):
    # Obtener el juego por ID
    riesgo = controlador_riesgo.obtener_riesgo_por_id(id)
    return render_template("editar_riesgo.html", riesgo=riesgo)

#(Registro Impacto)
@app.route("/")
@app.route("/registrosimpactoprobabilidad")
def registrosimpactoprobabilidad():
    registrosimpactoprobabilidad = controlador_registroimpactoprobabilidad.obtener_registroimpactoprobabilidad()
    return render_template("registrosimpactoprobabilidad.html", registrosimpactoprobabilidad=registrosimpactoprobabilidad)

@app.route("/agregar_registroimpactoprobabilidad")
def formulario_agregar_registroimpactoprobabilidad():
    return render_template("agregar_registroimpactoprobabilidad.html")

@app.route("/formulario_editar_registroimpactoprobabilidad/<int:id>")
def editar_registroimpactoprobabilidad(id):
    # Obtener el juego por ID
    registroimpactoprobabilidad = controlador_registroimpactoprobabilidad.obtener_registroimpactoprobabilidad(id)
    return render_template("editar_registroimpactoprobabilidad.html", registroimpactoprobabilidad=registroimpactoprobabilidad)

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

#(Criterio Impacto)
@app.route("/guardar_criterioimpacto", methods=["POST"])
def guardar_criterioimpacto():
    descripcion = request.form["descripcion"]
    valor = request.form["valor"]

    controlador_criterioimpacto.insertar_criterioimpacto(descripcion,valor)
    # De cualquier modo, y si todo fue bien, redireccionar
    return redirect("/criteriosimpacto")

@app.route("/actualizar_criterioimpacto", methods=["POST"])
def actualizar_criterioimpacto():
    id = request.form["id"]
    descripcion = request.form["descripcion"]
    valor = request.form["valor"]

    controlador_criterioimpacto.actualizar_criterioimpacto(descripcion,valor, id)
    return redirect("/criteriosimpacto")

@app.route("/eliminar_criterioimpacto", methods=["POST"])
def eliminar_criterioimpacto():
    controlador_criterioimpacto.eliminar_criterioimpacto(request.form["id"])
    return redirect("/criteriosimpacto")

#(Criterio Probabilidad)
@app.route("/guardar_criterioprobabilidad", methods=["POST"])
def guardar_criterioprobabilidad():
    descripcion = request.form["descripcion"]
    valor = request.form["valor"]

    controlador_criterioprobabilidad.insertar_criterioprobabilidad(descripcion,valor)
    # De cualquier modo, y si todo fue bien, redireccionar
    return redirect("/criteriosprobabilidad")

@app.route("/actualizar_criterioprobabilidad", methods=["POST"])
def actualizar_criterioprobabilidad():
    id = request.form["id"]
    descripcion = request.form["descripcion"]
    valor = request.form["valor"]

    controlador_criterioprobabilidad.actualizar_criterioprobabilidad(descripcion,valor, id)
    return redirect("/criteriosprobabilidad")

@app.route("/eliminar_criterioprobabilidad", methods=["POST"])
def eliminar_criterioprobabilidad():
    controlador_criterioprobabilidad.eliminar_criterioprobabilidad(request.form["id"])
    return redirect("/criteriosprobabilidad")    

#(Criterio Riesgo)
@app.route("/guardar_criterioriesgo", methods=["POST"])
def guardar_criterioriesgo():
    descripcion = request.form["descripcion"]
    valor = request.form["valor"]
    color = request.form["color"]

    controlador_criterioriesgo.insertar_criterioriesgo(descripcion,valor,color)
    # De cualquier modo, y si todo fue bien, redireccionar
    return redirect("/criteriosriesgo")

@app.route("/actualizar_criterioriesgo", methods=["POST"])
def actualizar_criterioriesgo():
    id = request.form["id"]
    descripcion = request.form["descripcion"]
    valor = request.form["valor"]
    color = request.form["color"]

    controlador_criterioriesgo.actualizar_criterioriesgo(descripcion,valor,color, id)
    return redirect("/criteriosriesgo")

@app.route("/eliminar_criterioriesgo", methods=["POST"])
def eliminar_criterioriesgo():
    controlador_criterioriesgo.eliminar_criterioriesgo(request.form["id"])
    return redirect("/criteriosriesgo")        

#(Vulnerabilidad)
@app.route("/guardar_vulnerabilidad", methods=["POST"])
def guardar_vulnerabilidad():
    descripcion = request.form["descripcion"]
    controlador_vulnerabilidad.insertar_vulnerabilidad(descripcion)
    # De cualquier modo, y si todo fue bien, redireccionar
    return redirect("/vulnerabilidades")

@app.route("/actualizar_vulnerabilidad", methods=["POST"])
def actualizar_vulnerabilidad():
    id = request.form["id"]
    descripcion = request.form["descripcion"]
    controlador_vulnerabilidad.actualizar_vulnerabilidad(descripcion, id)
    return redirect("/vulnerabilidades")

@app.route("/eliminar_vulnerabilidad", methods=["POST"])
def eliminar_vulnerabilidad():
    controlador_vulnerabilidad.eliminar_vulnerabilidad(request.form["id"])
    return redirect("/vulnerabilidades")

#(Amenaza)
@app.route("/guardar_amenaza", methods=["POST"])
def guardar_amenaza():
    descripcion = request.form["descripcion"]
    controlador_amenaza.insertar_amenaza(descripcion)
    # De cualquier modo, y si todo fue bien, redireccionar
    return redirect("/amenazas")

@app.route("/actualizar_amenaza", methods=["POST"])
def actualizar_amenaza():
    id = request.form["id"]
    descripcion = request.form["descripcion"]
    controlador_amenaza.actualizar_amenaza(descripcion, id)
    return redirect("/amenazas")

@app.route("/eliminar_amenaza", methods=["POST"])
def eliminar_amenaza():
    controlador_amenaza.eliminar_amenaza(request.form["id"])
    return redirect("/amenazas")

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

#(Causa)
@app.route("/guardar_causa", methods=["POST"])
def guardar_causa():
    riesgoid = request.form["riesgoid"]  
    descripcion = request.form["descripcion"]

    controlador_causa.insertar_causa(riesgoid,descripcion)
    # De cualquier modo, y si todo fue bien, redireccionar
    return redirect("/causas")

@app.route("/actualizar_causa", methods=["POST"])
def actualizar_causa():
    id = request.form["id"]
    riesgoid = request.form["riesgoid"]  
    descripcion = request.form["descripcion"]

    controlador_causa.actualizar_causa(riesgoid,descripcion,id)
    return redirect("/causas")

@app.route("/eliminar_causa", methods=["POST"])
def eliminar_causa():
    controlador_causa.eliminar_causa(request.form["id"])
    return redirect("/causas")

#(Riesgo)
@app.route("/guardar_riesgo", methods=["POST"])
def guardar_riesgo():
    descripcion = request.form["descripcion"]
    activoid = request.form["activoid"]
    vulnerabilidadid = request.form["vulnerabilidadid"]
    amenazaid = request.form["amenazaid"]
    controlador_riesgo.insertar_riesgo(descripcion,activoid,vulnerabilidadid,amenazaid)
    # De cualquier modo, y si todo fue bien, redireccionar
    return redirect("/riesgos")

@app.route("/actualizar_riesgo", methods=["POST"])
def actualizar_riesgo():
    id = request.form["id"]
    descripcion = request.form["descripcion"]
    activoid = request.form["activoid"]
    vulnerabilidadid = request.form["vulnerabilidadid"]
    amenazaid = request.form["amenazaid"]

    controlador_riesgo.actualizar_riesgo(descripcion,activoid,vulnerabilidadid,amenazaid,id)
    return redirect("/riesgos")

@app.route("/eliminar_riesgo", methods=["POST"])
def eliminar_riesgo():
    controlador_riesgo.eliminar_riesgo(request.form["id"])
    return redirect("/riesgos")

#(Registro Impacto Probabilidad)
@app.route("/guardar_registroimpactoprobabilidad", methods=["POST"])
def guardar_registroimpactoprobabilidad():
    riesgoid = request.form["riesgoid"]
    criterioimpactoid = request.form["criterioimpactoid"]
    criterioprobabilidadid = request.form["criterioprobabilidadid"]
    criterioriesgoid = request.form["criterioriesgoid"]
    uid = request.form["uid"]
    controlador_registroimpactoprobabilidad.insertar_registroimpactoprobabilidad(riesgoid,criterioimpactoid,criterioprobabilidadid,criterioriesgoid,uid)
    # De cualquier modo, y si todo fue bien, redireccionar
    return redirect("/registrosimpactoprobabilidad")

@app.route("/actualizar_registroimpactoprobabilidad", methods=["POST"])
def actualizar_registroimpactoprobabilidad():
    id = request.form["id"]
    riesgoid = request.form["riesgoid"]
    criterioimpactoid = request.form["criterioimpactoid"]
    criterioprobabilidadid = request.form["criterioprobabilidadid"]
    criterioriesgoid = request.form["criterioriesgoid"]
    uid = request.form["uid"]

    controlador_riesgo.actualizar_riesgo(riesgoid,criterioimpactoid,criterioprobabilidadid,criterioriesgoid,uid,id)
    return redirect("/registrosimpactoprobabilidad")

@app.route("/eliminar_registroimpactoprobabilidad", methods=["POST"])
def eliminar_registroimpactoprobabilidad():
    controlador_registroimpactoprobabilidad.eliminar_registroimpactoprobabilidad(request.form["id"])
    return redirect("/registrosimpactoprobabilidad")

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

@app.route("/api_actualizarunidadorganizacional", methods=["POST"])
def api_actualizarunidadorganizacional():
    id = request.json["id"]
    descripcion = request.json["descripcion"]
    controlador_unidadorganizacional.actualizar_unidadorganizacional(descripcion, id)
    return jsonify({"Mensaje":"Unidad Organizacional actualizada correctamente"})

@app.route("/api_eliminarunidadorganizacional", methods=["POST"])
def api_eliminarunidadorganizacional():
    controlador_unidadorganizacional.eliminar_unidadorganizacional(request.json["id"])
    return jsonify({"Mensaje":"Unidad Organizacional eliminada correctamente"})

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

@app.route("/api_actualizartipoactivo", methods=["POST"])
def api_actualizartipoactivo():
    id = request.json["id"]
    descripcion = request.json["descripcion"]
    controlador_tipoactivo.actualizar_tipoactivo(descripcion, id)
    return jsonify({"Mensaje":"Tipo Activo actualizado correctamente"})

@app.route("/api_eliminartipoactivo", methods=["POST"])
def api_eliminartipoactivo():
    controlador_tipoactivo.eliminar_tipoactivo(request.json["id"])
    return jsonify({"Mensaje":"Tipo Activo eliminado correctamente"})

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

@app.route("/api_actualizaramenaza", methods=["POST"])
def api_actualizaramenaza():
    id = request.jsosn["id"]
    descripcion = request.json["descripcion"]
    controlador_amenaza.actualizar_amenaza(descripcion, id)
    return jsonify({"Mensaje":"Amenaza actualizada correctamente"})

@app.route("/api_eliminaramenaza", methods=["POST"])
def api_eliminaramenaza():
    controlador_amenaza.eliminar_amenaza(request.json["id"])
    return jsonify({"Mensaje":"Amenaza eliminada correctamente"})

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

@app.route("/api_actualizarvulnerabilidad", methods=["POST"])
def api_actualizarvulnerabilidad():
    id = request.json["id"]
    descripcion = request.json["descripcion"]
    controlador_vulnerabilidad.actualizar_vulnerabilidad(descripcion, id)
    return jsonify({"Mensaje":"Vulnerabilidad actualizada correctamente"})

@app.route("/api_eliminarvulnerabilidad", methods=["POST"])
def api_eliminarvulnerabilidad():
    controlador_vulnerabilidad.eliminar_vulnerabilidad(request.json["id"])
    return jsonify({"Mensaje":"Vulnerabilidad eliminada correctamente"})

#API's CRUD Vulnerabilidad - Fin

#API's CRUD Activo - Inicio

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


@app.route("/api_actualizaractivo", methods=["POST"])
def api_actualizaractivo():
    id = request.json["id"]
    descripcion = request.json["descripcion"]
    tipoactivoid = request.json["tipoactivoid"]
    unidadorganizacionalid = request.json["unidadorganizacionalid"]

    controlador_activo.actualizar_activo(descripcion,tipoactivoid,unidadorganizacionalid,id)
    return jsonify({"Mensaje":"Activo actualizado correctamente"})

@app.route("/api_eliminaractivo", methods=["POST"])
def api_eliminaractivo():
    controlador_activo.eliminar_activo(request.json["id"])
    return jsonify({"Mensaje":"Activo eliminado correctamente"})

#API's CRUD Activo - Fin

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

@app.route("/api_actualizarriesgo", methods=["POST"])
def api_actualizarriesgo():
    id = request.json["id"]
    descripcion = request.json["descripcion"]
    activoid = request.json["activoid"]
    vulnerabilidadid = request.json["vulnerabilidadid"]
    amenazaid = request.json["amenazaid"]

    controlador_riesgo.actualizar_riesgo(descripcion,activoid,vulnerabilidadid,amenazaid,id)
    return jsonify({"Mensaje":"Riesgo actualizado correctamente"})

@app.route("/api_eliminarriesgo", methods=["POST"])
def api_eliminarriesgo():
    controlador_riesgo.eliminar_riesgo(request.json["id"])
    return jsonify({"Mensaje":"Riesgo eliminado correctamente"})

#API's CRUD Riesgo - Fin

#API's CRUD Causa - Inicio

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


@app.route("/api_actualizarcausa", methods=["POST"])
def api_actualizarcausa():
    id = request.json["id"]
    riesgoid = request.json["riesgoid"]  
    descripcion = request.json["descripcion"]

    controlador_causa.actualizar_causa(riesgoid,descripcion,id)
    return jsonify({"Mensaje":"Causa actualizada correctamente"})

@app.route("/api_eliminarcausa", methods=["POST"])
def api_eliminarcausa():
    controlador_causa.eliminar_causa(request.json["id"])
    return jsonify({"Mensaje":"Causa eliminada correctamente"})

#API's CRUD Causa - Fin

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


@app.route("/api_actualizarcriterioimpacto", methods=["POST"])
def api_actualizarcriterioimpacto():
    id = request.json["id"]
    descripcion = request.json["descripcion"]
    valor = request.json["valor"]

    controlador_criterioimpacto.actualizar_criterioimpacto(descripcion,valor, id)
    return jsonify({"Mensaje":"Criterio Impacto actualizado correctamente"})

@app.route("/api_eliminarcriterioimpacto", methods=["POST"])
def api_eliminarcriterioimpacto():
    controlador_criterioimpacto.eliminar_criterioimpacto(request.json["id"])
    return jsonify({"Mensaje":"Criterio Impacto eliminado correctamente"})

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

@app.route("/api_actualizarcriterioprobabilidad", methods=["POST"])
def api_actualizarcriterioprobabilidad():
    id = request.json["id"]
    descripcion = request.json["descripcion"]
    valor = request.json["valor"]

    controlador_criterioprobabilidad.actualizar_criterioprobabilidad(descripcion,valor, id)
    return jsonify({"Mensaje":"Criterio Probabilidad actualizado correctamente"})

@app.route("/api_eliminarcriterioprobabilidad", methods=["POST"])
def api_eliminarcriterioprobabilidad():
    controlador_criterioprobabilidad.eliminar_criterioprobabilidad(request.json["id"])
    return jsonify({"Mensaje":"Criterio Probabilidad eliminado correctamente"})


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

@app.route("/api_actualizarcriterioriesgo", methods=["POST"])
def api_actualizarcriterioriesgo():
    id = request.json["id"]
    descripcion = request.json["descripcion"]
    valor = request.json["valor"]
    color = request.json["color"]

    controlador_criterioriesgo.actualizar_criterioriesgo(descripcion,valor,color, id)
    return jsonify({"Mensaje":"Criterio Riesgo actualizado correctamente"})

@app.route("/api_eliminarcriterioriesgo", methods=["POST"])
def api_eliminarcriterioriesgo():
    controlador_criterioriesgo.eliminar_criterioriesgo(request.json["id"])
    return jsonify({"Mensaje":"Criterio Riesgo eliminado correctamente"})

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

@app.route("/api_actualizarregistroimpactoprobabilidad", methods=["POST"])
def api_actualizarregistroimpactoprobabilidad():
    id = request.form["id"]
    riesgoid = request.form["riesgoid"]
    criterioimpactoid = request.form["criterioimpactoid"]
    criterioprobabilidadid = request.form["criterioprobabilidadid"]
    criterioriesgoid = request.form["criterioriesgoid"]
    uid = request.form["uid"]

    controlador_riesgo.actualizar_riesgo(riesgoid,criterioimpactoid,criterioprobabilidadid,criterioriesgoid,uid,id)
    return jsonify({"Mensaje":"Registro Impacto Probabilidad actualizado correctamente"})

@app.route("/api_eliminarregistroimpactoprobabilidad", methods=["POST"])
def api_eliminarregistroimpactoprobabilidad():
    controlador_registroimpactoprobabilidad.eliminar_registroimpactoprobabilidad(request.form["id"])
    return jsonify({"Mensaje":"Registro Impacto Probabilidad eliminado correctamente"})

#API's CRUD Registro Impacto Probabilidad - Fin


# Iniciar el servidor
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)

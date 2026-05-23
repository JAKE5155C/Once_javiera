import os
from flask import Flask, render_template, request, redirect, url_for

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, "templates"),
    static_folder=os.path.join(BASE_DIR, "static"),
)

# Contraseña correcta
CLAVE_CORRECTA = "1234"

# ── Ruta raíz → muestra el formulario (index.html) ──
@app.route("/")
def inicio():
    return render_template("index.html")

# ── Ruta que captura el formulario ──
@app.route("/captura", methods=["POST"])
def captura():
    usuario    = request.form["usuario"]
    contrasena = request.form["contrasena"]

    if contrasena == CLAVE_CORRECTA:
        # Correcto → redirige a sesion1.html
        return redirect(url_for("bienvenida", nombre=usuario))
    else:
        # Incorrecto → regresa a la raíz
        return redirect(url_for("inicio"))

# ── Ruta bienvenida → muestra sesion1.html ──
@app.route("/bienvenida")
def bienvenida():
    nombre = request.args.get("nombre", "Estudiante")
    return render_template("sesion1.html", nombre=nombre)


if __name__ == "__main__":
    app.run(debug=True)

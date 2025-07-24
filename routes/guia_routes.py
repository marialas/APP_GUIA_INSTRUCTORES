import os
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from models.guia import GuiaAprendizaje, PROGRAMAS
from werkzeug.utils import secure_filename

guia_bp = Blueprint("guia_bp", __name__)

UPLOAD_FOLDER = "static/uploads"
ALLOWED_EXTENSIONS = {"pdf"}
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@guia_bp.route("/subir", methods=["GET", "POST"])
@login_required
def subir_guia():
    if request.method == "POST":
        nombre = request.form["nombre"]
        descripcion = request.form["descripcion"]
        programa = request.form["programa"]
        archivo = request.files["archivo_pdf"]

        if not archivo or not allowed_file(archivo.filename):
            flash("Debes subir un archivo PDF válido", "danger")
            return redirect(request.url)

        filename = secure_filename(archivo.filename)
        archivo.save(os.path.join(UPLOAD_FOLDER, filename))

        guia = GuiaAprendizaje(
            nombre=nombre,
            descripcion=descripcion,
            programa=programa,
            archivo_pdf=filename,
            instructor=current_user._get_current_object()
        )
        guia.save()

        flash("Guía subida exitosamente", "success")
        return redirect(url_for("guia_bp.subir_guia"))

    return render_template("subir_guia.html", programas=PROGRAMAS)

@guia_bp.route("/listar")
@login_required
def listar_guias():
    guias = GuiaAprendizaje.objects().order_by("-fecha_subida")
    return render_template("listar_guias.html", guias=guias)

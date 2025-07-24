from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required
from models.instructor import Instructor, REGIONALES
from utils.email_sender import enviar_correo_credenciales

auth_bp = Blueprint("auth_bp", __name__,)


@auth_bp.route("/")
def home():
    return redirect(url_for("auth_bp.login"))


@auth_bp.route("/registro", methods=["GET", "POST"])
def registro():
    if request.method == "POST":
        nombre = request.form["nombre"]
        correo = request.form["correo"]
        regional = request.form["regional"]
        password = request.form["password"]

        if Instructor.objects(correo=correo):
            flash("Este correo ya está registrado", "danger")
            return redirect(url_for("auth_bp.registro"))

        instructor = Instructor(
            nombre_completo=nombre,
            correo=correo,
            regional=regional
        )
        instructor.set_password(password)
        instructor.save()

        enviar_correo_credenciales(correo, nombre, correo, password)

        flash("Registro exitoso. Se enviaron tus credenciales al correo.", "success")
        return redirect(url_for("auth_bp.login"))

    return render_template("registro.html", regionales=REGIONALES)

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        correo = request.form["correo"]
        password = request.form["password"]

        usuario = Instructor.objects(correo=correo).first()
        if usuario and usuario.check_password(password):
            login_user(usuario)
            return redirect(url_for("guia_bp.subir_guia"))
        else:
            flash("Credenciales inválidas", "danger")

    return render_template("login.html")

@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth_bp.login"))



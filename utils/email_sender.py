from flask_mail import Message

def enviar_correo_credenciales(destinatario, nombre, usuario, clave):
    # Importamos solo dentro de la función
    from app import app, mail

    with app.app_context():
        mensaje = Message(
            subject="Credenciales de acceso - Plataforma Instructores SENA",
            sender=app.config['MAIL_USERNAME'],
            recipients=[destinatario]
        )
        mensaje.body = f"""Hola {nombre},

Tus credenciales de acceso son:
Usuario: {usuario}
Contraseña: {clave}

Enlace: https://aplicacion-flask-mongo.onrender.com

Equipo Plataforma SENA
"""
        mail.send(mensaje)

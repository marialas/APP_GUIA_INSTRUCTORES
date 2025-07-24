from flask import Flask
from flask_login import LoginManager
from flask_mail import Mail
from mongoengine import connect
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

connect(**app.config["MONGODB_SETTINGS"])

mail = Mail(app)
login_manager = LoginManager(app)
login_manager.login_view = "auth_bp.login"

from models.instructor import Instructor
@login_manager.user_loader
def load_user(user_id):
    return Instructor.objects(id=user_id).first()

from routes.auth_routes import auth_bp
from routes.guia_routes import guia_bp

app.register_blueprint(auth_bp)
app.register_blueprint(guia_bp)

if __name__ == "__main__":
    app.run(debug=True)


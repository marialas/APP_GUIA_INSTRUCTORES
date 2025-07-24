from mongoengine import Document, StringField
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

REGIONALES = ["Cauca", "Huila", "Antioquia", "Valle", "Nariño"]

class Instructor(UserMixin, Document):
    nombre_completo = StringField(required=True)
    correo = StringField(required=True, unique=True)
    regional = StringField(required=True, choices=REGIONALES)
    password_hash = StringField(required=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def get_id(self):
        return str(self.id)

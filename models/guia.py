from mongoengine import Document, StringField, DateTimeField, ReferenceField
from datetime import datetime
from models.instructor import Instructor

PROGRAMAS = [
    "Desarrollo de Software",
    "Multimedia",
    "Inteligencia Artificial",
    "Analítica de Datos",
    "Construcción",
    "Contabilidad"
]

class GuiaAprendizaje(Document):
    nombre = StringField(required=True)
    descripcion = StringField(required=True)
    programa = StringField(required=True, choices=PROGRAMAS)
    archivo_pdf = StringField(required=True)
    fecha_subida = DateTimeField(default=datetime.utcnow)
    instructor = ReferenceField(Instructor, required=True)

# APP Guía Instructores SENA — Flask + MongoDB + Login + Mail

Proyecto académico de **Anyeli Mariana Cabezas Salamanca** ([@marialas](https://github.com/marialas)) — Tecnóloga ADSO SENA.

Gestión de guías de aprendizaje e instructores con login (Flask-Login), recuperación por correo (Flask-Mail) y MongoDB.

Video demo original: https://drive.google.com/file/d/1ckocqm2fTYUssX8S1dFsdEShNWQFCS5C/view?usp=sharing

## Stack
Python 3.10+, Flask, Flask-Login, Flask-Mail, MongoEngine, Flask-WTF, gunicorn.

## Estructura
```
app.py → app + login_manager + mail + blueprints
config.py → Config por .env (SECRET_KEY, DB_NAME, DB_URI, MAIL_*)
models/instructor.py
routes/auth_routes.py → login/registro/recuperación
routes/guia_routes.py → CRUD guías
templates/ + static/
Procfile → deploy (Render/Railway)
```

## Instalación
```bash
python -m venv venv
# Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
# completa SECRET_KEY, DB_NAME, DB_URI, MAIL_USERNAME, MAIL_PASSWORD
python app.py
```
Abre http://127.0.0.1:5000

## Deploy
```bash
gunicorn app:app
```

## Autora
Tuluá, Colombia — abierta a remoto / Popayán. cabezasmari477@gmail.com

<<<<<<< HEAD
from fastapi import FastAPI, HTTPException
from typing import List
from model import UsuarioCreate, UsuarioResponse  # Importa los modelos de Pydantic
from pool import get_db_connection  # Importa la función para obtener la conexión a la base de datos
from pydantic import BaseModel

app = FastAPI()

# Funciones para interactuar con la base de datos
def create_usuario(usuario: UsuarioCreate):
    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
=======
from fastapi import FastAPI, HTTPException, Form, UploadFile, File
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from typing import List
from pydantic import BaseModel
from model import UsuarioCreate, UsuarioResponse
from pool import get_db_connection
import qrcode
from io import BytesIO
import base64
import os
from datetime import datetime
import shutil
import cv2
from ultralytics import YOLO
import socket

app = FastAPI()

# ────────────── Carpetas ──────────────
UPLOAD_DIR = "uploads"
RESULTS_DIR = "results"
DIST_PYTHON_DIR = "dist-python"

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(RESULTS_DIR, exist_ok=True)
os.makedirs(DIST_PYTHON_DIR, exist_ok=True)

# Montar dist-python como carpeta estática
app.mount("/dist", StaticFiles(directory=DIST_PYTHON_DIR), name="dist")

# Cargar modelo YOLO
model = YOLO("best.pt")

# ────────────── Funciones de DB ──────────────
def create_usuario(usuario: UsuarioCreate):
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
>>>>>>> e6a0384 (funcionando el back pero no el qr para coneccion celular)
        query = """
        INSERT INTO usuarios (rol, tipo_documento, documento, password)
        VALUES (%s, %s, %s, %s)
        """
        cursor.execute(query, (usuario.rol, usuario.tipo_documento, usuario.documento, usuario.password))
<<<<<<< HEAD
        connection.commit()
        cursor.close()
        connection.close()
        return {"msg": "Usuario creado exitosamente"}

=======
        conn.commit()
        cursor.close()
        conn.close()
        return {"msg": "Usuario creado exitosamente"}
>>>>>>> e6a0384 (funcionando el back pero no el qr para coneccion celular)
    except Exception as e:
        print(f"Error al crear usuario: {e}")
        raise HTTPException(status_code=500, detail="Error al crear usuario")

def get_usuarios() -> List[UsuarioResponse]:
    try:
<<<<<<< HEAD
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)

        query = "SELECT * FROM usuarios"
        cursor.execute(query)
        rows = cursor.fetchall()

        usuarios = [UsuarioResponse(**row) for row in rows]
        cursor.close()
        connection.close()

        return usuarios

=======
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM usuarios")
        rows = cursor.fetchall()
        usuarios = [UsuarioResponse(**row) for row in rows]
        cursor.close()
        conn.close()
        return usuarios
>>>>>>> e6a0384 (funcionando el back pero no el qr para coneccion celular)
    except Exception as e:
        print(f"Error al obtener usuarios: {e}")
        raise HTTPException(status_code=500, detail="Error al obtener usuarios")

<<<<<<< HEAD

# Rutas de la API
=======
# ────────────── Rutas Usuarios ──────────────
>>>>>>> e6a0384 (funcionando el back pero no el qr para coneccion celular)
@app.post("/usuarios/", response_model=dict)
def create_usuario_view(usuario: UsuarioCreate):
    return create_usuario(usuario)

@app.get("/usuarios/", response_model=List[UsuarioResponse])
def get_usuarios_view():
    return get_usuarios()

<<<<<<< HEAD
from pydantic import BaseModel

=======
>>>>>>> e6a0384 (funcionando el back pero no el qr para coneccion celular)
class LoginRequest(BaseModel):
    documento: str
    password: str

@app.post("/login/")
def login(request: LoginRequest):
<<<<<<< HEAD
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    query = "SELECT * FROM usuarios WHERE documento = %s AND password = %s"
    cursor.execute(query, (request.documento, request.password))
    user = cursor.fetchone()

    cursor.close()
    connection.close()

    if not user:
        raise HTTPException(status_code=401, detail="Credenciales incorrectas")

    return {"msg": "Login exitoso", "usuario": user}
=======
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    query = "SELECT * FROM usuarios WHERE documento = %s AND password = %s"
    cursor.execute(query, (request.documento, request.password))
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    if not user:
        raise HTTPException(status_code=401, detail="Credenciales incorrectas")
    return {"msg": "Login exitoso", "usuario": user}

# ────────────── Funciones auxiliares ──────────────
def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
    except Exception:
        ip = "127.0.0.1"
    finally:
        s.close()
    return ip

# ────────────── Rutas QR y Web ──────────────
@app.get("/", response_class=HTMLResponse)
def read_root():
    local_ip = get_local_ip()
    url = f"http://{local_ip}:8000/connect"

    # Generar QR
    img = qrcode.make(url)
    img_byte_arr = BytesIO()
    img.save(img_byte_arr)
    qr_base64 = base64.b64encode(img_byte_arr.getvalue()).decode("utf-8")

    html_content = f"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Conectar a la WebApp</title>
    </head>
    <body>
        <h1>Escanea el QR para conectarte</h1>
        <img src="data:image/png;base64,{qr_base64}" alt="QR Code">
        <p>O entra manualmente: <b>{url}</b></p>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)

@app.get("/connect", response_class=HTMLResponse)
def connect():
    index_path = os.path.join(DIST_PYTHON_DIR, "index.html")
    if os.path.exists(index_path):
        with open(index_path, "r", encoding="utf-8") as f:
            return HTMLResponse(f.read())
    return HTMLResponse("<h1>No hay index.html en dist-python</h1>")

# ────────────── Upload / YOLO ──────────────
@app.post("/upload_photo")
def upload_photo(file: UploadFile = File(...)):
    filename = datetime.now().strftime("%Y%m%d_%H%M%S") + "_" + file.filename
    file_path = os.path.join(UPLOAD_DIR, filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    print(f"📸 Foto recibida y guardada en {file_path}")

    results = model(file_path)
    annotated_frame = results[0].plot()

    result_filename = "result_" + filename
    result_path = os.path.join(RESULTS_DIR, result_filename)
    cv2.imwrite(result_path, annotated_frame)
    print(f"✅ Resultado procesado y guardado en {result_path}")

    return {"message": "Foto subida y procesada con éxito", "filename": filename, "result": result_filename}

# ────────────── Recibir datos simples ──────────────
@app.post("/send_data")
def receive_data(data: str = Form(...)):
    print(f"📲 Datos recibidos: {data}")
    return {"message": f"Datos recibidos: {data}"}
>>>>>>> e6a0384 (funcionando el back pero no el qr para coneccion celular)

#!/usr/bin/env python3
"""
Script para ejecutar SOLO el backend desde el directorio Backend
<<<<<<< HEAD
=======
Puede recibir el puerto por:
  1) variable de entorno FASTAPI_PORT
  2) variable de entorno PORT
  3) argumento en la línea de comandos (argv[1])
  4) fallback 8081
>>>>>>> e6a0384 (funcionando el back pero no el qr para coneccion celular)
"""
import os
import sys

<<<<<<< HEAD
# Asegurar que estamos en el directorio correcto
if not os.path.exists('app'):
    print("❌ Error: Ejecutar desde el directorio Backend")
    sys.exit(1)

print("🚀 Iniciando Backend FastAPI...")
print("📍 URL: http://localhost:8081")
print("📚 Docs: http://localhost:8081/docs")
print("=" * 50)

# Importar y ejecutar
try:
    from app.main import app
    import uvicorn
    
    uvicorn.run(
        app, 
        host="localhost", 
        port=8081,
=======
def get_port():
    # Prioridad: FASTAPI_PORT, PORT, argv[1], 8081
    port_env = os.environ.get("FASTAPI_PORT") or os.environ.get("PORT")
    if port_env:
        try:
            return int(port_env)
        except ValueError:
            print(f"⚠️  Valor de puerto inválido en variable de entorno: {port_env}")
    if len(sys.argv) > 1:
        try:
            return int(sys.argv[1])
        except ValueError:
            print(f"⚠️  Valor de puerto inválido en argumento: {sys.argv[1]}")
    return 8081

FASTAPI_PORT = get_port()

# Asegurar que estamos en el directorio correcto
if not os.path.exists('app'):
    print("❌ Error: Ejecutar desde el directorio Backend (debe existir la carpeta 'app')")
    sys.exit(1)

print(" Iniciando Backend FastAPI...")
print(f" URL (local): http://127.0.0.1:{FASTAPI_PORT}")
print(f" URL (red local): http://0.0.0.0:{FASTAPI_PORT}")
print(f" Docs: http://127.0.0.1:{FASTAPI_PORT}/docs")
print("=" * 50)

try:
    from app.main import app
    import uvicorn

    uvicorn.run(
        app,
        host="0.0.0.0",
        port=FASTAPI_PORT,
>>>>>>> e6a0384 (funcionando el back pero no el qr para coneccion celular)
        reload=False,
        log_level="info"
    )
except KeyboardInterrupt:
    print("\n🛑 Servidor detenido por el usuario")
except Exception as e:
    print(f"❌ Error: {e}")
    input("Presiona Enter para salir...")

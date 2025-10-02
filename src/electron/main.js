import { app, BrowserWindow, nativeImage } from "electron";
import path from "path";
import { fileURLToPath } from "url";
<<<<<<< HEAD

// reconstruir __dirname en ESM
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const iconPath = path.join(__dirname, '..', '..', 'App de inventario', '../logo.png');
app.on("ready", () => {
  const mainWindow = new BrowserWindow({
    fullscreen: true,
    icon: iconPath,
    webPreferences: {
      nodeIntegration: true,
      contextIsolation: false
    }
  });

  mainWindow.setOverlayIcon(
    nativeImage.createFromPath(path.join(app.getAppPath(), "../logo.png")),
    "App de inventario"
  );

   mainWindow.loadFile( path.join(app.getAppPath(), "dist-react/index.html") );
=======
import { spawn } from "child_process";
import os from "os";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const FASTAPI_PORT = process.env.FASTAPI_PORT || 8081;

function getLocalIPs() {
  const nets = os.networkInterfaces();
  const results = [];
  for (const name of Object.keys(nets)) {
    for (const net of nets[name]) {
      if (net.family === "IPv4" && !net.internal) {
        results.push(net.address);
      }
    }
  }
  return results;
}

let backend = null;
let mainWindow = null;

app.whenReady().then(() => {
  mainWindow = new BrowserWindow({
    fullscreen: true,
    icon: path.join(__dirname, "../logo.png"),
    webPreferences: {
      contextIsolation: true,
      nodeIntegration: false,
    },
  });

  const reactIndex = path.join(app.getAppPath(), "dist-react/index.html");
  mainWindow.loadFile(reactIndex);

  mainWindow.setOverlayIcon(
    nativeImage.createFromPath(path.join(__dirname, "../logo.png")),
    "App de inventario"
  );

  // 🔹 Ejecutar backend
  const venvPython =
    process.platform === "win32"
      ? path.join(__dirname, "../../backend/.venv/Scripts/python.exe")
      : path.join(__dirname, "../../backend/.venv/bin/python");

  backend = spawn(venvPython, ["run_backend.py"], {
    cwd: path.join(__dirname, "../../backend"),
  });

  backend.stdout.on("data", (data) => {
    console.log(`FastAPI: ${data}`);
  });

  backend.stderr.on("data", (data) => {
    console.error(`FastAPI error: ${data}`);
  });

  backend.on("close", (code) => {
    console.log(`FastAPI finalizó con código ${code}`);
  });

  // 🔹 Inyectar variable global solo si no existe
  mainWindow.webContents.on("did-finish-load", () => {
    const ips = getLocalIPs();
    const data = { ips, port: FASTAPI_PORT };
    console.log("📡 Enviando datos a la ventana:", data);

    mainWindow.webContents.executeJavaScript(`
      if (!window.fastapiInfo) {
        window.fastapiInfo = ${JSON.stringify(data)};
        console.log("⚡ fastapiInfo inyectado:", window.fastapiInfo);
      }
    `);
  });
});

// 🔹 Matar backend al cerrar
app.on("before-quit", () => {
  if (backend) {
    backend.kill("SIGTERM");
    console.log("🛑 Backend detenido al cerrar Electron");
  }
>>>>>>> e6a0384 (funcionando el back pero no el qr para coneccion celular)
});

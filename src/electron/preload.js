import { contextBridge, ipcRenderer } from "electron";

console.log("⚡ preload cargado");

contextBridge.exposeInMainWorld("electronAPI", {
  onFastapiInfo: (callback) => {
    ipcRenderer.on("fastapi-info", (_event, data) => {
      console.log("📡 preload recibió:", data);
      callback(data);
    });
  },
});

<<<<<<< HEAD
=======
import React, { useState, useEffect } from "react";
import QRCode from "react-qr-code";
>>>>>>> e6a0384 (funcionando el back pero no el qr para coneccion celular)
import "./common.css";

import iconInicio from "../../assets/icons/inicio.png";
import iconInventario from "../../assets/icons/inventario.png";
import iconOrdenes from "../../assets/icons/ordenes.png";
import iconLotes from "../../assets/icons/lotes.png";
import iconProveedores from "../../assets/icons/proveedores.png";
import iconReportes from "../../assets/icons/reportes.png";
<<<<<<< HEAD
import logo from "../../../logo.png"; 

const Sidebar = ({ paginaActual, cambiarPagina }) => {
  return (
    <div className="sidebar">
      
        <div className="sidebar-logo">
          <img src={logo} alt="Logo" className="logo" />
        </div>

      <ul>
        <li
          onClick={() => cambiarPagina("inicio")}
          className={paginaActual === "inicio" ? "active" : ""}
        >
          <img src={iconInicio} alt="Inicio" className="icon" />
          <span>Inicio</span>
        </li>
        <li
          onClick={() => cambiarPagina("inventario")}
          className={paginaActual === "inventario" ? "active" : ""}
        >
          <img src={iconInventario} alt="Inventario" className="icon" />
          <span>Inventario</span>
        </li>
        <li
          onClick={() => cambiarPagina("ordenes")}
          className={paginaActual === "ordenes" ? "active" : ""}
        >
          <img src={iconOrdenes} alt="Órdenes" className="icon" />
          <span>Órdenes</span>
        </li>
        <li
          onClick={() => cambiarPagina("lotes")}
          className={paginaActual === "lotes" ? "active" : ""}
        >
          <img src={iconLotes} alt="Lotes" className="icon" />
          <span>Lotes</span>
        </li>
        <li
          onClick={() => cambiarPagina("proveedores")}
          className={paginaActual === "proveedores" ? "active" : ""}
        >
          <img src={iconProveedores} alt="Proveedores" className="icon" />
          <span>Proveedores</span>
        </li>
        <li
          onClick={() => cambiarPagina("reportes")}
          className={paginaActual === "reportes" ? "active" : ""}
        >
          <img src={iconReportes} alt="Reportes" className="icon" />
          <span>Reportes</span>
        </li>
=======
import logo from "../../../logo.png";

const Sidebar = ({ paginaActual, cambiarPagina }) => {
  const [info, setInfo] = useState(null);

  useEffect(() => {
    // Solo revisa una vez si fastapiInfo ya existe
    if (window.fastapiInfo) {
      setInfo(window.fastapiInfo);
    } else {
      // Espera a que se inyecte sin usar setInterval
      const check = () => {
        if (window.fastapiInfo) {
          setInfo(window.fastapiInfo);
        } else {
          requestAnimationFrame(check);
        }
      };
      requestAnimationFrame(check);
    }
  }, []);

  if (!info) return <div className="sidebar">Cargando IP...</div>;

  const url = `http://${info.ips[0]}:${info.port}`;

  return (
    <div className="sidebar">
      <div className="sidebar-logo">
        <img src={logo} alt="Logo" className="logo" />
      </div>

      <ul>
        <li onClick={() => cambiarPagina("inicio")} className={paginaActual === "inicio" ? "active" : ""}>
          <img src={iconInicio} alt="Inicio" className="icon" />
          <span>Inicio</span>
        </li>
        <li onClick={() => cambiarPagina("inventario")} className={paginaActual === "inventario" ? "active" : ""}>
          <img src={iconInventario} alt="Inventario" className="icon" />
          <span>Inventario</span>
        </li>
        <li onClick={() => cambiarPagina("ordenes")} className={paginaActual === "ordenes" ? "active" : ""}>
          <img src={iconOrdenes} alt="Órdenes" className="icon" />
          <span>Órdenes</span>
        </li>
        <li onClick={() => cambiarPagina("lotes")} className={paginaActual === "lotes" ? "active" : ""}>
          <img src={iconLotes} alt="Lotes" className="icon" />
          <span>Lotes</span>
        </li>
        <li onClick={() => cambiarPagina("proveedores")} className={paginaActual === "proveedores" ? "active" : ""}>
          <img src={iconProveedores} alt="Proveedores" className="icon" />
          <span>Proveedores</span>
        </li>
        <li onClick={() => cambiarPagina("reportes")} className={paginaActual === "reportes" ? "active" : ""}>
          <img src={iconReportes} alt="Reportes" className="icon" />
          <span>Reportes</span>
        </li>

        {/* Solo un QR */}
        <li >
          <QRCode value={url} size={150} />
        </li>
          <a href={url} target="_blank" rel="noreferrer">{url}</a>
>>>>>>> e6a0384 (funcionando el back pero no el qr para coneccion celular)
      </ul>
    </div>
  );
};

export default Sidebar;

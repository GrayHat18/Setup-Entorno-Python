# Setup-Entorno-Python

Código Python para **crear, configurar e instalar automaticamente** un entorno virtual aislado para trabajar en diferentes proyectos python con librerias independientes sin afectar el entorno global del sistema operativo.

---

## 🚀 Características
- Es 100% **multiplataforma**, funciona para Windows 10/11, Linux, macOS.
- Se crea un entorno virtual (`venv`) de forma automaticamente en donde la carpeta donde se guarde este python o en la carpeta del proyecto que se desea desarrollar.
- Se instalan dependencias desde un archivo `requirements.txt` existente o en su defecto genera uno nuevo con dependencias básicas (`pandas`, `openpyxl`).
- No se necesita  configuraciones previas ni privilegios de administrador en el sistema operativo.
- No modifica ni afecta nada del entorno global del sistema operativo donde se encuentre instalado Python.

---

## 🧩 Pasos para Uso Rápido
1. Descargar este repositorio en la carpeta donde se desea crear el entorno virtual, con los siguientes comandos:
   ```bash
   git clone https://github.com/GrayHat18/Setup-Entorno-Python.git
   cd Setup-Entorno-Python

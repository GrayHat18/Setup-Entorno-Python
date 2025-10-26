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
2. Ejecutar el script:
   ```bash
   python setup_env.py
3. Activar el entorno virtual:
   - Window:
     ```bash
     venv\Scripts\activate
   - Linux/macOS:
     ```bash
     source venv/bin/activate

## 📦 Requisitos
1. Tener Python 3.9 o superior instalado en el sistema operativo
2. Tener permisos para crear carpetas y ejecutar scripts locales

## 🧠 Autor
**GrayHat18**
_Desarrollador backend, arquitecto de sistemas y motivado por la automatización digital._
💻 https://github.com/GrayHat18

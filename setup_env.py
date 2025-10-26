#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script universal para crear y configurar un entorno virtual Python
Autor: GrayHat
Repositorio: https://github.com/GrayHat18/Setup-Entorno-Python
Compatibilidad: Windows 10/11, Linux, macOS
"""

import os
import sys
import subprocess
import venv
from pathlib import Path


# === CONFIGURACIÓN GENERAL ===
VENV_DIR = "venv"
REQUIREMENTS_FILE = "requirements.txt"
DEFAULT_PACKAGES = ["pandas", "openpyxl"]


def run_command(command: list[str]) -> None:
    """Ejecuta comandos del sistema mostrando salida en tiempo real."""
    try:
        print(f"\n➡️ Ejecutando: {' '.join(command)}")
        subprocess.check_call(command)
    except subprocess.CalledProcessError as e:
        print(f"❌ Error ejecutando el comando: {e.cmd}")
        sys.exit(1)


def create_virtual_env() -> None:
    """Crea el entorno virtual si no existe."""
    venv_path = Path(VENV_DIR)
    if venv_path.exists():
        print("ℹ️ Entorno virtual existente, reutilizando...")
    else:
        print("🧩 Creando entorno virtual...")
        venv.create(VENV_DIR, with_pip=True)
        print(f"✅ Entorno virtual creado en: {venv_path.resolve()}")


def install_requirements() -> None:
    """Instala dependencias desde requirements.txt o usa las básicas."""
    venv_python = Path(VENV_DIR) / ("Scripts/python.exe" if os.name == "nt" else "bin/python")

    # Crear requirements.txt si no existe
    if not Path(REQUIREMENTS_FILE).exists():
        print("📄 'requirements.txt' no encontrado. Generando uno con dependencias básicas...")
        with open(REQUIREMENTS_FILE, "w", encoding="utf-8") as f:
            f.write("\n".join(DEFAULT_PACKAGES))

    print("📦 Instalando dependencias...")
    run_command([str(venv_python), "-m", "pip", "install", "--upgrade", "pip"])
    run_command([str(venv_python), "-m", "pip", "install", "-r", REQUIREMENTS_FILE])


def activation_instructions() -> None:
    """Muestra cómo activar el entorno según el sistema operativo."""
    if os.name == "nt":
        activation_cmd = r"venv\Scripts\activate"
    else:
        activation_cmd = "source venv/bin/activate"

    print("\n✅ Entorno configurado correctamente.")
    print("--------------------------------------------------")
    print(f"💡 Para activarlo manualmente ejecuta:\n   {activation_cmd}")
    print("--------------------------------------------------\n")


def main() -> None:
    """Ejecución principal del script."""
    print("🚀 Iniciando configuración automática del entorno Python...\n")

    create_virtual_env()
    install_requirements()
    activation_instructions()

    print("🎯 Proceso completado sin errores.")
    print("✨ Tu entorno está listo para usarse.\n")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n🛑 Proceso interrumpido por el usuario.")
        sys.exit(1)
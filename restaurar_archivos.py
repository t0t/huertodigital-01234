#!/usr/bin/env python3
"""
Script para restaurar los archivos principales 0.md, 1.md, 2.md, 3.md y 4.md
"""

import os

directorio = "/Users/a01234/huertodigital-01234/archivo"

# Mapeo de los nuevos nombres a los originales
restaurar = {
    "documento_1.md": "0.md",
    "documento.md": "1.md",
    "documento_4.md": "2.md",
    "documento_3.md": "3.md",
    "documento_2.md": "4.md"
}

# Ejecutar los cambios
for nuevo, original in restaurar.items():
    ruta_nueva = os.path.join(directorio, nuevo)
    ruta_original = os.path.join(directorio, original)
    
    if os.path.exists(ruta_nueva):
        try:
            os.rename(ruta_nueva, ruta_original)
            print(f'Restaurado: {nuevo} → {original}')
        except Exception as e:
            print(f'Error al restaurar {nuevo}: {e}')
    else:
        print(f'No se encontró el archivo {nuevo}')

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script para convertir todos los archivos Markdown (*.md) de la carpeta raíz
en un solo archivo PDF.
"""

import os
import glob
import markdown
from weasyprint import HTML
from pathlib import Path
import tempfile

def main():
    # Directorio raíz donde se encuentran los archivos Markdown
    root_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Obtener todos los archivos .md en la carpeta raíz
    md_files = glob.glob(os.path.join(root_dir, "*.md"))
    
    if not md_files:
        print("No se encontraron archivos Markdown en la carpeta raíz.")
        return
    
    print(f"Se encontraron {len(md_files)} archivos Markdown.")
    
    # Crear un documento HTML combinado
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; }
            h1 { color: #333; }
            h2 { color: #555; }
            pre { background-color: #f5f5f5; padding: 10px; border-radius: 5px; }
            code { font-family: monospace; }
            hr { margin: 30px 0; border: 1px solid #ddd; }
        </style>
    </head>
    <body>
    """
    
    # Ordenar los archivos alfabéticamente
    md_files.sort()
    
    # Procesar cada archivo Markdown
    for md_file in md_files:
        print(f"Procesando: {os.path.basename(md_file)}")
        
        try:
            with open(md_file, 'r', encoding='utf-8') as file:
                md_content = file.read()
            
            # Convertir Markdown a HTML
            file_html = markdown.markdown(
                md_content,
                extensions=['extra', 'codehilite', 'tables']
            )
            
            # Añadir el nombre del archivo como título
            file_name = os.path.basename(md_file)
            html_content += f"<h1>{file_name}</h1>\n"
            html_content += file_html
            html_content += "<hr>\n"  # Separador entre archivos
        
        except Exception as e:
            print(f"Error al procesar {md_file}: {e}")
    
    html_content += """
    </body>
    </html>
    """
    
    # Crear un archivo temporal para el HTML
    with tempfile.NamedTemporaryFile(suffix='.html', delete=False) as temp_html:
        temp_html_path = temp_html.name
        temp_html.write(html_content.encode('utf-8'))
    
    # Ruta del archivo PDF de salida
    output_pdf = os.path.join(root_dir, "documentos_combinados.pdf")
    
    try:
        # Convertir HTML a PDF
        HTML(filename=temp_html_path).write_pdf(output_pdf)
        print(f"PDF creado exitosamente: {output_pdf}")
    except Exception as e:
        print(f"Error al crear el PDF: {e}")
    finally:
        # Eliminar el archivo HTML temporal
        os.unlink(temp_html_path)

if __name__ == "__main__":
    main()

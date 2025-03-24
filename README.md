# Huerto Digital - 01234

https://github.com/t0t/huertodigital-01234

https://t0t.github.io/

https://t0t.github.io/huertodigital-01234/

## Herramientas

### Conversor de Markdown a PDF

El repositorio incluye un script en Python que permite convertir todos los archivos Markdown (*.md) de la carpeta raíz en un único archivo PDF.

#### Requisitos

- Python 3.x
- Bibliotecas: `markdown`, `weasyprint`

#### Instalación

```bash
# Crear un entorno virtual
python -m venv venv

# Activar el entorno virtual
source venv/bin/activate  # En macOS/Linux
# o
# venv\Scripts\activate   # En Windows

# Instalar dependencias
pip install -r requirements.txt
```

#### Uso

Para generar el PDF con todos los documentos Markdown:

```bash
# Activar el entorno virtual si no está activado
source venv/bin/activate  # En macOS/Linux
# o
# venv\Scripts\activate   # En Windows

# Ejecutar el script
python md_to_pdf.py
```

El archivo PDF resultante se guardará como `documentos_combinados.pdf` en la carpeta raíz del proyecto.
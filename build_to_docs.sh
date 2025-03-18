#!/bin/bash

# Script para construir el sitio Quartz y copiarlo a la carpeta docs

echo "Iniciando construcción del sitio Quartz..."

# Ir a la carpeta de Quartz
cd "$(dirname "$0")/quartz"

# Construir el sitio
npx quartz build

# Crear la carpeta docs si no existe
mkdir -p ../docs

# Limpiar la carpeta docs
rm -rf ../docs/*

# Copiar el contenido de public a docs
cp -r public/* ../docs/

echo "¡Construcción completada! El sitio ha sido copiado a la carpeta /docs"
echo "Ahora puedes hacer commit y push a GitHub."
echo "Configura GitHub Pages para usar la rama 'main' y la carpeta '/docs'."

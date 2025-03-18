https://publish.obsidian.md/01234/

# Huerto Digital - Conversión de Notas Obsidian a HTML con Quartz

Este repositorio contiene mis notas de Obsidian y la configuración para convertirlas en un sitio web estático usando Quartz.

## Configuración de Quartz

### Instalación inicial

```bash
# Clonar el repositorio de Quartz
git clone https://github.com/jackyzha0/quartz.git
cd quartz

# Instalar dependencias
npm i

# Ejecutar el asistente de configuración
npx quartz create
```

### Añadir contenido

```bash
# Copiar notas de Obsidian al directorio content de Quartz
cp -r /ruta/a/tus/notas/*.md quartz/content/

# Crear un archivo index.md en la carpeta content
echo "# Huerto Digital

Bienvenido a mi jardín digital de conocimientos interconectados.

## Notas Recientes

- [[nota1]]
- [[nota2]]
- [[nota3]]

" > quartz/content/index.md
```

### Construir y visualizar el sitio

```bash
# Construir el sitio
cd quartz
npx quartz build

# Visualizar el sitio localmente
npx quartz build --serve
```

El sitio estará disponible en: http://localhost:8080

### Consejos importantes

1. **Nombres de archivo**: Evita usar espacios, acentos o caracteres especiales en nombres de archivos.
2. **Enlaces internos**: Usa la sintaxis `[[nombre-archivo]]` para enlaces internos.
3. **Configuración**: Edita `quartz.config.ts` para personalizar el título, colores y comportamiento.
4. **Ignorar carpetas**: Añade directorios a `ignorePatterns` en `quartz.config.ts` para excluir contenido.
5. **URL base**: Para despliegue local, usa `baseUrl: "./"` en la configuración.

### Actualización de contenido

Cada vez que añadas nuevas notas:

1. Copia las nuevas notas a `quartz/content/`
2. Ejecuta `npx quartz build` para reconstruir el sitio
3. Visualiza con `npx quartz build --serve`

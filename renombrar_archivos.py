#!/usr/bin/env python3
"""
Script para renombrar archivos en la carpeta 'archivo'
siguiendo los criterios:
- Nombres claros
- En minúsculas
- Sin números
"""

import os
import re
from pathlib import Path

def limpiar_nombre(nombre_original):
    """Convierte un nombre de archivo según los criterios establecidos."""
    # Obtener nombre sin extensión y extensión
    nombre_base, extension = os.path.splitext(nombre_original)
    
    # Reemplazar referencias numéricas específicas
    nombre_base = nombre_base.replace('01234', 'huerto_digital')
    nombre_base = nombre_base.replace('0123', 'huerto')
    
    # Eliminar prefijos numéricos (como 0_, 1_, 2_, etc.)
    nombre_base = re.sub(r'^\d+_?', '', nombre_base)
    nombre_base = re.sub(r'^\d+\.', '', nombre_base)
    
    # Eliminar números dentro del nombre (excepto en patrones como 'meta-modelo')
    nombre_base = re.sub(r'_\d+_', '_', nombre_base)
    nombre_base = re.sub(r'\d+_', '', nombre_base)
    
    # Manejar casos especiales (nombres que requieren tratamiento particular)
    mapping_especial = {
        # Campo 0
        'matriz': 'matriz_origen',
        'codigo': 'codigo_fuente',
        'depuracion': 'depuracion',
        'preexistencia': 'preexistencia',
        'repositorio': 'repositorio',
        
        # Campo 1
        'arje': 'principio_fundamental',
        'basb': 'construccion_segundo_cerebro',
        'concepto': 'concepto',
        'conciencia': 'conciencia',
        'darse_cuenta': 'darse_cuenta',
        'discernimiento': 'discernimiento',
        'efecto_aladino': 'efecto_aladino',
        'elemento': 'elemento_basico',
        'espiritu': 'espiritu',
        'existencia': 'existencia',
        'idea': 'idea',
        'logos': 'logos_palabra_creadora',
        'luz': 'luz',
        'modelo': 'modelo',
        'nodo_neurona': 'nodo_neurona',
        'observacion': 'observacion',
        'orden': 'orden',
        'razon': 'razon',
        'realidad': 'realidad',
        'sintesis': 'sintesis',
        'sujeto': 'sujeto',
        'universo': 'universo',
        
        # Campo 2
        'autocancelacion': 'autocancelacion',
        'faceta': 'faceta',
        'percepcion': 'percepcion',
        'reshimo': 'reshimo_huella',
        'sesgo': 'sesgo',
        'sinergia': 'sinergia',
        'tension': 'tension',
        'paradoja': 'paradoja',
        'impresion_mental': 'impresion_mental',
        'dualidad_onda-particula': 'dualidad_onda_particula',
        
        # Campo 3
        'concatenacion': 'concatenacion',
        'conectivo': 'conectivo',
        'contexto': 'contexto',
        'convergencia': 'convergencia',
        'explica': 'explicacion',
        'mapa': 'mapa',
        'mente': 'mente',
        'onda': 'onda',
        'palabra': 'palabra',
        'sentido': 'sentido',
        'significado': 'significado',
        'simbolo': 'simbolo',
        'sistema': 'sistema',
        'tetractys': 'tetractys',
        'tetragramaton': 'tetragramaton',
        'vinculo': 'vinculo',
        'cognicion_extendida': 'cognicion_extendida',
        'llm': 'modelos_lenguaje',
        'pardes': 'pardes_jardin_hermeneutica',
        'poesia': 'poesia',
        'cognicion': 'cognicion',
        'sinapsis': 'sinapsis',
        'interpretacion': 'interpretacion',
        'dialogo': 'dialogo',
        'encuentro': 'encuentro',
        'mapa_mental': 'mapa_mental',
        'red_coherente_conocimiento': 'red_coherente_conocimiento',
        'arte': 'arte',
        'informacion': 'informacion',
        'termino': 'termino',
        
        # Campo 4
        'accion': 'accion',
        'cuaternario': 'cuaternario',
        'cuerpo': 'cuerpo',
        'frecuencia': 'frecuencia',
        'objeto': 'objeto',
        'olam': 'olam_mundo',
        'particula': 'particula',
        'resultado': 'resultado',
        'vibracion': 'vibracion',
        'vida': 'vida',
        'ahora': 'ahora_presente',
        'despliegue': 'despliegue',
        'fin': 'fin',
        'mejora_continua': 'mejora_continua',
        'mistica': 'mistica',
        'proceso': 'proceso',
        'coherencia_esencial': 'coherencia_esencial',
        'evidencia': 'evidencia',
        'invarianza_estructural': 'invarianza_estructural',
        'pkm': 'gestion_conocimiento_personal',
        'propiedad': 'propiedad',
        'aaas': 'agentes_como_servicio',
        'coagulacion_significado': 'coagulacion_significado',
        'estructura': 'estructura',
        'hermeneutica': 'hermeneutica',
        'literal': 'literal',
        'recurso': 'recurso',
        
        # Otros casos especiales
        'huerto_digital': 'huerto_digital',
        'evocaciones_poeticas': 'evocaciones_poeticas',
        'evocaciones-poeticas': 'evocaciones_poeticas',
        'estructura_nodal': 'estructura_nodal',
        'meta_busqueda_centralizada': 'meta_busqueda_centralizada',
        'alignment': 'alineamiento',
        'alma': 'alma',
        'analogia': 'analogia',
        'campo-semantico': 'campo_semantico',
        'campo_semantico': 'campo_semantico',
        'causa-efecto': 'causa_efecto',
        'causa_efecto': 'causa_efecto',
        'contemplacion': 'contemplacion',
        'diagrama-huerto_digital': 'diagrama_huerto_digital',
        'diagrama-01234': 'diagrama_huerto_digital',
        'dominio': 'dominio',
        'esquema_huerto_digital_base': 'esquema_huerto_digital_base',
        'esquema_global': 'esquema_global',
        'estructura_huerto_digital': 'estructura_huerto_digital',
        'estructura_vault': 'estructura_vault',
        'faceta_como_percepcion': 'faceta_como_percepcion',
        'frases_clave_huerto_digital': 'frases_clave_huerto_digital',
        'glosario_total': 'glosario_total',
        'gradiente': 'gradiente',
        'index': 'indice',
        'instrucciones_gpt': 'instrucciones_gpt',
        'latencia': 'latencia',
        'meta': 'meta',
        'meta_modelo_huerto_digital': 'meta_modelo_huerto_digital',
        'meta_modelo_huerto_digital_pkms': 'meta_modelo_gestion_conocimiento',
        'metamodelo-index': 'indice_metamodelo',
        'perfil-sergiofores': 'perfil_sergiofores',
        'proyecto': 'proyecto',
        'que_es_huerto_digital': 'que_es_huerto_digital',
        'simbolo-0': 'simbolo_origen',
        'simbolo-1': 'simbolo_unidad',
        'simbolo-2': 'simbolo_dualidad',
        'sonar_pensar_sentir_decir_hacer': 'sonar_pensar_sentir_decir_hacer',
        'insight': 'insight_revelacion',
        'creacion': 'creacion',
        'inteligencia': 'inteligencia',
        'fonema': 'fonema',
        'peso': 'peso',
        'pnl': 'programacion_neurolinguistica',
        'cosa': 'cosa',
        'lugaritmo': 'lugaritmo',
        'kli': 'kli',
        
        # Referencias para los índices
        '0': 'origen_potencialidad',
        '1': 'unidad_direccion',
        '2': 'dualidad_estructura',
        '3': 'conexion_significado',
        '4': 'manifestacion_resultado',
    }
    
    # Aplicar mapeo especial si existe
    if nombre_base in mapping_especial:
        nombre_base = mapping_especial[nombre_base]
    
    # Convertir a minúsculas y reemplazar espacios por guiones bajos
    nombre_base = nombre_base.lower().replace(' ', '_')
    
    # Asegurar que no queden múltiples guiones bajos consecutivos
    nombre_base = re.sub(r'_+', '_', nombre_base)
    
    # Eliminar guiones bajos al inicio o final
    nombre_base = nombre_base.strip('_')
    
    # Si después de todas las transformaciones queda vacío, usar un nombre genérico
    if not nombre_base:
        nombre_base = "documento"
    
    # Reconstruir el nombre con la extensión
    return nombre_base + extension

def renombrar_archivos(directorio):
    """Renombra todos los archivos en el directorio según los criterios."""
    # Crear un diccionario para almacenar las transformaciones (original -> nuevo)
    cambios = {}
    conflictos = []
    
    # Obtener todos los archivos en el directorio
    archivos = [f for f in os.listdir(directorio) if os.path.isfile(os.path.join(directorio, f))]
    
    # Primera pasada: determinar los nuevos nombres
    for archivo in archivos:
        ruta_original = os.path.join(directorio, archivo)
        nuevo_nombre = limpiar_nombre(archivo)
        ruta_nueva = os.path.join(directorio, nuevo_nombre)
        
        # Verificar si el nuevo nombre ya existe o ya está en la lista de cambios
        if os.path.exists(ruta_nueva) and ruta_original != ruta_nueva:
            conflictos.append((archivo, nuevo_nombre, "Ya existe un archivo con este nombre"))
        elif nuevo_nombre in [v for k, v in cambios.items()]:
            conflictos.append((archivo, nuevo_nombre, "Colisión con otro archivo a renombrar"))
        else:
            cambios[archivo] = nuevo_nombre
    
    # Segunda pasada: resolver conflictos
    for original, nuevo, mensaje in conflictos:
        base, ext = os.path.splitext(nuevo)
        contador = 1
        while True:
            nombre_alternativo = f"{base}_{contador}{ext}"
            if not os.path.exists(os.path.join(directorio, nombre_alternativo)) and \
               nombre_alternativo not in [v for k, v in cambios.items()]:
                cambios[original] = nombre_alternativo
                break
            contador += 1
    
    # Imprimir vista previa de cambios
    print("Vista previa de cambios:")
    print("-" * 80)
    for original, nuevo in cambios.items():
        if original != nuevo:
            print(f"{original} -> {nuevo}")
    print("-" * 80)
    
    # Generar un script para ejecutar los cambios reales
    script_path = os.path.join(directorio, "..", "ejecutar_renombrado.py")
    with open(script_path, 'w') as f:
        f.write("#!/usr/bin/env python3\n")
        f.write("import os\n\n")
        f.write("# Script generado automáticamente para renombrar archivos\n\n")
        f.write("directorio = r'{}'\n\n".format(directorio))
        f.write("# Realizar los cambios\n")
        f.write("cambios = {\n")
        for original, nuevo in cambios.items():
            if original != nuevo:
                f.write(f"    '{original}': '{nuevo}',\n")
        f.write("}\n\n")
        f.write("# Ejecutar los cambios\n")
        f.write("for original, nuevo in cambios.items():\n")
        f.write("    ruta_original = os.path.join(directorio, original)\n")
        f.write("    ruta_nueva = os.path.join(directorio, nuevo)\n")
        f.write("    try:\n")
        f.write("        os.rename(ruta_original, ruta_nueva)\n")
        f.write("        print(f'Renombrado: {original} -> {nuevo}')\n")
        f.write("    except Exception as e:\n")
        f.write("        print(f'Error al renombrar {original}: {e}')\n")
    
    # Hacer ejecutable el script
    os.chmod(script_path, 0o755)
    
    print(f"\nSe ha generado un script para ejecutar los cambios en: {script_path}")
    print("Revisa la vista previa anterior y ejecuta el script generado si estás conforme con los cambios.")

if __name__ == "__main__":
    directorio_archivo = os.path.join(os.path.dirname(os.path.abspath(__file__)), "archivo")
    if os.path.exists(directorio_archivo) and os.path.isdir(directorio_archivo):
        renombrar_archivos(directorio_archivo)
    else:
        print(f"Error: No se encontró el directorio 'archivo' en {directorio_archivo}")

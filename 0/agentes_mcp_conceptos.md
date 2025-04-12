# Conceptos Fundamentales: Agentes y MCP

Esta nota introduce conceptos clave relacionados con los sistemas de IA avanzados: los Agentes y el protocolo MCP. Aunque presentamos estas definiciones aquí en la fase **0 (Potencial/Origen)** como conocimiento base, es fundamental entender que su naturaleza operativa se extiende principalmente a través de:
*   **3 (Conexión/Significado):** Facilitando la comunicación y la interacción entre sistemas (MCP, diálogos del agente).
*   **4 (Manifestación/Resultado):** Permitiendo la acción autónoma y la producción de resultados en el entorno (acciones del agente).

## ¿Qué es un Agente (en IA)?

Un **Agente** es una entidad computacional, a menudo impulsada por un LLM, diseñada para actuar de forma autónoma en un entorno digital (o incluso físico) para alcanzar objetivos específicos.

Características clave:

1.  **Percepción:** Recibe información sobre su entorno (datos, sensores, APIs).
2.  **Razonamiento/Planificación:** Procesa la información, delibera sobre posibles acciones y planifica secuencias para lograr sus metas (alineado con **1: Dirección/Propósito** y **2: Distinción/Análisis**).
3.  **Acción:** Ejecuta acciones en su entorno (llamar a APIs, modificar archivos, enviar mensajes) para producir un resultado (**4: Manifestación/Resultado**).
4.  **Autonomía:** Opera con cierto grado de independencia, tomando decisiones sin intervención humana constante.

Los agentes extienden la capacidad de los LLMs más allá de la simple generación de texto, permitiéndoles interactuar activamente con el mundo digital.

## ¿Qué es MCP (Protocolo Puente)?

Basado en nuestra conversación, **MCP** se refiere a un **protocolo o mecanismo específico que actúa como un puente estandarizado** entre un LLM y sistemas externos (APIs, bases de datos, herramientas de software, etc.).

Su función principal es facilitar y estandarizar la comunicación (**3: Conexión/Significado**):

1.  **Habilitar Acceso:** Permite al LLM solicitar información actualizada o específica que no posee internamente.
2.  **Permitir Acción:** Facilita que el LLM desencadene acciones o procesos en otros sistemas (ej: enviar un correo, actualizar una base de datos).
3.  **Estandarizar Interfaz:** Define cómo se deben formular las solicitudes del LLM y cómo deben formatearse las respuestas de los sistemas externos, asegurando una interacción predecible.

MCP es un componente crucial para que los Agentes basados en LLM puedan interactuar eficazmente con herramientas y datos externos.

## Temas Relacionados

*   **Uso de Herramientas (Tool Use) / Llamada a Funciones (Function Calling):** Mecanismos generales (donde MCP sería un ejemplo específico) que permiten a los LLMs invocar funcionalidades externas.
*   **Orquestación de Agentes:** Coordinación de múltiples agentes que colaboran para resolver tareas complejas.
*   **RAG (Retrieval-Augmented Generation):** Técnicas donde el LLM recupera información relevante de fuentes externas *antes* de generar una respuesta, a menudo usando protocolos como MCP para el acceso.
*   **Prompt Engineering:** El arte de diseñar las instrucciones (prompts) para guiar eficazmente el razonamiento y las acciones de los agentes y LLMs.

# Chatbot Amira - Procesamiento de Texto para Deep Learning & NLP

Este repositorio contiene los recursos iniciales para el desarrollo del chatbot inteligente de Amira Rashid, basado en Deep Learning y Procesamiento de Lenguaje Natural (NLP). El propósito es crear una herramienta capaz de responder de manera automática a las preguntas de seguidores en un entorno web, tomando como base datos astrológicos y consultas frecuentes.

## Estructura principal

- **conversations.json**  
  Archivo que almacena los patrones de preguntas y las etiquetas temáticas propuestas por el equipo de Amira.

- **amira_text_processing.py**  
  Script en Python encargado de procesar el archivo de conversaciones, extraer el vocabulario relevante, lematizar y tokenizar los mensajes de entrada ("patterns"), obtener la lista de etiquetas ("tags") y generar la bolsa de palabras para el entrenamiento futuro del chatbot.

- **vocabulario.pkl**  
  Archivo serializado (pickle) que almacena la lista de palabras procesadas (vocabulario lematizado) a partir de los patrones de entrada.

- **tags.pkl**  
  Archivo serializado (pickle) que contiene la lista de etiquetas únicas para clasificar las intenciones o temas de las conversaciones.

- **bow_amira_patterns.csv**  
  Archivo CSV que representa la "bolsa de palabras" de los mensajes de ejemplo, listo para su uso en tareas de modelado y entrenamiento en Deep Learning.

## Propósito

El objetivo de este repositorio es centralizar el procesamiento previo de datos necesarios para entrenar un modelo de chatbot personalizado para Amira Rashid. Este procesamiento incluye la limpieza, lematización, tokenización y vectorización de ejemplos de conversaciones, sentando así las bases para los siguientes pasos: entrenamiento del modelo de Deep Learning y despliegue en web.

## Requisitos técnicos

- Python 3.8+
- [spaCy](https://spacy.io/)  
  Instalar ejecutando:  
  `pip install spacy`  
  y el modelo de español:  
  `python -m spacy download es_core_news_sm`

## Uso

1. Coloca el archivo `conversations.json` en el mismo directorio que el script.
2. Ejecuta el script principal:
    ```
    python amira_text_processing.py
    ```
3. Se generarán los archivos `vocabulario.pkl`, `tags.pkl` y `bow_amira_patterns.csv` en el mismo directorio.

Estos archivos son insumos fundamentales para el entrenamiento del modelo conversacional que se desarrollará en los siguientes sprints.

---

**Autor:**  
Bernardo Corona Domínguez  
Para Digital NAO – Reto Deep Learning y NLP para Chatbot


# Analítica y Visualización de Accidentes de Tráfico en Cataluña con ElasticSearch y Kibana

Este proyecto tiene como objetivo analizar y visualizar datos abiertos sobre atestados de accidentes de tráfico en Cataluña utilizando ElasticSearch como motor de búsqueda y análisis, y Kibana como herramienta de visualización.

## 📊 Descripción general

A partir de un conjunto de datos públicos descargado del portal [datos.gob.es](https://datos.gob.es/), se transforman los registros para ser indexados en ElasticSearch. Luego, mediante Kibana, se construyen dashboards interactivos que permiten explorar patrones temporales, geográficos y estacionales de los incidentes viales.

## 🗂️ Estructura del proyecto

```
/accidentes-trafico-analisis
│
├── data/                                       
│   ├── accidentes_trafico_original.json       # Dataset original 
│   ├── accidentes_trafico_procesado.json      # Dataset listo para ser indexado   
│
├── elasticsearch/
│   ├── mapping_accidentes.json                # Definición del mapping del índice
│   ├── load_data.py                           # Script para cargar datos en ElasticSearch
│
├── kibana/
│   ├── dashboard_ndjson/                      # Visualizaciones exportadas en formato ndjson
│   ├── instrucciones_visualizacion.md         # Guía para importar visualizaciones
│
├── scripts/
│   ├── transformar_dataset.py                 # Limpieza y transformación del dataset original
│
├── README.md
├── requirements.txt                           # Dependencias necesarias para el entorno Python
└── LICENSE
```

## ⚙️ Tecnologías utilizadas

- Python 3
- ElasticSearch
- Kibana
- pandas
- elasticsearch (librería oficial de Python)

## Preparación del entorno

### Linux 🐧

### Windows 🪟

1. Instalar [Java 17/21](https://www.java.com/es/download/).
2. Descargar [ElasticSearch](https://www.elastic.co/downloads/elasticsearch) y [Kibana](https://www.elastic.co/downloads/elasticsearch)
3. Descomprimir ambos .zip y editar:
    - ```config/elasticsearch.yml``` y ```config/kibana.yml``` para desactivar seguridad (igual que en Linux).
4. Ejecutar:
    - ```bin\elasticsearch.bat```
    - ```bin\kibana.bat```

## 🚀 Cómo usar este proyecto

### 1. Clona el repositorio

```bash
git clone https://github.com/dsanchezp25/Mineria-de-accidentes-de-trafico.git
```

### 2. Instala las dependencias

```bash
pip install -r requirements.txt
```

### 3. Ejecuta ElasticSearch y Kibana

En una terminal:
```bash
./elasticsearch-8.12.2/bin/elasticsearch
```
En otra terminal:
```bash
./kibana-8.12.2/bin/kibana
```
Asegúrate de tener ambos servicios levantados. Por defecto:

- ElasticSearch en `http://localhost:9200`
- Kibana en `http://localhost:5601`

### 4. Carga los datos en ElasticSearch

```bash
python elasticsearch/load_data.py
```

### 5. Visualiza en Kibana

- Accede a Kibana
- Crea un index pattern para `accidentes_cataluna`
- Importa las visualizaciones si lo deseas desde `kibana/dashboard_ndjson`

## 📈 Dashboards incluidos

- Evolución temporal de accidentes por mes y año
- Accidentes por región policial y área de tránsito
- Tendencias estacionales

## 📄 Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo LICENSE para más detalles.

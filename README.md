
# Analítica y Visualización de Accidentes de Tráfico en Cataluña con Elasticsearch y Kibana

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
- Elasticsearch
- Kibana
- pandas
- elasticsearch (librería oficial de Python)

## Preparación del entorno

### Linux 🐧
Esta instalación se ha llevado a cabo en Arch Linux, lo único que cambia respecto a otras distribuciones es el comando de actualización de los paquetes del sistema.
1. Actualizar el sistema

```bash
sudo pacman -Syu
```

2. Instalar Java
```bash
sudo pacman -S jre-openjdk
```

3. Comprobar versión de Java
```bash
java -version
```

4. Descargar y descomprimir Elasticsearch
```bash
curl -L -O https://artifacts.elastic.co/downloads/elasticsearch/<versión>
tar -xvf <versión>
```

5. Mover los ficheros extraídos
```bash
sudo mv <versión> /usr/share/elasticsearch
```

6. Crear directorio separado para los datos y asignar permisos de usuario
```bash
sudo mkdir /var/lib/elasticsearch
sudo chown -R <tu_usuario>:<tu_usuario> /var/lib/elasticsearch
```

7. Editar el fichero de configuración de Elasticsearch
```bash
sudo nano /usr/share/elasticsearch/config/elasticsearch.yml
```

8. Modificar la siguiente información según se requiera
```yaml
cluster.name: mdad
node.name: node-mdad
path.data: /var/lib/elasticsearch
path.logs: /usr/share/elasticsearch/logs
```

9. Ejecutar Elasticsearch
```bash
cd /usr/share/elasticsearch/bin/
./elasticsearch
```

10. Para comprobar la correcta ejecución, este comando debería devolver un fichero JSON
```bash
curl -u elastic:"<contraseña>" -k -X GET "https://localhost:9200"
```


### Windows 🪟

1. Instalar [Java 17/21](https://www.java.com/es/download/).
2. Descargar [Elasticsearch](https://www.elastic.co/downloads/elasticsearch) y [Kibana](https://www.elastic.co/downloads/elasticsearch)
3. Descomprimir ambos .zip y editar:
    - ```config/elasticsearch.yml```.
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
./elasticsearch-9.0.1/bin/elasticsearch
```
En otra terminal:
```bash
./kibana-9.0.1/bin/kibana
```
Asegúrate de tener ambos servicios activados. Por defecto:

- ElasticSearch en `http://localhost:9200`
- Kibana en `http://localhost:5601`

### 4. Carga los datos en Elasticsearch

```bash
python3 elasticsearch/load_data.py
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

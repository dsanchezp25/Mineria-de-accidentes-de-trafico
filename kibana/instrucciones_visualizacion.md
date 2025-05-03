
# 🧭 Instrucciones para importar visualizaciones en Kibana

Este directorio contiene visualizaciones y dashboards exportados de Kibana en formato `.ndjson`. A continuación se explica cómo importarlos:

---

## ✅ ¿Cómo importar un dashboard o visualización?

1. Abre tu navegador y accede a Kibana: http://localhost:5601
2. Ve a **Stack Management → Saved Objects**
3. Haz clic en el botón **Import**
4. Selecciona el archivo `.ndjson` deseado desde la carpeta `dashboard_ndjson`
5. Acepta los avisos de sobrescritura si aparecen

---

## 📁 Archivos disponibles

- `atestados_por_anyo.ndjson`: Gráfico de barras con número de atestados por año.
- `por_region_policial.ndjson`: Gráfico de pastel con % de atestados por región policial.

---

💡 Después de importar las visualizaciones, puedes añadirlas a un dashboard o combinarlas en uno nuevo desde la Visualize Library.

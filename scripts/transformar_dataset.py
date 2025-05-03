import json

# Ruta del archivo original
with open("data/accidentes_tráfico.json", encoding="utf-8") as f:
    raw = json.load(f)

# Extraer los datos reales
rows = raw["data"]

# Transformar cada fila en un diccionario con nombres de campo
datos_transformados = []

for r in rows:
    doc = {
        "mes": int(r[8]),
        "nom_mes": r[9],
        "any": int(r[10]),
        "regio_policial": r[11],
        "area_transit": r[12],
        "nombre_atestats": int(r[13])
    }
    datos_transformados.append(doc)

# Guardar en archivo JSON como lista de diccionarios
with open("data/accidentes_trafico_procesado.json", "w", encoding="utf-8") as f:
    json.dump(datos_transformados, f, ensure_ascii=False, indent=2)

print("✅ Transformación completada. Datos procesados guardados en data/accidentes_trafico_procesado.json")

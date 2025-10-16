# vehicles-streamlit
Proyecto del Sprint 7 – Rodrigo García – App web con Streamlit

## Vehicles Streamlit App
Aplicación web simple desarrollada con Streamlit para explorar el dataset `vehicles_us.csv`.

## Descripción
Este proyecto forma parte del Sprint 7 del Bootcamp de Análisis de Datos (TripleTen).  
El objetivo es crear una aplicación web interactiva que permita explorar datos de anuncios de venta de coches en Estados Unidos.

## Funcionalidad
- Muestra una vista previa de las primeras filas del dataset.  
- Genera un histograma de la columna `odometer`.  
- Genera un gráfico de dispersión `odometer` vs `price`.  
- Incluye controles opcionales con checkboxes para mostrar/ocultar los gráficos.

## Cómo ejecutar localmente

### 1) Crear y activar entorno virtual (ejemplo con Python 3.11)
```bash
py -3.11 -m venv vehicles_env
.\vehicles_env\Scripts\Activate
```

### 2) Instalar dependencias
```bash
pip install -r requirements.txt
```

### 3) Ejecutar la aplicación
```bash
streamlit run app.py
```

### 4) Abrir en el navegador
La app está disponible en:  
http://localhost:8501

---
## Demo en vivo
Puedes ver la aplicación desplegada aquí:  
[https://vehicles-streamlit-sjp6.onrender.com](https://vehicles-streamlit-sjp6.onrender.com)


## Autor
Proyecto desarrollado por **Rodrigo García (icespots)** como práctica del módulo de **Streamlit (Sprint 7)**.

# 🚗 EDA · Accidentalidad en Madrid (2024)

![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?logo=jupyter&logoColor=white)
![pandas](https://img.shields.io/badge/pandas-150458?logo=pandas&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?logo=scikitlearn&logoColor=white)

> **Máster en Big Data · Práctica final del bloque de Python**

Análisis Exploratorio de Datos (EDA) sobre los accidentes de tráfico registrados en la ciudad de Madrid durante 2024, a partir de los **datos abiertos del Ayuntamiento de Madrid**, y entrenamiento de un modelo de **Regresión Logística** para predecir si un implicado da positivo en alcohol.

---

## ❓ Pregunta de negocio

> **¿En qué franja horaria se producen los accidentes con mayor gravedad (ingreso superior a 24 horas o fallecidos) y qué condiciones (estado meteorológico, tipo de accidente, etc.) pueden influir en ello?**

---

## 🗂️ Estructura del repositorio

| Archivo | Descripción |
|---|---|
| 📓 [`EDA_FERNANDO.ipynb`](EDA_FERNANDO.ipynb) | Notebook con todo el EDA, visualizaciones, conclusiones y el entrenamiento del modelo. |
| 🐍 [`models.py`](models.py) | Clase `AlcoholLogisticModel` con los métodos `fit`, `predict`, `evaluate`, `save_model` y `load_model`. |
| 📄 [`2024_Accidentalidad.csv`](2024_Accidentalidad.csv) | Dataset de accidentes de tráfico de Madrid en 2024 (separador `;`). |
| 💾 [`fernando_modelo.pkl`](fernando_modelo.pkl) | Modelo entrenado guardado con `pickle`. |

---

## 🧭 Contenido del notebook

**Parte I · Análisis Exploratorio (EDA)**

1. 📋 **Descripción de los datos**: carga, tamaño, duplicados y tipos de datos.
2. 🧹 **Preparación y limpieza**: eliminación de columnas, tratamiento de nulos, agrupación de colisiones y transformación de fecha y hora.
3. 📊 **Análisis univariante**: distribución de cada variable.
4. 🔗 **Análisis bivariante**: codificación de variables, matriz de correlación y respuesta a la pregunta de negocio (definición del *tramo negro* 17h - 21h).
5. ➕ **Pregunta adicional**: relación entre estado meteorológico y lesividad.
6. ✅ **Conclusiones**

**Parte II · Modelo de Regresión Logística**

7. 🧩 **Selección y preparación de las variables**
8. 🏋️ **Entrenamiento y evaluación**
9. 💾 **Guardado y carga del modelo**

---

## 📌 Conclusiones del EDA

- 🕔 El mayor número de accidentes se da **por la tarde**, aunque **a las 8-9 de la mañana** también es una hora complicada.
- 🚑 Los accidentes más graves (ingreso > 24 h o fallecidos) se concentran sobre todo por la tarde, lo que lleva a definir un **tramo negro entre las 17h y las 21h**.
- 🛣️ Muchos de ellos se producen en **carretera**, coincidiendo con el retorno a casa del trabajo.
- 🍺 **El alcohol o la edad no fueron determinantes.**
- 🚙 La mayoría de los accidentes son **colisiones entre coches** (probablemente distracciones).

### 📢 Propuesta de campaña

Insistir en que **el desplazamiento hacia o desde el trabajo es muy peligroso en horas punta**.

> 🔍 **Línea de mejora:** sería un buen dato lograr saber cuál fue la causa de la distracción (encender un cigarro, hablar por el móvil, etc.).

---

## 🤖 Modelo de Regresión Logística

- **Variable objetivo:** `positiva_alcohol`
- **Variables predictoras:** tipo de accidente, hora, sexo, tipo de vehículo, estado meteorológico y mes.
- **División:** 80 % entrenamiento / 20 % prueba.

> ⚠️ El modelo obtiene un **accuracy muy elevado**, pero la matriz de confusión muestra que **nunca predice los positivos**: los datos están **totalmente desbalanceados**, por lo que el modelo no tendría mucho valor. Lo adecuado sería probar otro modelo.

---

## 🚀 Cómo ejecutarlo

```bash
# 1. Clonar el repositorio
git clone https://github.com/fernanditomartinez85/EDA-ACCIDENTALIDAD-MADRID.git
cd EDA-ACCIDENTALIDAD-MADRID

# 2. Instalar dependencias
pip install pandas numpy matplotlib seaborn scikit-learn jupyter

# 3. Abrir el notebook
jupyter notebook EDA_FERNANDO.ipynb
```

### Requisitos

- Python 3
- pandas / numpy
- matplotlib / seaborn
- scikit-learn
- pickle (incluido en Python)

---

## 📚 Fuente de los datos

- Dataset (CSV): <https://datos.madrid.es/egob/catalogo/300228-28-accidentes-trafico-detalle.csv>
- Dataset (Excel): <https://datos.madrid.es/egob/catalogo/300228-29-accidentes-trafico-detalle.xlsx>
- Descripción de las variables: [Estructura_ConjuntoDatos_Accidentesv2.pdf](https://datos.madrid.es/FWProjects/egob/Catalogo/Seguridad/Ficheros/Estructura_ConjuntoDatos_Accidentesv2.pdf)

---

<details>
<summary><b>📝 Ver el enunciado completo de la práctica</b></summary>

<br>

A continuación, os presentamos la práctica final para el bloque de Python, cuyo objetivo principal es llevar a cabo un Análisis Exploratorio de Datos (EDA) a partir de un conjunto de datos abiertos de accidentes de tráfico en la ciudad de Madrid. Posteriormente, y usando la información obtenida, se entrenará un modelo de Regresión Logística que ayude a predecir la probabilidad de dar positivo en alcohol.

Los datos empleados en este EDA se encuentran publicados por el Ayuntamiento de Madrid y se pueden descargar en diferentes formatos (CSV o Excel). Adicionalmente, se cuenta con un documento PDF que describe la estructura de las variables. Este dataset contiene información detallada sobre los accidentes de tráfico: fecha, hora, tipo de accidente, tipo de persona implicada, etc.

### 1. Análisis Exploratorio de los Datos (EDA)

**Objetivo**

Realizar un análisis exploratorio que ayude a entender la naturaleza de los datos y preparar la información para su posterior uso en un modelo de Machine Learning. Formular y responder a la pregunta de negocio: *“¿En qué franja horaria se producen los accidentes con mayor gravedad (ingreso superior a 24 horas o fallecidos) y qué condiciones (estado meteorológico, tipo de accidente, etc.) pueden influir en ello?”*

**Tareas propuestas**

- **Cargar los datos:** leer el fichero, inspeccionar la forma del dataframe y revisar los tipos de datos de cada columna.
- **Limpieza de datos y tratamiento de valores nulos:** identificar columnas con valores faltantes y decidir una estrategia para tratarlos (eliminar filas, rellenar con media o mediana, etc.), reflexionando si tiene sentido o no.
- **Codificación de variables categóricas.**
- **Exploración univariante y bivariante:**
  - Distribución de variables categóricas: tipos de accidente, tipo de persona, sexo, etc.
  - Distribución de variables numéricas: coordenadas UTM, número de calle, etc.
  - Búsqueda de relaciones entre variables (¿existe relación entre la hora y el tipo de accidente?, ¿entre el estado meteorológico y la lesividad?).
- **Categoría adicional** (basta con elegir al menos una y desarrollarla con suficiente detalle):
  - Identificación de outliers.
  - Análisis de correlaciones (matriz de correlaciones y heatmap).
  - Análisis geográfico (mapas de densidad con las coordenadas UTM, “puntos calientes”).
  - Estudio de la temporalidad con series de tiempo.
  - Análisis de sesgo y validación de datos.
- **Presentación de resultados:** organizar el notebook en secciones lógicas con títulos y subtítulos, añadir una explicación tras cada resultado o al final de cada sección, y explicar el razonamiento de cada decisión para que cualquier persona pueda seguir el EDA. Si hay limitaciones o datos insuficientes, añadirlo como posible línea de mejora.
- **Conclusiones del EDA:** resumir los hallazgos relevantes y responder a la pregunta de negocio inicial.

**Preguntas guía** (se recomienda responder entre 6 y 10):

1. ¿Qué tipo de accidente es el más frecuente en cada distrito?
2. ¿Qué franja horaria concentra mayor número de atropellos a personas?
3. ¿Existe relación entre el rango de edad de la persona implicada y la gravedad de las lesiones (lesividad)?
4. ¿Existen diferencias en la positividad en alcohol según el sexo de la persona implicada?
5. ¿En qué meses del año (o estaciones) se produce un mayor número de accidentes?
6. ¿Se observa alguna relación entre el estado meteorológico y la lesividad de los accidentes?
7. ¿El tipo de vehículo implicado influye en la probabilidad de sufrir lesiones graves?
8. ¿En qué tipos de accidente se da más frecuencia de positivos en alcohol?
9. ¿Existen diferencias notables en los accidentes implicando peatones según el distrito?
10. ¿En qué horas del día ocurren más accidentes con caída (motocicleta, bicicleta, etc.)?
11. ¿Hay relación entre el tipo de persona (conductor, peatón, testigo, etc.) y el tipo de accidente?
12. ¿Se concentran más accidentes con positivo en droga en determinados tipos de accidente?
13. ¿Existen distritos con un mayor porcentaje de accidentes graves (lesividad 03 o 04) respecto al total del distrito?
14. ¿Los accidentes que ocurren de madrugada (00:00-06:00) tienen mayor incidencia de positividad en alcohol?
15. ¿Qué rango de edad aparece más frecuentemente como conductor en los accidentes y/o tipo de lesividad?

### 2. Modelo de Regresión Logística

**Objetivo**

Usar la información preprocesada del EDA para entrenar un modelo de Regresión Logística que prediga si un implicado da positivo en alcohol (`positiva_alcohol`) o no, organizando el código en un script independiente `models.py` con una clase que centralice la lógica del modelo.

**Tareas propuestas**

- **Selección y preparación de las variables:** definir la variable objetivo (`positiva_alcohol`), seleccionar las variables predictoras, codificar las categóricas y normalizar/estandarizar las numéricas si es necesario.
- **Separación de datos:** train/test split (por ejemplo, 80 % - 20 %).
- **Creación de la clase del modelo en `models.py`** (por ejemplo `AlcoholLogisticModel`) con los métodos `__init__`, `fit`, `predict`, `evaluate`, `save_model` y `load_model`.
- **Entrenamiento:** importar la clase en el notebook, crear una instancia, entrenar y visualizar las métricas.
- **Evaluación e interpretación de resultados:** evaluar en el conjunto de test (accuracy, F1-score, etc.) y conectar los hallazgos con la pregunta de negocio.

</details>

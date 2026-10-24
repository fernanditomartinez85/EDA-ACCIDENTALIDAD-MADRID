# 🚗 Accidentalidad en Madrid (2024)

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white) ![pandas](https://img.shields.io/badge/pandas-150458?style=flat-square&logo=pandas&logoColor=white) ![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white) ![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat-square&logo=scikitlearn&logoColor=white) ![Matplotlib](https://img.shields.io/badge/Matplotlib-11557c?style=flat-square) ![Seaborn](https://img.shields.io/badge/Seaborn-4c72b0?style=flat-square) ![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=flat-square&logo=jupyter&logoColor=white)

> Práctica final de Python: análisis exploratorio de los accidentes de tráfico de Madrid y un modelo de clasificación.

## 🎯 Objetivo

A partir de los [datos abiertos de accidentes de tráfico](https://datos.madrid.es/egob/catalogo/300228-28-accidentes-trafico-detalle.csv) del Ayuntamiento de Madrid en 2024 ([descripción de las variables](https://datos.madrid.es/FWProjects/egob/Catalogo/Seguridad/Ficheros/Estructura_ConjuntoDatos_Accidentesv2.pdf)), se resuelven dos problemas:

- **Análisis exploratorio (EDA):** entender la naturaleza de los datos, prepararlos para el modelo y responder a la pregunta de negocio: *¿En qué franja horaria se producen los accidentes con mayor gravedad (ingreso superior a 24 horas o fallecidos) y qué condiciones (estado meteorológico, tipo de accidente, etc.) pueden influir en ello?*
- **Clasificación:** predecir con una Regresión Logística si un implicado da positivo en alcohol (`positiva_alcohol`).

## 📊 Datos

Datos abiertos del Ayuntamiento de Madrid con el detalle de los accidentes de tráfico de 2024: una fila por persona implicada, con fecha, hora, distrito, tipo de accidente, estado meteorológico, tipo de vehículo, edad, sexo, lesividad y resultado de las pruebas de alcohol y drogas.

- Fuente: [datos.madrid.es](https://datos.madrid.es/egob/catalogo/300228-28-accidentes-trafico-detalle.csv)
- [Descripción de las variables](https://datos.madrid.es/FWProjects/egob/Catalogo/Seguridad/Ficheros/Estructura_ConjuntoDatos_Accidentesv2.pdf)

## 🗂️ Estructura del proyecto

```
├── 2024_Accidentalidad.csv    Datos en crudo de los accidentes de tráfico de Madrid en 2024 (separador ;)
├── EDA_FERNANDO.ipynb         Análisis exploratorio, conclusiones y entrenamiento del modelo
├── models.py                  Clase AlcoholLogisticModel con la lógica del modelo
├── test_models.py             Test de la clase: crearla, entrenarla, evaluarla, guardarla y cargarla
├── fernando_modelo.pkl        Modelo entrenado guardado con pickle
└── requirements.txt           Librerías necesarias
```

## ⚙️ Requisitos

Python 3 con pandas, numpy, scikit-learn, matplotlib y seaborn (por ejemplo, el entorno `base` de Anaconda), o instalarlas con:

```
pip install -r requirements.txt
```

## ▶️ Ejecución

Todos los comandos se lanzan desde la carpeta del proyecto.

```
jupyter notebook EDA_FERNANDO.ipynb
```

Para lanzar el test de la clase:

```
python -m unittest test_models
```

El notebook lee `2024_Accidentalidad.csv` e importa la clase `AlcoholLogisticModel` de [models.py](models.py), por lo que los tres ficheros deben estar en la misma carpeta. Al final se guarda el modelo entrenado en `fernando_modelo.pkl` y se vuelve a cargar.

## 🤖 Modelo

La clase `AlcoholLogisticModel` recibe en `__init__` los conjuntos de entrenamiento y prueba y tiene los métodos `fit`, `predict`, `evaluate` (accuracy, precisión, recall y F1, matriz de confusión y curvas ROC y precisión-recall), `save_model` y `load_model`. El modelo es un pipeline con un `OneHotEncoder` y una Regresión Logística con `class_weight='balanced'`, para compensar que solo un 3 % de los implicados da positivo.

| Problema | Clase | Modelo elegido | Transformaciones | Resultado en test |
|---|---|---|---|---|
| Positivo en alcohol | `AlcoholLogisticModel` | Regresión Logística con `class_weight='balanced'` y split 80 % / 20 % estratificado | OneHotEncoder de tipo de accidente, franja horaria, sexo, tipo de vehículo, estado meteorológico y mes | Detecta 194 de los 286 positivos (recall 0,68) con precisión 0,10; AUC ROC 0,81 |

## 📓 Notebook

En [EDA_FERNANDO.ipynb](EDA_FERNANDO.ipynb) se hace el análisis exploratorio de los datos y el entrenamiento del modelo:

- **Descripción de los datos:** carga del CSV, tamaño, duplicados (se eliminan 2.053 registros) y tipos de datos.
- **Preparación y limpieza:** se eliminan `positiva_droga` (solo 203 registros con valor) y `num_expediente`, se agrupan las colisiones frontal, fronto-lateral y lateral en *Colisión doble*, los nulos de lesividad pasan a *77 - Se desconoce* y los de estado meteorológico se rellenan con la moda. Se crea la columna `mes`, la hora se redondea a la hora entera y se revisan los outliers de las coordenadas (se mantienen).
- **Análisis univariante:** distribución de tipo de accidente, estado meteorológico, tipo de vehículo, tipo de persona, sexo, distrito, edad, lesividad, mes, hora y positivo en alcohol.
- **Análisis bivariante:** tablas y gráficos para responder a la pregunta de negocio. Se define un *tramo negro* entre las 17h y las 21h y se estudia por sexo y alcohol, distrito, localización, edad y tipo de accidente, y se cruza la gravedad con el estado meteorológico y el tipo de accidente.
- **Pregunta adicional:** relación entre el estado meteorológico y la lesividad.
- **Modelo:** selección de variables a partir de los positivos en alcohol, hora en franjas horarias, entrenamiento, evaluación, coeficientes del modelo y guardado.

## 💡 Conclusiones

- En el **tramo negro (17h - 21h)** se concentra una cuarta parte de los accidentes graves, y los puntos con más accidentes en ese tramo son las autovías de acceso a Madrid (A-2, A-42, M-30, M-40).
- El **tipo de accidente** es lo que más influye en la gravedad: los atropellos a personas son los que más acaban en accidente grave (6,4 %), frente al 0,7 % de los alcances. El **estado meteorológico** no influye.
- **Propuestas:** campaña sobre los desplazamientos al trabajo en hora punta, más vigilancia en las autovías de acceso al final de la jornada, protección de los peatones y controles de alcoholemia de noche y de madrugada.
- El **modelo de alcohol** detecta 2 de cada 3 positivos a cambio de muchas falsas alarmas. Ser hombre y la madrugada son lo que más sube la probabilidad de dar positivo.

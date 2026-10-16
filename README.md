# EDA: Accidentalidad en Madrid (2024)

A partir de los datos abiertos de accidentes de tráfico del Ayuntamiento de Madrid en 2024, se realiza un Análisis Exploratorio de Datos (EDA) y se entrena un modelo de machine learning:

- **EDA:** entender la naturaleza de los datos, prepararlos para el modelo y responder a la pregunta de negocio.
- **Clasificación:** predecir con una Regresión Logística si un implicado da positivo en alcohol (`positiva_alcohol`).

**Pregunta de negocio:** ¿En qué franja horaria se producen los accidentes con mayor gravedad (ingreso superior a 24 horas o fallecidos) y qué condiciones (estado meteorológico, tipo de accidente, etc.) pueden influir en ello?

## Estructura del proyecto

```
├── 2024_Accidentalidad.csv    Datos en crudo de los accidentes de tráfico de Madrid en 2024 (separador ;)
├── EDA_FERNANDO.ipynb         Análisis exploratorio, conclusiones y entrenamiento del modelo
├── models.py                  Clase AlcoholLogisticModel con la lógica del modelo
└── fernando_modelo.pkl        Modelo entrenado guardado con pickle
```

## Requisitos

Python 3 con pandas, numpy, scikit-learn, matplotlib y seaborn (por ejemplo, el entorno `base` de Anaconda).

## Ejecución

Desde la carpeta del proyecto, abrir el notebook y ejecutar las celdas en orden:

```
jupyter notebook EDA_FERNANDO.ipynb
```

El notebook importa la clase `AlcoholLogisticModel` de [models.py](models.py), por lo que ambos ficheros deben estar en la misma carpeta junto con el CSV.

## Notebook

En [EDA_FERNANDO.ipynb](EDA_FERNANDO.ipynb) el análisis se organiza en las siguientes secciones:

- **Descripción de los datos:** carga del CSV, tamaño, duplicados (se eliminan 2.053 registros) y tipos de datos.
- **Preparación y limpieza:**
  - Se eliminan `positiva_droga` (solo 203 registros con valor) y `num_expediente`.
  - Se agrupan las colisiones frontal, fronto-lateral y lateral en *Colisión doble*.
  - Los nulos de lesividad se rellenan con *Sin asistencia sanitaria* y los de estado meteorológico con la moda.
  - Se crea la columna `mes` a partir de la fecha y la hora se redondea a la hora entera.
- **Análisis univariante:** distribución de tipo de accidente, estado meteorológico, tipo de vehículo, tipo de persona, sexo, distrito, edad, lesividad, mes, hora y positivo en alcohol.
- **Análisis bivariante:** codificación de las variables categóricas con `LabelEncoder`, matriz de correlación y gráficos para responder a la pregunta de negocio. Se define un *tramo negro* entre las 17h y las 21h y se estudia por sexo y alcohol, distrito, localización, edad y tipo de accidente.
- **Pregunta adicional:** relación entre el estado meteorológico y la lesividad.
- **Conclusiones** y propuesta de campaña.

## Conclusiones del EDA

- El mayor número de accidentes se da por la tarde, aunque a las 8-9 de la mañana también es una hora complicada.
- Los accidentes con ingreso superior a 24 horas o fallecidos se concentran sobre todo por la tarde, por lo que se define como tramo negro de 17h a 21h.
- Muchos de ellos se producen en carretera, coincidiendo con la vuelta a casa del trabajo.
- El alcohol o la edad no fueron determinantes.
- La mayoría de los accidentes son colisiones entre coches (probablemente distracciones).

**Propuesta de campaña:** insistir en que el desplazamiento hacia o desde el trabajo es muy peligroso en horas punta. Como línea de mejora, sería un buen dato saber cuál fue la causa de la distracción (encender un cigarro, hablar por el móvil, etc.).

## Modelo

La clase `AlcoholLogisticModel` de [models.py](models.py) recibe en `__init__` los conjuntos de entrenamiento y prueba y tiene los métodos `fit`, `predict`, `evaluate` (accuracy y matriz de confusión), `save_model` y `load_model`.

| Problema | Clase | Modelo | Variables predictoras | Resultado en test |
|---|---|---|---|---|
| Positivo en alcohol | `AlcoholLogisticModel` | Regresión Logística, split 80 % / 20 % | Tipo de accidente, hora, sexo, tipo de vehículo, estado meteorológico y mes (codificadas con `LabelEncoder`) | Accuracy muy elevado, pero nunca predice los positivos: los datos están totalmente desbalanceados |

Lo adecuado sería probar otro modelo.

## Datos

- Dataset (CSV): https://datos.madrid.es/egob/catalogo/300228-28-accidentes-trafico-detalle.csv
- Descripción de las variables: https://datos.madrid.es/FWProjects/egob/Catalogo/Seguridad/Ficheros/Estructura_ConjuntoDatos_Accidentesv2.pdf

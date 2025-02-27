
# Características categóricas (datos de tipo cadena)
CATEGORICAL_FEATURE_KEYS = ['Wilderness_Area', 'Soil_Type']

# Características numéricas marcadas como continuas
NUMERIC_FEATURE_KEYS = [
    'Elevation', 'Aspect', 'Slope', 'Horizontal_Distance_To_Hydrology',
    'Vertical_Distance_To_Hydrology', 'Horizontal_Distance_To_Roadways',
    'Hillshade_9am', 'Hillshade_Noon', 'Hillshade_3pm',
    'Horizontal_Distance_To_Fire_Points'
]

# Característica que se puede agrupar en intervalos (por ejemplo, Elevation podría ser una opción)
BUCKET_FEATURE_KEYS = ['Elevation']

# Número de intervalos utilizados por tf.transform para codificar cada característica de tipo bucket
FEATURE_BUCKET_COUNT = {'Elevation': 5}

# Característica que el modelo predecirá
LABEL_KEY = 'Cover_Type'

# Función de utilidad para renombrar la característica transformada
def transformed_name(key):
    return key + '_xf'

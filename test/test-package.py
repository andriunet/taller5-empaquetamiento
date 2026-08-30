from pathlib import Path

import pandas as pd
from model.predict import make_prediction

# El archivo de datos se busca en la misma carpeta de este script,
# de modo que funcione sin importar desde dónde se ejecute.
CSV_PATH = Path(__file__).resolve().parent / "bankchurn_test.csv"

sample_input_data = pd.read_csv(CSV_PATH)
result = make_prediction(input_data=sample_input_data)

print("Version del paquete:", result["version"])
print("Errores            :", result["errors"])
print("No. de predicciones:", len(result["predictions"]))
print("Primeras 20        :", result["predictions"][:20])

# Taller 5 - Empaquetamiento

Empaquetamiento del modelo de prediccion de abandono de clientes bancarios
(bank churn) usando setuptools, tox y build.

## Estructura

```
package-src/            Codigo fuente del paquete
  model/                Paquete Python (config, pipeline, entrenamiento, prediccion)
  requirements/         Dependencias del paquete, de prueba y de tipos
  tests/                Pruebas unitarias (pytest)
  setup.py              Metadatos y definicion del paquete
  tox.ini               Ambientes de automatizacion (train, test_package, checks)
test/                   Prueba de humo del paquete ya instalado
  test-package.py
  bankchurn_test.csv
```

## Uso rapido

```bash
cd package-src
tox run -e train           # entrena y guarda el modelo
tox run -e test_package    # entrena y ejecuta las pruebas unitarias
python3 -m build           # genera dist/*.tar.gz y dist/*.whl
```

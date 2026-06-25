# Script: obtener companias telefonicas

Este script consulta el portal de CRT, extrae companias y URLs de consulta, y guarda el resultado en `companies.json`.

## Requisitos

- Python 3.10 o superior
- `pip` habilitado
- Conexion a internet

## Dependencias

Las dependencias del proyecto estan en `requirements.txt`:

- `beautifulsoup4==4.15.0`
- `requests==2.34.2`

## Instalacion

1. (Opcional, recomendado) Crear y activar un entorno virtual.

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Windows (PowerShell)

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

2. Instalar dependencias:

```bash
pip install -r requirements.txt
```

## Ejecutar

```bash
python app.py
```

## Resultado

Al terminar, el script crea o sobrescribe el archivo `companies.json` con este formato:

```json
{
  "version": 1710000000,
  "companies": [
    {
      "name": "Nombre de compania",
      "url": "https://ejemplo.com"
    }
  ]
}
```

- `version`: timestamp Unix del momento de ejecucion.
- `companies`: lista de companias extraidas del sitio.

## Configuracion

En `constants.py` puedes ajustar:

- `URL`: sitio fuente a consultar.
- `fileJson`: nombre/ruta del archivo de salida JSON.

## Solucion de problemas

- **`ModuleNotFoundError`**: ejecuta `pip install -r requirements.txt` en el entorno activo.
- **Error HTTP**: revisa tu conexion y disponibilidad de la URL configurada.
- **JSON vacio o incompleto**: la estructura HTML del sitio pudo cambiar (selector `operators-list` en `app.py`).

# Script: obtener compañías telefónicas

Este script consulta el portal de CRT, extrae compañías y URLs de consulta, y guarda el resultado en `companies.json`.

## Requisitos

- Python 3.10 o superior
- `pip` habilitado
- Conexión a internet

## Dependencias

Las dependencias del proyecto están en `requirements.txt`:

- `beautifulsoup4==4.15.0`
- `requests==2.34.2`

## Instalación

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
      "name": "Nombre de compañía",
      "url": "https://ejemplo.com"
    }
  ]
}
```

- `version`: timestamp Unix del momento de ejecución.
- `companies`: lista de compañías extraídas del sitio.

## Configuración

En `constants.py` puedes ajustar:

- `URL`: sitio fuente a consultar.
- `fileJson`: nombre/ruta del archivo de salida JSON.

## Solución de problemas

- **`ModuleNotFoundError`**: ejecuta `pip install -r requirements.txt` en el entorno activo.
- **Error HTTP**: revisa tu conexión y disponibilidad de la URL configurada.
- **JSON vacío o incompleto**: la estructura HTML del sitio pudo cambiar (selector `operators-list` en `app.py`).

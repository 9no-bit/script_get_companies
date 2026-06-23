# Script: obtener companias telefonicas

Este script consulta el portal de CRT y muestra en consola nombres de companias y sus URLs.

## Requisitos previos

- Python 3.10 o superior
- `pip` habilitado
- Conexion a internet (el script consume una URL publica)

## Instalacion

1. (Opcional, recomendado) Crear y activar entorno virtual:

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

## Ejecutar el script

```bash
python app.py
```

## Salida esperada

Veras mensajes como:
- `:::::Iniciando proceso:::::`
- `Datos obtenidos:`
- lineas con `nombre url`
- `:::::Proceso finalizado:::::`

## Solucion de problemas

- **`ModuleNotFoundError`**: ejecuta `pip install -r requirements.txt` en el entorno activo.
- **No imprime resultados**: el HTML del sitio puede haber cambiado; valida `class_='operators-list'` en `app.py`.
- **Error HTTP**: revisa conexion a internet y disponibilidad del portal en la URL de `constants.py`.

## Notas

- La URL origen esta definida en `constants.py`.
- Si la estructura HTML del sitio cambia, puede fallar el parseo con BeautifulSoup.

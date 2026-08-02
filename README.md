# AdHoc Challenge

## Cómo ejecutar el script

### Usando uv

```bash
uv sync
uv run main.py
```

### Usando Python/pip

```bash
python main.py 
```

### Argumentos

| Argumento | Alias | Tipo | Default | Descripción |
|---|---|---|---|---|
| `--umbral` | `-u` | int | `25` | Umbral de edad para segmentación |
| `--dni` | `-d` | str | `None` | DNI de la persona a consultar |

Ejemplo:

```bash
# Cambiar el umbral de segmentación
uv run main.py -u 30

# Consultar la edad de una persona puntual por DNI
uv run main.py -d 41942661

# Usando ambos
uv run main.py -u 30 -d 41942661
```

Si no se pasa `--dni`, esa sección simplemente se omite. Si se pasa un DNI que no existe en los datos se informa que no fue encontrado.


## Cómo correr las pruebas

Las pruebas están escritas con pytest:

### Usando uv

```bash
uv run pytest
```

### Usando Python/pip

```bash
pip install pytest
pytest
```

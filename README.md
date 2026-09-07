# 💾 Application Checkpointing

## Descripción

Este proyecto contiene un ejemplo de **Application Checkpointing** en Python. El programa permite guardar el estado actual de una ejecución y posteriormente restaurarlo.

La finalidad es que, si el programa se detiene o ocurre una interrupción, sea posible recuperar la información guardada y continuar desde el último punto registrado.

## 🔧 Herramientas utilizadas

El programa utiliza diferentes herramientas para guardar y restaurar el estado:

* **Pickle:** permite guardar y recuperar objetos de Python.
* **`pickle.dump()`:** guarda el estado actual del programa en un archivo.
* **`pickle.load()`:** carga la información guardada anteriormente.
* **Archivo `.pkl`:** almacena el checkpoint del programa.
* **Funciones:** organizan las operaciones para guardar y restaurar el estado.

## 💻 Funcionamiento

Al ejecutar el programa, se puede modificar el estado de la aplicación y guardar un checkpoint.

Por ejemplo:

```text
Estado actual:
Contador: 5

Checkpoint guardado correctamente.

Estado actual:
Contador: 10

Checkpoint guardado correctamente.
```

Si el programa se cierra o se interrumpe, al ejecutarlo nuevamente se puede cargar el último checkpoint:

```text
Checkpoint encontrado.

Estado restaurado:
Contador: 10

La ejecución continúa desde el estado guardado.
```

De esta manera, el programa puede recuperar su estado anterior sin tener que comenzar nuevamente desde cero.

## ▶️ Ejecución

Para ejecutar el programa es necesario tener Python instalado. Desde la terminal, dentro de la carpeta del proyecto, se utiliza:

```bash
python checkpoint.py
```

## 📁 Archivo

El proyecto contiene los siguientes archivos:

```text
checkpoint.py
checkpoint.pkl
```

* **`checkpoint.py`** contiene el código principal del programa.
* **`checkpoint.pkl`** es el archivo donde se guarda el estado de ejecución.

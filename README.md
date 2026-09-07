# 💾 Application Checkpointing

## Descripción

Este proyecto contiene un ejemplo de **Application Checkpointing** en Python. El programa procesa un total de 10 tareas y guarda automáticamente el progreso después de cada una.

Si el programa se detiene, el progreso queda guardado en un archivo y, al volver a ejecutarlo, el programa puede **restaurar el estado anterior y continuar desde la tarea donde se quedó**.

## 🔧 Herramientas utilizadas

El programa utiliza diferentes herramientas para guardar y restaurar el estado:

* **Pickle:** permite guardar y recuperar información de Python.
* **`pickle.dump()`:** guarda el estado actual en el archivo de checkpoint.
* **`pickle.load()`:** recupera el estado guardado.
* **`os.path.exists()`:** comprueba si existe un archivo de checkpoint.
* **`os.remove()`:** elimina el checkpoint cuando todas las tareas han sido completadas.
* **`time.sleep()`:** agrega una pausa de un segundo para simular el procesamiento de cada tarea.
* **`try - except`:** controla posibles errores al intentar cargar el checkpoint.
* **`while`:** permite procesar las tareas hasta completar las 10.

## 💻 Funcionamiento

Al ejecutar el programa, se comprueba si existe un checkpoint.

Si no existe, el programa comienza desde la primera tarea:

```text
=== APPLICATION CHECKPOINTING ===

Iniciando el programa desde cero...

Procesando tarea 1 de 10
Checkpoint guardado.

Presiona ENTER para continuar o escribe 's' para detener:
```

Después de cada tarea, el programa guarda el progreso en el archivo:

```text
checkpoint.pkl
```

Si el usuario decide detener el programa, el progreso queda guardado.

Al ejecutarlo nuevamente, el programa encuentra el checkpoint y continúa desde la tarea guardada:

```text
=== APPLICATION CHECKPOINTING ===

Checkpoint encontrado.
Restaurando estado...
Continuando desde la tarea: 5

Procesando tarea 5 de 10
Checkpoint guardado.
```

Cuando las 10 tareas terminan, el archivo de checkpoint se elimina porque ya no es necesario:

```text
Todas las tareas fueron completadas.
Checkpoint eliminado.
```

## ▶️ Ejecución

Para ejecutar el programa es necesario tener Python instalado. Desde la terminal, dentro de la carpeta del proyecto, se utiliza:

```bash
python checkpoint.py
```

Durante la ejecución se puede presionar **ENTER** para continuar con la siguiente tarea o escribir **`s`** para detener el programa y conservar el progreso.

## 📁 Archivos

El proyecto utiliza los siguientes archivos:

```text
checkpoint.py
checkpoint.pkl
```

* **`checkpoint.py`** contiene el código principal del programa.
* **`checkpoint.pkl`** se genera automáticamente y almacena el estado actual de la ejecución.

El archivo `checkpoint.pkl` se elimina automáticamente cuando todas las tareas han sido completadas.

# 🛠️ Application Checkpointing en Python

## Descripción

Este proyecto contiene un ejemplo de **Application Checkpointing**, una técnica que permite guardar el estado de un programa para poder recuperarlo posteriormente.

El programa simula el procesamiento de 10 tareas. Después de cada tarea se guarda un checkpoint con el progreso actual. Si el programa se detiene, al ejecutarlo nuevamente puede recuperar el último estado guardado y continuar desde ese punto.

## 🔧 Herramientas utilizadas

El programa utiliza diferentes herramientas para guardar y restaurar el estado:

- **Pickle:** permite guardar y recuperar el estado del programa.
- **Archivos:** se utiliza un archivo `.pkl` para almacenar el checkpoint.
- **OS:** comprueba si existe un checkpoint antes de intentar cargarlo.
- **Try - Except:** controla posibles errores al cargar el archivo.
- **While:** mantiene el procesamiento de las tareas.
- **Time:** agrega un pequeño tiempo de espera para simular el procesamiento.

## 💻 Funcionamiento

Al iniciar el programa por primera vez, comienza desde la primera tarea:

```text
=== APPLICATION CHECKPOINTING ===

Iniciando el programa desde cero...

Procesando tarea 1 de 10
Checkpoint guardado.

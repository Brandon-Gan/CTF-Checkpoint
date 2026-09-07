import pickle
import os
import time

ARCHIVO_CHECKPOINT = "checkpoint.pkl"
TOTAL_TAREAS = 10


def guardar_checkpoint(tarea_actual):
    estado = {
        "tarea_actual": tarea_actual
    }

    with open(ARCHIVO_CHECKPOINT, "wb") as archivo:
        pickle.dump(estado, archivo)

    print("Checkpoint guardado.")


def cargar_checkpoint():
    if os.path.exists(ARCHIVO_CHECKPOINT):
        try:
            with open(ARCHIVO_CHECKPOINT, "rb") as archivo:
                estado = pickle.load(archivo)

            print("Checkpoint encontrado.")
            return estado["tarea_actual"]

        except (pickle.PickleError, EOFError, KeyError):
            print("No se pudo cargar el checkpoint.")

    return 1


print("=== APPLICATION CHECKPOINTING ===")
print()

tarea = cargar_checkpoint()

if tarea == 1:
    print("Iniciando el programa desde cero...")
else:
    print("Restaurando estado...")
    print("Continuando desde la tarea:", tarea)

print()

while tarea <= TOTAL_TAREAS:

    print("Procesando tarea", tarea, "de", TOTAL_TAREAS)
    time.sleep(1)

    guardar_checkpoint(tarea + 1)

    print()

    opcion = input("Presiona ENTER para continuar o escribe 's' para detener: ")

    if opcion.lower() == "s":
        print("Programa detenido.")
        print("El progreso ha sido guardado.")
        break

    tarea += 1

if tarea > TOTAL_TAREAS:
    print("Todas las tareas fueron completadas.")

    if os.path.exists(ARCHIVO_CHECKPOINT):
        os.remove(ARCHIVO_CHECKPOINT)

    print("Checkpoint eliminado.")
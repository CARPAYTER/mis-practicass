from collections import deque
import time
cola_reproduccion=deque()
#AGREGAR ELEMENTOS DE REPRODUCCION
cola_reproduccion.append("1.-Mochila azul")
cola_reproduccion.append("2.-Aerolinea carrillo")
cola_reproduccion.append("3.-La calabaza")
#MOSTRAR LAS CANCIONES EN ESPERA
print("Canciones en espera:")
for cancion in cola_reproduccion:
    print("_",cancion)
    print("INICIANDO REPRODUCCION")
    #DESENCOLAR
    while cola_reproduccion:
        cancion_actual=cola_reproduccion.popleft()
        print(f"Sonando ahora :{cancion_actual}")
        time.sleep(1)#SIMULA LA DURACION DEL TEMA
        print(f"Finalizo: {cancion_actual}")
        #MUESTRA CUANTAS CANCIONES QUERAN EN LA COLA
        print(f"(Quedan{len(cola_reproduccion)}canciones en la cola)")
        print("La cola de reproduccion ha finalizado")
from collections import deque
cola=deque()
#AGREGAR ELEMENTOS
cola.append("Cliente1")
cola.append("Cliente2")
cola.append("Cliente3")
#SACAR EL PRIMER 
atendido=cola.popleft()
#MOSTRAR RESULTADOS
print("Atendido",atendido)
print("Cola restante",cola)
pila = []
print ()
print("Pila creada:", pila)

for i in range(1, 11):
    pila.append(f"Plato {i}")

print("\nSe agregaron los 10 platos:")
print(pila)

if pila:
    print("\nEl plato que esta arriba del todo es:", pila[-1])

print("\nQuitando 4 platos de la pila:")
for i in range(4):
    quitado = pila.pop()
    print("Se saco:", quitado)

print("Como quedo la pila:", pila)

cantidad = len(pila)
vacia = (cantidad == 0)

print("\nCantidad de platos que quedan:", cantidad)
print("¿La pila esta vacia?:", vacia)

print("\nVaciando lo que queda de la pila:")
while len(pila) > 0:
    print("Quitando:", pila.pop())

print("\nPila final:", pila)
print("¿Ahora si quedo vacia?:", len(pila) == 0)
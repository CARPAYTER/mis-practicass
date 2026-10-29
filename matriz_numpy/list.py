import numpy as ap
A= np.array([1,2],[3,4])
B= np.array([5,6],[7,8])
#Suma de elementos
print ("--Suma A+B--")
print(Suma)
#Multiplicacion de elementos
prod_elem=A*B
print("--Multiplicacion AxB--")
print(prod_elem)
#Producto matricial
prod_mat=A@B 
print("--Productos Matricial")
print(prod_mat)
#Transpuesta
transpuesta=A.T 
print("--Transpuesta de A")
print(transpuesta)
#Determinante e inversa
det=np.linalg.det(A)
inv=np.linalg.det(B)
print("DETERMINANTE DE A")
print(det)
print("INVERSA DE A")
print(inv)
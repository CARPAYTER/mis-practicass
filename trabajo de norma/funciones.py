import datetime
def saludar():
    print("Hola , Bienvenidos")
    saludar()


 def mostrar_hora():
        hora_actual=datetime.detetime.now().strftime("%H:%M:%S")
        print(f"La hora actual es :{hora_actual}")
        mostrar_hora()

        
def calcular_area_triangulo(base,altura):
            area=(base*altura)/2
            return area
        resultado=calcular_area_triangulo(10,5)
        print(f"EL area del triangulo es:{resultado }")

 def saludar_persona(nombre,edad):
            print(f"Hola {nombre } , tienes{edad} años")
            saludar_persona("jhonatan",19)


            #--------------------------------------------------------------
         #sin parametros
  def Bienvenida():
                print("hola , bienvenidos al programa") 
                Bienvenida()

 import datetime
 def mostrar_hora():
     hora_actual = datetime.datetime.now().strftime("%H:%M:%S")
    print (f"La hora actual es:{hora_actual}")
     mostrar_hora

#con parametros
def calcular_area_triangulo(base,altura):
    area = base * altura
    return area

resultado = calcular_area_triangulo(10,5)
print(f"El area es:{resultado} ")

def saludar_persona(nombre,apellido):
    print(f"hola:{nombre} , apelli{apellido} es")
    saludar_persona("jhonatan" , "islas")


class circulo():
    def __init__(self, radio):
          self.radio = radio
  
    def obtener_perimetro(self):
         return float(self.radio) * 2 * 3.14 
    def obtener_area(self):
         return float(self.radio)**2 * 3.14 
    def obtener_volumen(self):
         return float(self.radio)**3 * 4 * 3.14 / 3
    
ncirculos=int(input("cuantos circulos desea: "))
circulolist=[]

for i in range(ncirculos):
   circulo1=circulo(float(input("introduzca el radio del circulo numero "+str(i+1)+": ")))

for x in range(ncirculos):
  resultado=circulo1.obtener_perimetro()
  print("del circulo numero "+str(x+1)+":")
  print(resultado)
  resultado1= circulo1.obtener_area()
  print("area del circulo numero "+str(x+1)+":")
  print(resultado1)
  resultado2= circulo1.obtener_volumen()
  print("volumen del circulo numero "+str(x+1)+":")
  print(resultado2)
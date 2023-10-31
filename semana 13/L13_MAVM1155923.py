class circulo():
    def __init__(self, radio):
          self.radio = radio
  
    def obtener_perimetro(self):
         return float(self.radio) * 2 * 3.14 
    def obtener_area(self):
         return float(self.radio)**2 * 3.14 
    def obtener_volumen(self):
         return float(self.radio)**3 * 4 * 3.14 / 3
    
circulo1=circulo(10)

resultado=circulo1.obtener_perimetro()
print(resultado)
resultado1= circulo1.obtener_area()
print(resultado1)
resultado2= circulo1.obtener_volumen()
print(resultado2)
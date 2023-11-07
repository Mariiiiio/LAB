class Automovil():
 def __init__(self):
    self.modelo= 0
    self.precio= 0.0
    self.marca= ""
    self.disponible= True
    self.tipocambio= 0.0
    self.descuentoAplicado=0.12

 def def_modelo(self, modelo):
  self.modelo = int(modelo)

 def def_precio(self, precio):
  self.precio = float(precio)
 
 def def_modelo(self, marca):
  self.marca = str(marca)

 def def_cambio(self, tipocambio):
  self.tipocambio = float(tipocambio)
  tipocambio= self.precio * tipocambio

 def camb_disponibilidad(self):
  if self.disponible == True:
   self.disponible=False
  elif self.disponible == False:
    self.disponible=True

 def mostr_disponibilidad(self):
  if self.disponible == True:
   print("Disponible")
  elif self.disponible == False:
   print("No Disponible")

 def descuento(self):
  return self.precio*self.descuentoAplicado
 
 def mostrar_inf(self):
  print("Marca: " + str(self.marca) + "Modelo: " + int(self.modelo) + "Precio de venta: Q" + float(self.precio) + "Precio en dolares: " + float(self.tipocambio))
  print("disponibilidad: " + Automovil.mostr_disponibilidad)

Automovil1= Automovil()
Automovil1.def_modelo("2007")
Automovil1.def_precio(3000.0)
Automovil1.def_cambio(7.7)

print(Automovil1.mostrar_inf())

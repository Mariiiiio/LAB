
filas = 10
columnas = 11

tablero1 = [[" O " for _ in range(columnas)] for _ in range(filas)]
tablero2 = [[" O " for _ in range(columnas)] for _ in range(filas)]

barcos = {
    'Barco Pequeño 1': 3,
    'Barco Pequeño 2': 3,
    'Barco Pequeño 3': 3,
    'Barco Grande 1': 5,
    'Barco Grande 2': 5
}
Letras="ABCDEFGHIJ"
Letras_m="KLMNÑOPQRSTXWYZ"

def mostrar_tablero(tablero):
    print('      1  2  3  4  5  6  7  8  9  10')
    for i in range(filas):
        fila = "".join(tablero[i])
        print(chr(65 + i) + ' ' + fila)

while True:
 try:

  def colocar_barco(tablero, fila, columna, tamaño, orientación):

    if orientación == "H":
        for i in range(tamaño):
             if tablero[Letras.index(fila)][columna + i] == " O ":
                tablero[Letras.index(fila)][columna + i] = "🚢 "
             else:
                raise ValueError

    elif orientación == "V":
        for i in range(tamaño):
            if tablero[Letras.index(fila) + i][columna] == " O ":
               tablero[Letras.index(fila) + i][columna] = "🚢 "
            else:
               raise ValueError
        
    else:
        print("coordenada no valida")

  print("Jugador 1")
  x=colocar_barco(tablero1, str(input("En que fila quiere colocar el barco pequeño 1: ")), 
                int(input("En que columna quiere colocar el barco pequeño 1: ")), 
                3, input("Quiere colocar el barco pequeño 1 horizontal (H) o vertical(V): "))

  mostrar_tablero(tablero1)
  x1=colocar_barco(tablero1, str(input("En que fila quiere colocar el barco pequeño 2: ")), 
                 int(input("En que columna quiere colocar el barco pequeño 2: ")), 
                 3, input("Quiere colocar el barco pequeño 2 horizontal (H) o vertical(V): "))
  mostrar_tablero(tablero1)
  x2=colocar_barco(tablero1, str(input("En que fila quiere colocar el barco pequeño 3: ")), 
                 int(input("En que columna quiere colocar el barco pequeño 3: ")), 
                 3, input("Quiere colocar el barco pequeño 3 horizontal (H) o vertical(V): "))
  mostrar_tablero(tablero1)
  x3=colocar_barco(tablero1, str(input("En que fila quiere colocar el barco grande 1: ")), 
                 int(input("En que columna quiere colocar el barco grande 1: ")), 
                 5, input("Quiere colocar el barco grande 1 horizontal (H) o vertical(V): "))
  mostrar_tablero(tablero1)
  x4=colocar_barco(tablero1, str(input("En que fila quiere colocar el barco grande 2: ")), 
                 int(input("En que columna quiere colocar el barco grande 2: ")), 
                 5, input("Quiere colocar el barco grande 2 horizontal (H) o vertical(V): "))
  mostrar_tablero(tablero1)
  break
 except (IndexError, ValueError):
    print("coordenada no valida, comienza de nuevo")
    
while True:
 try:
   print("Jugador 2")
   y=colocar_barco(tablero2, str(input("En que fila quiere colocar el barco pequeño 1: ")), 
                int(input("En que columna quiere colocar el barco pequeño 1: ")), 
                3, input("Quiere colocar el barco pequeño 1 horizontal (H) o vertical(V): "))

   mostrar_tablero(tablero2)
   y1=colocar_barco(tablero2, str(input("En que fila quiere colocar el barco pequeño 2: ")), 
                 int(input("En que columna quiere colocar el barco pequeño 2: ")), 
                 3, input("Quiere colocar el barco pequeño 2 horizontal (H) o vertical(V): "))
   mostrar_tablero(tablero2)
   y2=colocar_barco(tablero2, str(input("En que fila quiere colocar el barco pequeño 3: ")), 
                 int(input("En que columna quiere colocar el barco pequeño 3: ")), 
                 3, input("Quiere colocar el barco pequeño 3 horizontal (H) o vertical(V): "))
   mostrar_tablero(tablero2)
   y3=colocar_barco(tablero2, str(input("En que fila quiere colocar el barco grande 1: ")), 
                 int(input("En que columna quiere colocar el barco grande 1: ")), 
                 5, input("Quiere colocar el barco grande 1 horizontal (H) o vertical(V): "))
   mostrar_tablero(tablero2)
   y4=colocar_barco(tablero2, str(input("En que fila quiere colocar el barco grande 2: ")), 
                 int(input("En que columna quiere colocar el barco grande 2: ")), 
                 5, input("Quiere colocar el barco grande 2 horizontal (H) o vertical(V): "))
   mostrar_tablero(tablero2)
   break
 except (IndexError, ValueError):
    print("coordenada no valida")

while True:
 try:
  def disparar(tablero, fila, columna):
    if tablero[Letras.index(fila)][columna] == "🚢 ":
        tablero[Letras.index(fila)][columna] = "💥 "
        print("Le diste al Barco!")
    elif tablero[Letras.index(fila)][columna] == " O ":
        tablero[Letras.index(fila)][columna] = "🌊 " 
        print("Disparo al Agua")
    else:
        print("ya habias disparado aqui")
    
  print("Turno de Jugador 1")
  disparar(tablero2, str(input("En que fila desea disparar: ")),
          int(input("En que columna desea disparar: ")))
  
  print("Turno de Jugador 2")
  disparar(tablero1, str(input("En que fila desea disparar: ")),
          int(input("En que columna desea disparar: ")))
  
  def ganador(tablero):
    for fila in tablero:
        if "🚢 " in fila:
            return False
    return True
  
  if ganador(tablero2):
     print("Ganador: jugador 1")
     print("tablero 1")
     mostrar_tablero(tablero1)
     print("tablero 2")
     mostrar_tablero(tablero2)
     break
  elif ganador(tablero1):
     print("Ganador: jugador 2")
     print("tablero 1")
     mostrar_tablero(tablero1)
     print("tablero 2")
     mostrar_tablero(tablero2)
     break
  
  
 except (IndexError, ValueError):
    print("coordenada no valida")

   
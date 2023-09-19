
print("Ejercicio")
print("desea ingresar a la calculadora")
print("si o no")
z = input()
while z == "si":
  print("ingrese primer numero")
  n1 = input()
  print("ingrese segundo numero")
  n2 = input()
  n1=int(n1)
  n2=int(n2)
  print("elija la operacion a utilizar")
  print("1: suma")
  print("2: resta")
  print("3: multiplicacion")
  print("4: division")
  print("5: modulo")
  print("6: cociente")
  print("7: exponente")
  print("8: salir")
  op = input()
  op=int(op)

  

  suma= n1 + n2
  resta= n1 - n2
  multi= n1 * n2
  div= n1 / n2
  modul= n1 % n2
  cociente= n1 // n2
  exponente= n1 ** n2

  if op == 1:
    print( str(n1) +"+"+ str(n2) +"="+ str(suma))
  if op == 2:
    print( str(n1) +"-"+ str(n2) +"="+ str(resta))
  if op == 3:
    print( str(n1) +"*"+ str(n2) +"="+ str(multi))
  if op == 4:
    print( str(n1) +"/"+ str(n2) +"="+ str(div))
  if op == 5:
    print( str(n1) +"%"+ str(n2) +"="+ str(modul))
  if op == 6:
    print( str(n1) +"//"+ str(n2) +"="+ str(cociente))
  if op == 7:
    print( str(n1) +"**"+ str(n2) +"="+ str(exponente))
  if op == 8:
    print("Adios")
    break
  elif op >  8: 
    print("ese numero no esta en las opciones")



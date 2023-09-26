
while True:
 print("Menu:")
 print("1. factorial")
 print("2. Secuencia de Fibonacci")
 print("3. salir")
 r=input()
 r=int(r)

 if r == 1:
  print("ingrese un numero")
  n1=input()
  n1=int(n1)
  factorial=1
  factorial=int(factorial)

  for i in range(1, n1+1):
    factorial=factorial*i
  print(str(n1)+"*...*2*1= "+str(factorial))

 elif r == 2:
  x=0
  y=1
  z=0
  print("ingrese un numero")
  n2=input(":")
  n2=int(n2)

 print(str(x)+", "+str(y)+", ",end=" ") 
 for s in range(0,n2):
   z=x+y
   print(str(z)+", ",end=" ") 
   x=y
   y=z
 print("Fibonacci: ("+str(n2)+")")

 if r == 3:
  break
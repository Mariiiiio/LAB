caracteres = input("Ingresa una cadena de caracteres: ")

unos = 0
ceros = 0
otros = 0

for x in caracteres:
    if x == '1':
        unos += 1
    elif x == '0':
        ceros += 1
    else:
        otros += 1

print("Cantidad 0: " + str(ceros))        
print("Cantidad 1: " + str(unos))
print("Otros caracteres: " + str(otros))
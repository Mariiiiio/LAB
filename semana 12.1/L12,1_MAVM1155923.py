class Calculadora:
    def __init__(self):
        self.num1 = 0.0
        self.num2 = 0.0

    def insertar_numero1(self, num):
        self.num1 = num

    def insertar_numero2(self, num):
        self.num2 = num

    def ob_suma(self):
        return self.num1 + self.num2

    def ob_resta(self):
        return self.num1 - self.num2

    def ob_multiplicacion(self):
        return self.num1 * self.num2

    def ob_division(self):
        if self.num2 != 0:
            return self.num1 / self.num2
        else:
            return "No se puede dividir entre cero"

calcu = Calculadora()

while True:
    print("Menú:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

    op = input("Elija una opción: ")

    if op == '1':
        num1 = float(input("Ingrese el primer numero: "))
        num2 = float(input("Ingrese el segundo numero: "))
        calcu.insertar_numero1(num1)
        calcu.insertar_numero2(num2)
        resultado = calcu.ob_suma()
        print("La suma es: ", resultado)
    elif op == '2':
        num1 = float(input("Ingrese el primer numero: "))
        num2 = float(input("Ingrese el segundo numero: "))
        calcu.insertar_numero1(num1)
        calcu.insertar_numero2(num2)
        resultado = calcu.ob_resta()
        print("La resta es: ", resultado)
    elif op == '3':
        num1 = float(input("Ingrese el primer numero: "))
        num2 = float(input("Ingrese el segundo numero: "))
        calcu.insertar_numero1(num1)
        calcu.insertar_numero2(num2)
        resultado = calcu.ob_multiplicacion()
        print("La multiplicación es:", resultado)
    elif op == '4':
        num1 = float(input("Ingrese el primer numero: "))
        num2 = float(input("Ingrese el segundo numero: "))
        calcu.insertar_numero1(num1)
        calcu.insertar_numero2(num2)
        resultado = calcu.ob_division()
        print("La división es: ", resultado)
    elif op == '5':
        print("Adiooooos!")
        break
    else:
        print("Esa opcion no es valida")

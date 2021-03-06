ej10_emayor.py                                                                                      0000644 0001750 0001751 00000001311 14216246710 013115  0                                                                                                    ustar   emayor                          emayor                                                                                                                                                                                                                 lista = ["Daniel", "Juan", "David", "Jorge", "Martin", "Marcos"]
letra = ""

def buscarNombre(lista,letra):
    resultado = list()
    long = len(lista)
    for i in lista:
        if letra in i[0]:
            resultado.append(i)
    return resultado

# Mientras el usuario no ingrese '0', el programa admitirá la entrada de cualquier letra
while letra != '0':
    letra = input("Ingrese una letra (D, J, M). Ingrese 0 para continuar\n> ")
    if letra != '0':
        resultado = buscarNombre(lista,letra)
        if resultado != []:
            for i in resultado:
                print(i)
        else:
            print(f"No se han encontrado nombres que empiezen con {letra}")




                                                                                                                                                                                                                                                                                                                       ej1_emayor.py                                                                                       0000644 0001750 0001751 00000001356 14216005001 013030  0                                                                                                    ustar   emayor                          emayor                                                                                                                                                                                                                 # Diseñar un programa que, dados dos números enteros, muestre por pantalla uno de los siguientes mensajes,
# dependiendo de la verificación de la condición que corresponda.
# El segundo es el cuadrado exacto del primero.
# El segundo es menor que el cuadrado del primero.
# El segundo es mayor que el cuadrado del primero.

# LECTURA DE DATOS
a = int(input('Ingrese un número A\n> '))
b = int(input('Ingrese un número B\n> '))

# VERIFICACION DE DATOS E IMPRESIÓN DEL MENSAJE
if (a*a) == b:
    print("El segundo número es el cuadrado exacto del primero")
else:
    if (a*a) > b:
        print("El segundo es menor que el cuadrado del primero.")
    else:
        print("El segundo es mayor que el cuadrado del primero.")

                                                                                                                                                                                                                                                                                  ej2_emayor.py                                                                                       0000644 0001750 0001751 00000001310 14216150561 013033  0                                                                                                    ustar   emayor                          emayor                                                                                                                                                                                                                 # Escribir un programa que permita evaluar el polinomio x^4 + x^3 + 2x^2 − x. 
# Luego, escribir otro programa que solicite valores de x por teclado y calcule
# el valor del polinomio para ellos, mostrando el resultado. Es importante 
# tener en cuenta cuál es la modularización adecuada del problema y cuál sería 
# el criterio de parada al ingreso de datos.

# Devolver resultado de x^4 + x^3 + 2x^2 − x
def EvaluarPolinomio(x):
    return x**4 + x**3 + 2*(x*x) - x

def LeerDatos():
    valor = float(input('> '))
    return valor

print("Ingrese un valor para X")
x = LeerDatos()
resultado = EvaluarPolinomio(x)
print(f"({x} ^ 4) + ({x} ^ 3) + (2 * {x} ^ 2) - {x} = {resultado}")

                                                                                                                                                                                                                                                                                                                        ej3_emayor.py                                                                                       0000644 0001750 0001751 00000002550 14216213603 013040  0                                                                                                    ustar   emayor                          emayor                                                                                                                                                                                                                 # Realizar un programa que calcule el desglose en billetes y monedas de una cantidad exacta de euros. Hay billetes
# de 500, 200, 100, 50, 20, 10 y 5 € y monedas de 2 y 1 €.
# Siempre se debe dar el menor número de billetes posibles (para 100€ entregaría un único billete, no diez de 10€)     

# SOLUCIÓN:
# Usamos división exacta (//) para calcular la cantidad de billetes/monedas con la que nos podemos acercar, comenzando
# por el de 500 y siguiendo en orden "decreciente" hasta el 2. Luego de cada división tomamos el monto original y 
# nos quedamos con el resto de la misma división que hicimos y probamos con otra nominación.
# Si ya no es divisible por 2, entonces quedará usar monedas de 1 para representar la cantidad restante. 

nominaciones = (500, 200, 100, 50, 20, 10, 5, 2, 1)

def ContarBilletes(monto):
    billetes = [0] * 9
    for n in nominaciones[:7]:
        cuenta = monto // n
        if (cuenta) > 0:
            billetes[nominaciones.index(n)]+=cuenta
            monto = monto % n
    billetes[8] = monto
    return billetes                                                           

monto = int(input('Ingrese un monto\n> '))
resultado = ContarBilletes(monto)
for i in range(0,9):
    if resultado[i] > 0:
        print(f"Billetes de €{nominaciones[i]}: {resultado[i]}")

        
    
            


                                                                                                                                                        ej4_emayor.py                                                                                       0000644 0001750 0001751 00000002460 14216660036 013047  0                                                                                                    ustar   emayor                          emayor                                                                                                                                                                                                                 # Ejercicio 4
# Diseñar una función que reciba los tres coeficientes de una ecuación de segundo grado, y devuelva una lista con
# sus soluciones reales.
# Si la ecuación sólo tiene una solución real, devuelve una lista con dos copias de la misma. Si no tiene solución real
# alguna o si tiene infinitas soluciones, devuelve una lista con dos copias del valor None. asdalskdjlaksjdlkajsldkjalskdjalskjdlaksjdlaksjdlkajsldkajsdlkjasldk

from math import sqrt

# Función original usando try/except para manejar el error de meter un número sdasdasd
# negativo en sqrt

# def baskhara(a, b, c):
#     try:
#         delta = sqrt((b*b)-(4*a*c))
#         x1 = (-b+delta)/(2*a)
#         x2 = (-b-delta)/(2*a)
#     except: 
#         x1 = None
#         x2 = None
#     return (x1, x2)

# Función alternativa que usa cosas que ya usamos

def baskhara(a, b, c):
    delta = (b*b)-(4*a*c)
    if delta >= 0:
        delta = sqrt(delta)
        x1 = (-b+delta)/(2*a)
        x2 = (-b-delta)/(2*a)
    else:
        x1 = None
        x2 = None
    return (x1, x2)


a = float(input("Ingrese un número para A \n> "))
b = float(input("Ingrese un número para B \n> ")) 
c = float(input("Ingrese un número para C \n> "))

raices = baskhara(a, b, c)

print(f"Las raíces son {raices}")

                                                                                                                                                                                                                ej5_emayor.py                                                                                       0000644 0001750 0001751 00000002170 14216660034 013044  0                                                                                                    ustar   emayor                          emayor                                                                                                                                                                                                                 # Diseñar y escribir una función que determine si un número natural (entero mayor que 1) es o no primo.
# Luego escribir el programa que lea un número ingresado por teclado y, utilizando la función previamente escrita,
# determine si es primo o no. El algoritmo deberá continuar pidiendo números, hasta que el usuario ingrese un
# número 0. En ese caso, se debe confirmar la salida del programa, dando al usuario la posibilidad de seguir
# ingresando números.

from math import sqrt, floor

n = 1

# Se decide verificar n % i == 0 hasta que i sea el entero más cercano por izquierda de la raíz cuadrada del número.

def esPrimo(n):
    for i in range(2,1+floor(sqrt(n))):
        # print(str(i)+', ',end='')
        if (n % i == 0):
            return False
    return True

while n != 0:
    n = int(input("Ingrese un número mayor a 1 (0 para salir)\n> "))
    if n != 0:
        if n <= 1:
            print("El número debe ser mayor a 1!")
        else:
            if esPrimo(n):
                print("El número ES primo!")
            else: 
                print("El número NO ES primo!")
                                                                                                                                                                                                                                                                                                                                                                                                           ej6_emayor.py                                                                                       0000644 0001750 0001751 00000001365 14216247567 013066  0                                                                                                    ustar   emayor                          emayor                                                                                                                                                                                                                 # Una palabra es alfabética si todas sus letras están 
# ordenadas alfabéticamente. Por ejemplo: amor, chino e himno
# son palabras alfabéticas. Diseñar un programa que 
# lea una palabra y nos diga si es alfabética o no.

# Se convierte la palabra en lista y se la ordena. sorted() es "case-sensitive". Las palabras
# que comienzan en mayúscula son menores en orden que las minúsculas (por ASCII)

def esAlfabetica(palabra):
    palabra_lista = list(palabra)
    palabra_ord = sorted(list(palabra))
    if palabra_ord == palabra_lista:
        return True
    return False

palabra = input("Ingrese una palabra\n> ")
if esAlfabetica(palabra):
    print("La palabra es alfabética")
else:
    print("La palabra no es alfabética")                                                                                                                                                                                                                                                                           ej7_emayor.py                                                                                       0000644 0001750 0001751 00000004304 14216252027 013046  0                                                                                                    ustar   emayor                          emayor                                                                                                                                                                                                                 # Una de las técnicas de criptografía más rudimentarias consiste en sustituir cada uno de los caracteres del alfabeto
# por otro situado n posiciones más a la derecha. Si n = 2, por ejemplo, sustituiremos la a por la c, la b por la d, y así
# sucesivamente. El problema que aparece en las últimas n letras del alfabeto tiene fácil solución: en el ejemplo, la
# letra y se sustituirá por la a y la letra z por la b. La sustitución debe aplicarse a las letras minúsculas y mayúsculas
# y a los dígitos. Diseñar un programa que lea un texto y el valor de n y muestre su versión criptográfica.

# (<caracter-a-codificar> + <valor-clave> - <inicio-de-caracteres>) % <cantidad-de-caracteres> + <inicio-de-caracteres>
# Al caracter original se le suma el valor de la llave "z" y luego se le resta el código del primer caracter
# de su secuencia (la sucesión de letras o números en la tabla ASCII; el primer elemento
# tiene representación decimal 48 para digitos, 65 para letras mayúsculas y 97 para minúsculas)
# El resultado es la "distancia" del caracter en cuestion respecto del primero.
# Se divide esto entre la cantidad de caracteres de la secuencia (26 para letras, 10 para números), 
# ya que si la cuenta anterior es mayor a 26 (o a 10), el caracter resultante estaría fuera de rango
# El resto de esta division, más el valor del primer caracter, nos devuelve el caracter codificado. 

def encriptar(cadena,clave):
    long = len(cadena)
    cadenaSalida = ""
    for i in range(long):
        char = cadena[i]
        char_code = ord(char)
        # SI ES UN NÚMERO...
        if char_code in range(48,58):
            cadenaSalida += chr((char_code + clave - 48) % 10 + 48)
        # SI ES MAYÚSCULA...
        elif char.isupper():
            cadenaSalida += chr((char_code + clave - 65) % 26 + 65)
        # SI ES UN ESPACIO
        elif char_code == 32:
            cadenaSalida += " "
        # SI ES MINÚSCULA...
        else:
            cadenaSalida += chr((char_code + clave - 97) % 26 + 97)
    return cadenaSalida

texto = input("Ingrese una frase\n> ")
clave = int(input("Ingrese un número para codificar la frase\n> "))
resultado = encriptar(texto,clave)
print(f"Texto encriptado: {resultado}")



                                                                                                                                                                                                                                                                                                                            ej8_emayor.py                                                                                       0000644 0001750 0001751 00000001725 14216250546 013057  0                                                                                                    ustar   emayor                          emayor                                                                                                                                                                                                                 # La función para desencriptar es similar a la de encriptar. En lugar de 
# añadir la clave se sustrae...

def desencriptar(cadena,clave):
    long = len(cadena)
    cadenaSalida = ""
    for i in range(long):
        char = cadena[i]
        char_code = ord(char)
        # SI ES UN NÚMERO...
        if char_code in range(48,58):
            cadenaSalida += chr((char_code - clave - 48) % 10 + 48)
        # SI ES MAYÚSCULA...
        elif char.isupper():
            cadenaSalida += chr((char_code - clave - 65) % 26 + 65)
        # SI ES UN ESPACIO
        elif char_code == 32:
            cadenaSalida += " "
        # SI ES MINÚSCULA...
        else:
            cadenaSalida += chr((char_code - clave - 97) % 26 + 97)
    return cadenaSalida

texto = input("Ingrese una frase codificada\n> ")
clave = int(input("Ingrese la clave para decodificar la frase\n> "))
resultado = desencriptar(texto,clave)
print(f"Texto desencriptado: {resultado}")                                           ej9_emayor.py                                                                                       0000644 0001750 0001751 00000001214 14216230673 013050  0                                                                                                    ustar   emayor                          emayor                                                                                                                                                                                                                 lista = list()
palabra = ""

# Se calcula la cantidad de elementos, se ordena la lista y 
# se devuelven el elemento del primer índice y del último
def primerUlt(lista):
    long = len(lista)
    lista.sort()
    return (lista[0],lista[long-1])

# Mientras el usuario no ingrese '0', el programa admitirá la 
# entrada de una cantidad indefinida de elementos
while palabra != '0':
    palabra = input("Ingrese una palabra. Ingrese 0 para continuar\n> ")
    if palabra != '0':
        lista.append(palabra)

# Se obtiene el resultado y se imprime
resultado = primerUlt(lista)
print(f"Primera y última palabra: {resultado}")
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
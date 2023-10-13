### Bucles ###

# 1. Ejercicio: Imprime los números del 1 al 10 usando un bucle for.
print("BUCLES")
print("Ejercicio 1")
numeros = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
for dieznumeros in numeros:
    print(dieznumeros, end=" ")

# otra forma#
print()
print("Ejercicio1.1")
numeros = range(10)
for dieznumeros in numeros:
    print(dieznumeros+1, end=" ")

# otra forma#
print()
print("Ejercicio 1.2")
numeros = range(1, 11)
for dieznumeros in numeros:
    print(dieznumeros, end=" ")


# 2. Ejercicio: Imprime los números pares del 1 al 20 usando un bucle while.
print()
print("Ejercicio 2")
numeros_1 = 1
while numeros_1 <= 20:
    if numeros_1 % 2 == 0:
        print(numeros_1, end=" ")
    numeros_1 += 1

# 3. Ejercicio: Usa un bucle para calcular la suma de los números del 1 al 100.

print()
print("Ejercicio 3")

i = 1
j = 100

x = range(i, j+1)
suma = 0

for y in x:
    suma += y

print("La suma es:", suma)

### FUNCIONES ###

# 1. Ejercicio: Define una función que tome dos números y retorne su suma.

print("FUNCIONES")
print("Ejercicio 1")


def suma(a, b):
    return a+b


resultado = suma(2, 5)
print(resultado)

# 2. Ejercicio: Define una función que tome un número y retorne su factorial.
print()
print("Ejercicio 2.1")


def factorial(n):
    result = 1
    for c in range(1, n + 1):
        result = result * c
    return result


print(factorial(5))

print()
print("Ejercicio 2.2")


def factorial(n):
    result = 1
    while n >= 1:
        result = result * n
        n = n - 1
    return result


n = 5
print(factorial(n))

# 3. Ejercicio: Define una función que tome un número y determine si es primo.
print()
print("Ejercicio 3")


def primo(value):
    if (value == 1):
        return False
    for i in range(2, value+1):
        if (value % i == 0 and value != i):
            return False
    return True


n = 4
if primo(n):
    print(n, " Si es un numero primo")
else:
    print(n, "No es un numero primo")


# 4. Ejercicio: Define una función que reciba una lista de números y retorne la suma de ellos.
print()
print("Ejercicio 4")


def sumatorio(list_numeros):
    sumatorio_total = 0
    for numeros in list_numeros:
        sumatorio_total += numeros
    return sumatorio_total


list_numeros = ([4, 5, 2, 3])
print(sumatorio(list_numeros))


# 5. Ejercicio: Define una función que reciba una cadena de texto y retorne la cadena en reversa
print()
print("Ejercicio 5")


def cadena_reversa(cadena):
    return cadena[::-1]


cadena = "otro ejercicio de python"
print(cadena_reversa(cadena))

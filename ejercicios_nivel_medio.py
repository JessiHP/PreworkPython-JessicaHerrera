#1. Ejercicio: Define una función que utilice un bucle para imprimir los primeros n números de la serie de Fibonacci.
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
n = 10
print(f"El numero {n} de la serie de Fibonacci es {fib(n)}")

#2. Ejercicio: Define una función que tome un número y retorne una lista de su divisores.
def divisor(n):
    x = list ()
    for c in range (1,n):
        if n%c ==0:
            x.append(c)
    return x
               
b = 12
print ("Los divisores de" ,(b), "son",divisor(b))

#3. Ejercicio: Define una función que tome una lista y retorne una nueva lista con los elementos únicos de la lista original.
def unico(entrylist):
    outputlist = list ()
    valorvalido=True
    for indexc, c in enumerate(entrylist, start=0):
        
        for indexd, d in enumerate(entrylist, start=0):    
            if indexc==indexd:
                valorvalido=True
            elif entrylist[indexc]!=entrylist[indexd]:
                valorvalido=True
            elif entrylist[indexc]==entrylist[indexd]:
                valorvalido=False
                break
        if valorvalido==True:
            outputlist.append(c)
    return outputlist        


a=['agua','tomate','agua','peras','aguacate','aguacate']
b=[3,4,5,2,4,5,2]

print("Valores unicos de la lista" ,(a),"=",unico(a))


#4. Ejercicio: Define una función que tome un número y retorne la suma de sus dígitos.
def sumdig(n):
    x = list(str(n))
    result = 0
    for c in x:
        result = result + int(c)
    return result

a = 4567
print("La suma de los digitos de",(a), "es",sumdig(a))

#5. Ejercicio: Define una función que tome una cadena y cuente el número de vocales en la cadena.
def findvowels(cadena:str):
    vowels = list("aeiouAEIOU")
    sumvowels=0
    for c in vowels:
        sumvowels= sumvowels + cadena.count(c)
    return sumvowels

cadena = ('hola paraiso verde natural')
print("El numero de vocales en '",(cadena),"' es",findvowels(cadena))

#6. Ejercicio: Define una función que tome una lista y un número n, y retorne los primeros n elementos de la lista.
def firstn (lista:list,n:int):
    index=0
    sublista = list()
    for element in lista:
        if index==n:
            break
        if index!=n:
            sublista.append(element)
        index=index+1
    return sublista

n = 2
lista = ["papas",4,3,5,"libros"]
print ("Los primeros elementos de ",(lista),"son",firstn(lista,n))
#7. Ejercicio: Define una función que tome una cadena y retorne la cantidad de letras mayúsculas y minúsculas en la cadena.
def mayusminusletter(cadena:str):
    upperletter=0
    lowerletter=0
    for element in cadena:
            upperletter= upperletter + str.isupper(element)
            lowerletter= lowerletter + str.islower(element)
    return (upperletter,lowerletter)

cadena= "hOLa amiGos"
countletter=mayusminusletter(cadena)
countmayuscula=countletter [0]
countminuscula=countletter [1]
print("El numero de mayusculas en mi cadena", (cadena),"son",(countmayuscula))
print("El numero de minusculas en mi cadena", (cadena),"son",(countminuscula))

#Otra forma##
def mayusminusletter(cadena:str):
    upperletter=0
    lowerletter=0
    for element in cadena:
        if str.isupper(element):
            upperletter=upperletter +1
        if str.islower(element):
            lowerletter=lowerletter + 1
    return (upperletter,lowerletter)

cadena= "BueNOS Dias"
countletter=mayusminusletter(cadena)
countmayuscula=countletter [0]
countminuscula=countletter [1]
print("El numero de mayusculas en mi cadena", (cadena),"son",(countmayuscula))
print("El numero de minusculas en mi cadena", (cadena),"son",(countminuscula))

#8. Ejercicio: Define una función que tome un número y retorne True si es un número perfecto, False en caso contrario. Un número perfecto es aquel que es igual a la suma de sus divisores propios positivos. Por ejemplo, 6 es un número perfecto porque sus divisores son 1, 2 y 3, y 6 = 1 + 2 + 3.

#9. Ejercicio: Define una función que reciba un número y retorne su representación en binario.
#10. Ejercicio: Define una función que reciba dos listas y retorne la intersección de ambas (los elementos que están en las dos listas).
#11. Ejercicio: Define una función que tome una cadena y determine si es un palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda).
#12. Ejercicio: Escribe un programa que imprima los números del 1 al 50, pero para múltiplos de tres imprima “Fizz” en lugar del número y para los múltiplos de cinco imprima “Buzz”. Para números que son múltiplos de tanto tres como cinco imprima “FizzBuzz”.
#13. Ejercicio: Define una función que tome una lista y retorne la lista ordenada en orden ascendente.
#14. Ejercicio: Define una función que reciba una lista de palabras y un entero n, y retorne la lista de palabras que son más largas que n.
#15. Ejercicio: Define una función que tome un número y calcule su serie de Fibonacci.
#16. Ejercicio: Define una función que tome una lista de números y retorne el número más grande de la lista.
#17. Ejercicio: Define una función que reciba un número y retorne la suma de sus dígitos al cubo.
#18. Ejercicio: Define una función que reciba una lista de números y retorne el segundo número más grande de la lista.
#19. Ejercicio: Define una función que tome dos listas y retorne True si tienen al menos un miembro en común, de lo contrario, retorne False.
#20. Ejercicio: Define una función que tome una lista y retorne una nueva lista con los elementos de la lista original en orden inverso.
#21. Ejercicio: Define una función que reciba una cadena y cuente el número de dígitos y letras que contiene.
#22. Ejercicio: Define una función que reciba una lista de números y retorne la suma acumulada de los números
#23. Ejercicio: Define una función que encuentre el elemento más común en una lista.
#24. Ejercicio: Define una función que tome un número y retorne un diccionario con la tabla de multiplicar de ese número del 1 al 10.
#25. Ejercicio: Define una función que tome una cadena y retorne un diccionario con la cantidad de apariciones de cada caracter en la cadena.
#26. Ejercicio: Define una función que tome dos listas y retorne la lista de elementos que no están en ambas listas.
#27. Ejercicio: Define una función que tome una lista y retorne la lista sin duplicados.
#28. Ejercicio: Define una función que reciba un número entero positivo y retorne la suma de los cuadrados de todos los números pares menores o iguales a esenúmero.
#29. Ejercicio: Define una función que reciba una lista de números y retorne el promedio de los números en la lista.
#30. Ejercicio: Define una función que reciba una lista de cadenas y retorne la cadena más larga en la lista.
#31. Ejercicio: Define una función que reciba un número entero n y retorne una lista con los n primeros números primos.
#32. Ejercicio: Define una función que reciba una cadena y retorne la misma cadena pero con las palabras en orden inverso.
#33. Ejercicio: Escribe una función que reciba una lista de tuplas y retorne una lista ordenada basada en el último elemento de cada tupla.
#34. Ejercicio: Define una función que reciba una cadena y retorne la cantidad de letras vocales en la cadena.
#35. Ejercicio: Define una función que reciba un número entero y retorne True si es un número primo, de lo contrario retorne False.
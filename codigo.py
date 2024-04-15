# """
# Ejercicio 1: Suma de Dos Números
# Descripción: Este ejercicio consiste en crear una función que reciba dos números como argumentos y devuelva la suma de ambos.
# """

def sumar(a, b):
    # Escribe aqui el return de la suma de 2 numeros
    resp = a+b
    return resp

# """
# Ejercicio 2: Factorial de un Número
# Descripción: En este ejercicio se requiere crear una función que calcule el factorial de un número dado. El factorial de un número nn se calcula como n!=n×(n−1)×(n−2)×…×1n!=n×(n−1)×(n−2)×…×1.
# """
    
def factorial(n):
    if n == 0:
        # Escribe aqui el return de la operacion anterior
        return 1
    else:
        # Escribe aqui el return de la operacion contraria a la operacion anterior
        return n * factorial(n-1)

# """
# Ejercicio 3: Contar Vocales en una Cadena
# Descripción: En este ejercicio se debe implementar una función que cuente el número de vocales (mayúsculas y minúsculas) en una cadena de texto dada.
# """
    
def contar_vocales(cadena):
    vocales = 'aeiouAEIOU'
    contador = 0
    for letra in cadena:
        if letra in vocales:
            # Escribe aqui el contador de vocales
            contador = contador + 1
    return contador

# """
# Ejercicio 4: Verificar Palíndromo
# Descripción: En este ejercicio se debe implementar una función que verifique si una cadena de texto dada es un palíndromo, es decir, si se lee igual de izquierda a derecha que de derecha a izquierda.
# """

def es_palindromo(cadena):
    # Escribe aqui el return de la cadena al reves con una funcion de python
    return cadena == cadena[::-1]

# """
# Ejercicio 5: Suma de Elementos de una Lista
# Descripción: En este ejercicio se debe crear una función que calcule la suma de todos los elementos de una lista dada.
# """

def suma_lista(lista):
    # Escribe aqui el return de la suma de todos los elementos de la lista
    suma = 0
    for elemento in lista:
        suma += elemento
    return suma

if __name__ == "__main__":
    print(sumar(2,3))
    print(factorial(0))
    print(contar_vocales("Parangaricutirimicuaro"))
    print(es_palindromo("radar"))
    print(suma_lista([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
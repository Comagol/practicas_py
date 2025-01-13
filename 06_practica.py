"""
Recursividad
"""

# Recursividad: Es una funcion que se llama a ella misma
#Importante saber cuando usar un bucle y cuando una funcion recursiva
#def hello():
#    hello()
    
#hello() bucle infinito


#Crea una funcion que cuente de 100 a 0
# No es el mejor uso de una forma recursiva
def uncount(number : int):
    if number >= 0:
        print(number)
        uncount(number - 1)

#uncount(100)

"""
Extra
"""

# Usar funciones recursivas en lugar de bucles cuando una funcion se pueda acabar dividiendo en otros subproblemas, tienen tomas de decisiones segun una variable. cuando podemos descomponer problemas. Cuando entender el bucle sea mas complejo.

def numero_factorial (number : int) -> int:
    if number < 0:
        return 0
    elif number == 0:
        return 1
    else:  
        return number * numero_factorial(number-1)
    
print(numero_factorial(5))

# Calcular el valor de un elemento concreto (segun su posicion) en la sucecion de Fibonacci (la funcion recibe la posicion)

def fibonacci (number : int) -> int:
    if number <= 0:
        print("Los numeros negativos no son validos")
        return 0
    elif number == 1:
        return 0
    elif number == 2:
        return 1
    else:
        return fibonacci(number - 1) + fibonacci(number - 2)

print(fibonacci(10))
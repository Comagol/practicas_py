"""
OPERADORES
"""

# Operadores Aritméticos
print(f"Suma: 10 + 3 = {10+3}")
print(f"Resta: 10 - 3 = {10-3}")
print(f"Multiplicacion: 10 * 3 = {10*3}")
print(f"division: 10 / 3 = {10/3}")
print(f"Modulo: 10 % 3 = {10%3}")
print(f"Exponente: 10 ** 3 = {10**3}")
print(f"Division entera: 10 // 3 = {10//3}")

# Operadores de Comparacion
print(f"Igualdad: 10 == 3 es {10 == 3}")
print(f"Desigualdad: 10 != 3 es {10!=3}")
print(f"Mayor que: 10 > 3 es {10>3}")
print(f"Menor que: 10 < 3 es {10<3}")
print(f"Mayor o igual que: 10 >= 3 es {10>=3}")
print(f"Menor o igual que: 10 >= 3 es {10<=3}")

# Operadores Logicos
print(f"AND &&: 10 +3 == 13 and 5 - 1 == 4 es {10+3==13 and 5-1 == 4}")
print(f"OR ||: 10 +3 == 14 or 5 - 1 == 4 es {10+3==14 or 5-1 == 4}")
print(f"NOT !: not 10 + 3 == 14 es {not 10 + 3 == 14}")

# Operadores de Asignacion
my_number = 11 #asignacion 
print(my_number)
my_number += 1 #suma y asignacion
print(my_number)
my_number -= 1 #resta y asignacion
print(my_number)
my_number *= 2 #multiplicacion y asignacion
print(my_number)
my_number /= 2 #division y asignacion
print(my_number)
my_number %= 3 #modulo y asignacion
print(my_number)
my_number **= 2 #exponente y asignacion
print(my_number)
my_number //= 2 #division entera y asignacion
print(my_number)

# Operadores de Identidad
my_new_number = my_number
print(f"my_number is my_new_number es {my_number is my_new_number}")
print(f"my_number is my_new_number es {my_number is not my_new_number}")

# Operadores de Pertenencia
print(f"'f' in 'francisco' = {'f' in 'francisco'}")
print(f"'h' in 'francisco' = {'h' not in 'francisco'}")

"""
Estructuras de control
"""

# Condicionales

my_string = "FranComabella"

if my_string == "FranComabella":
    print("my string es 'FranComabella'")
elif my_string == "Comagol":
    print("my string es 'Comagol'")
else:
    print("my string no es 'FranComabella'")

# Iterativas

for i in range(11):
    print(i)

i = 0

while i <= 10:
    print(f"i vale: {i}")
    i += 1

# Manejo de Excepciones
try:
    print(10/10)
except:
    print("se ha producido un error")
finally:
    print("Ha finalizado el manejo de excepciones")

"""
# EJERCICIO
"""
"""Crea un programa que imprima por consula todos los numeros comprendidos entre el 10 y el 55 (incluidos), pares y que no son ni el 16 ni multiplos de 3."""

for number in range (10, 56):
    if number % 2 == 0 and number != 16 and number % 3 != 0:
        print(number)
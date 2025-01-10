"""
FUNCIONES DEFINIDAS POR EL USUARIO
"""

# Funciones Simples

def greet():
    print("Hola, Phyton!")
    
greet()

# Funcion con Retorno

def return_greet():
    return "Hola, Fran!"

print(return_greet())

# Funcion con Argumento

def arg_greet(name):
    print(f"Hola, {name}")
    
arg_greet("Francisco")

# Funcion con Argumentos

def arg_greet(name, age):
    print(f"Hola {name} tienes {age} años.")
    
arg_greet("Francisco", 27)

# Funcion con Argumento Predeterminado

def arg_greet(name = "Franco"):
    print(f"Hola, {name}")
    
arg_greet("sin el predeterminado")
arg_greet()

# Con Argumentos y Return

def return_args_greet(greet, name):
    return f"{greet}, {name}!"

print(return_args_greet("Hi", "Comabella"))

# Con Retorno de Varios Valores

def multiple_return_greet():
    return "Hola", "Python"

greet, name = multiple_return_greet()
print(f"{greet}, {name}")


# Con un numero variable de argumentos

def variable_arg_greet(*names):
    for name in names:
        print(f"Hola {name}, mucho gusto!")

variable_arg_greet("Fran", "Naza", "Chula")

# Con un numero de variables de argumentos con palabra clave

def variable_key_arg_greet(**names):
    for key, value in names.items():
        print(f"Hola {value} ({key}), mucho gusto!")

variable_key_arg_greet(
    language="Phyton", 
    name="Fran", 
    alias="Pachu",
    age=27
)


"""
Funciones dentro de funciones
"""

def outer_function():
    def inner_function():
        print("Funcion interna")
    inner_function()
    
outer_function()


"""
Funciones del lenguaje (built in)
"""

print(len("Comabella Francisco"))
print(type("Comabella Francisco"))
print("Francisco Comabella".upper())


"""
Variables globales y locales
"""

global_var = "Python"

def hello_python():
    local_var = "hola"
    print(f"{local_var}, {global_var}")
    
    
print(global_var)
#print(local_var)   no funciona porque la variable esta definida dentro de la funcion, su scope es dentro de la funcion
hello_python()



"""
Extra
"""

def print_numbers(text_1, text_2) -> int:
    count = 0
    for number in range (1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print(f"{text_1} {text_2}")
        elif number % 3 == 0:
            print(text_1)
        elif number % 5 ==0:
            print(text_2)
        else:
            print(number)
            count += 1
    return count
        
print(print_numbers("texto 1", "texto 2"))
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

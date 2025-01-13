"""
Valor y Referencia
"""

#Tipos de datos por valor

my_int_a = 10
my_int_b = 20
my_int_b = my_int_a
print(my_int_a)
print(my_int_b)


# Tipos de datos por referncia
#El concepto de variable por referencia, heredan su posicion de memoria. por eso se muestran por consola los mismos valores, porque son el mismo espacio de memoria

my_list_a = [10, 20]
#my_list_b = [30,40]
my_list_b = my_list_a
my_list_b.append(30)
print(my_list_a)
print(my_list_b)


# Funciones con datos por valor
my_int_c = 10
def my_int_func(my_int_c : int):
    my_int_c = 20
    print(my_int_c)

my_int_func(my_int_c)
print(my_int_c)

# Funcione con datos por referencia, como comparten el mismo espacio de memoria tienen los mismos valores en cada espacio de memoria 

my_list_c = [10, 20]

def my_list_func(my_list: list):
    my_list.append(30)
    my_list_d = my_list
    my_list_d.append(40)
    print(my_list)
    print(my_list_d)

print(my_list_c)
my_list_func(my_list_c)
print(my_list_c)


"""
Extra
"""

#Por valor

def value(value_a : int , value_b : int):
    temp = value_a
    value_a = value_b
    value_b = temp
    return value_a, value_b

my_int_d = 10
my_int_e = 20
my_int_f, my_int_g = value(my_int_d, my_int_e)

print(f"{my_int_d}, {my_int_e}")
print(f"{my_int_f}, {my_int_g}")

#Por referencia, aca si podemos porque agregamos el temp para guardar info (y no perderla) un nuevo lugar en memoria.

def ref(value_a : list , value_b : list) -> tuple:
    temp = value_a
    value_a = value_b
    value_b = temp
    return value_a, value_b

my_list_e = [10,20]
my_list_f = [30,40]
my_list_g, my_list_h = value(my_list_e, my_list_f)
print(f"{my_list_e}, {my_list_f}")
print(f"{my_list_g}, {my_list_h}")
#Listas
#Las listas guardan datos de forma ordenada

my_list = ["Francisco", "Comabella", "Nazarena", "Chula"]
print(my_list)
my_list.append("Javier") #Append agrega un valor al final de la lista
print(my_list)
my_list.remove("Comabella")#.Remove elimina si es exactamente igual lo que le pasamos, tipo de dato y valor
print(my_list)
my_list[1] #Asi accedemos a una posicion en especifico de una lista(comienza a contar desde el 0)
print(my_list[1])
my_list[1] = "Naza" #Actualizamos el valor de la posicion 1
print(my_list)
my_list.sort() # El sort ordena la lista, en este caso alfabeticamente
print(my_list)


#Tuplas
# Las tuplas son inmutables (muy segura). se usan para estructuras de datos que sean inmutables
my_tuple = ("Francisco", "Comabella", "Pachu" , 41)
print(my_tuple[2]) # solo podemos acceder a las pocisiones


# Sets
# Son estructuras desordenadas, son buenas para almacenar datos pero no para buscarlos
my_set = {"Francisco", "Comabella", "Pachu" , "41"}
print(my_set)
my_set.add("comabellafran@gmail.com") #Insertamos un dato
print(my_set)
my_set.add("comabellafran@gmail.com") #Insertamos el mismo dato, pero no lo inserta porque ya esta presente el mismo dato
print(my_set)
my_set.remove("Comabella") #Eliminacion de un dato
print(my_set)
print(type(my_set))


"""
DICCIONARIO
"""
# los datos que se guardan son clave valor ("clave" : "valor")
# los dicionarios por definicion no son ordenados, por lo tanto no podemos ingresar a ubicaciones especificas (En python lo muestra ordenado, pero no es una estructura ordenada)


my_dict : dict = { 
   "name" :"francisco" , "last_name" : "comabella",
    "age" : "25", "surname" : "Coma"                
} 

my_dict["email"] = "comabellafra@hotmail.com" # Insercion de dato
print(my_dict["email"]) # Acceso
my_dict["name"] = "Javier" #Actualizacion de dato, si no existe el campo name lo acaba creando e insertando
print(my_dict)
del my_dict["last_name"] #Eliminacion con la operacion reservada del
print(my_dict)
my_dict = dict(sorted(my_dict.items())) #Ordenacion, pero hay que volver a convertirlo en un diccionario y pasarle la funcion .items
print(my_dict)

"""
Extra
"""

def my_agenda():
    
    agenda = {}
    
    while True:
    
        print("")
        print("1. Buscar Contacto")
        print("2. Insertar Contacto")
        print("3. Actualizar Contacto")
        print("4. Eliminar Contacto")
        print("5. Salir")

        option = input("\nSelecciona una opcion: ")
        
        match option:
            case "1":
                name = input("Introduce el nombre del contacto que quieres buscar: ")
                if name in agenda: 
                    print(f"El numero de telefono de {name} es {agenda[name]}")
                else :
                    print(f"El contacto {name}, no existe en la agenda")
                pass
            case "2":
                name = input("introduce el nombre del contacto:")
                phone = input("introduce el telefono del contacto:")
                if phone.isdigit() and len(phone) > 0 and len(phone) <= 11:
                    agenda [name] = phone
                    print(agenda)
                else:
                    print("Debes ingresar un numero de telefono con un maximo de 11 caracteres")
                pass
            case "3":
                name = input("Introduce el nombre del contacto para luego modificar su numero de telefono:")
                if name in agenda:
                    phone = input("Ingrese el numero de telefono: ")
                    if phone.isdigit() and len(phone) > 0 and len(phone) <= 11:
                        agenda [name] = phone
                        print(f"El numero de telefono de {name} es {phone}")
                    else:
                        print("Debes ingresar un numero de telefono con un maximo de 11 caracteres")
                else:
                    print("Debes ingresar un nombre que se encuentre en la agenda")
                pass
            case "4":
                name = input("Introduce el nombre del contacto que quieres eliminar: ")
                if name in agenda:
                    del agenda [name]
                else:
                    print(f"El contacto {name}, no existe")
                pass
            case "5":
                print("Saliendo de la agenda.")
                break
            case _:
                print("Opcion no valida, elige una opcion del 1 al 5.")
my_agenda()


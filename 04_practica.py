"""
Operaciones
"""

s1 = "Hola"
s2 = "Francisco"

# Concatenacion
print(s1 + " " +  s2)

# Repeticion
print(s1*3)

# Indexacion y concatenacion de indices
print(s1[0] + s1[1] + s1[2] + s1[3])

#longitud de una cadena de texto
print(len(s2))

#Slicing 
print(s2[0:4])
print(s2[2:])
print(s2[:4])

# Busqueda
print("F" in s2)
print("u" in s2)

# Reemplazo
print(s1.replace("o" , "a"))

#division / split
print(s2.split("n"))

# Mayusculas y minusculas

print(s1.upper())
print(s2.lower())
s3 = "francisco javier comabella"
print(s3.title())
print(s3.capitalize())

# Eliminacion de espacios al principio y al final
print(" hoola mundooo   ".strip())

# Busqueda al principio y al final
print(s1.startswith("Ho"))
print(s1.startswith("ho"))
print(s2.endswith("co"))

#busqueda en posicion casesensitive
print(s3.find("javier"))
print(s3.find("c"))

# Busqueda de ocurrencias
print(s3.count("a"))

s4="Python"
# Formateo de una cadena de texto
print("Saludo: {}, lenguaje: {}!".format(s1, s4))

# Interpolacion
print(f"saludo: {s1}, lenguaje: {s4}!")

# Transformacion de listas en caracteres
print(list(s3))

# Transformacion de listas en cadenas
l1 = [s1+ ", "  + s2 + "!"]
print("".join(l1))

# Transformaciones numericas
s5= "123456"
s5 = int(s5)
print(s5)

s6= "123456.5"
s6 = float(s6)
print(s6)

"""
Extra
"""

def check( word1: str, word2: str):

    #Palindromos
    print(f"¿{word1} es un palindromo?: {word1 == word1[::-1]}")
    print(f"¿{word2} es un palindromo?: {word2 == word2[::-1]}")
    
    #Anagrama
    print(f"¿{word1} es un anagrama de {word2}?: {sorted(word1)  == sorted(word2)}")
    
    #Isogramas
    #print(f"¿{word1} es un isograma?: {len(word1) == len(set(word1))}")
    #print(f"¿{word2} es un isograma?: {len(word2) == len(set(word2))}")
    
    def isogram(word:str) -> bool:
        
        word_dict = dict()
        for character in word2:
            word_dict[character] = word_dict.get(character,0) +1
            
        isogram = True
        values = list(word_dict.values())
        isogram_len = values[0]
        for word_count in values:
            if word_count != isogram_len:
                isogram = False
                break
        return isogram

    print(f"¿{word1} es un isograma?: {len(word1) == len(set(word1))}")
    print(f"¿{word2} es un isograma?: {len(word2) == len(set(word2))}")
        
check("neuquen", "phyton")
#check("amor", "roma")
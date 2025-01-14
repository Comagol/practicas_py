"""
Pilas y Colas
"""

"""
Ejercicio
"""
# Pila/Stack (LIFO LAST IN FIRST OUT) en python una lista es una pila
stack = []
stack.append("1") #push
stack.append("2")
stack.append("3")
stack.pop() #pop

print(stack)


# Cola/queue (FIFO first in first out)
queue = []
#enqueue
queue.append("1")
queue.append("2")
queue.append("3")
#dequeue
queue.pop(0)
print(queue)

"""
Extra
"""

#Web

def web_navigation():
    stack = []
    
    while True :
        action = input(
            "añade un URL o interactua con las palabras adelante/atras/salir: "
        )
        
        if action == "salir":
            print("Saliendo del navegador web.")
            break
        elif action == "adelante":
            pass
        elif action == "atras":
            if len(stack) >0:
                stack.pop()
        else:
            stack.append(action)
        if len(stack) > 0:
            print(f"Has navegado a la web: {stack[len(stack)-1]}.")
        else:
            print("Estas en la pagina principal")

#web_navigation()


def shared_printed():
    queue = []
    while True :
        
        action = input("Añade un documento a la cola o selecciona imprimir / salir: ")
        if action == "salir":
            break
        elif action == "imprimir":
            if len(queue) > 0:
                print(f"Imprimiendo: {queue.pop(0)}")
        else:
            queue.append(action)
        
        print(f"Cola de impresion: {queue}")
    
shared_printed()
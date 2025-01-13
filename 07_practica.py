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


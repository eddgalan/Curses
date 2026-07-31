from collections import deque


def manage_delivery_queue() -> deque:
    # Crea una cola para gestionar entregas de productos
    delivery_queue = deque(['order_1', 'order_2', 'order_3'])
    delivery_queue.append('order_4')    # Agrega otro elemento al final de la cola
    delivery_queue.appendleft('order_0')    # Agrega un elemento al inicio de la cola
    return delivery_queue

queue = manage_delivery_queue()
print(queue)

queue.pop()
print(queue)

queue.popleft()
print(queue)

from enum import Enum
from wsgiref.util import request_uri


class OrderStatus(Enum):
    PENDING = 1
    SHIPPED = 2
    DELIVERED = 3


def check_order_status(status: OrderStatus):
    # Comprueba el estado del pedido y devuelve un mensaje
    if status == OrderStatus.PENDING:
        return "Order is still pending"
    elif status == OrderStatus.SHIPPED:
        return "Order has ben shipped"
    elif status == OrderStatus.DELIVERED:
        return "Order has been delivered"


print(check_order_status(OrderStatus.SHIPPED))
print(check_order_status(OrderStatus.PENDING))
print(check_order_status(OrderStatus.DELIVERED))
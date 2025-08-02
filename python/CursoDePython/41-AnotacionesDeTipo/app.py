from employee import Employee


def add_employee_ids(id1: int, id2: int) -> int:
    return id1 + id2


# IDs Empleados
id1_: int = 10
id2_: int = 20

print(add_employee_ids(id1_, id2_))


employee1 = Employee("Juan", 28, 2000)
print(employee1.introduce())
print(employee1)

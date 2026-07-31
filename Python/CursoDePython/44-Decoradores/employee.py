def check_access(func):
    def wrapper(employee):
        if employee.get("role") == "admin":
            return func(employee)
        else:
            print("You don't have access")

    return wrapper


@check_access
def delete_employee(employee):
    print(f"Employee {employee['name']} deleted")


admin = {"name": "Carlos", "role": "admin"}
user = {"name": "Juan", "role": "user"}

delete_employee(admin)
delete_employee(user)

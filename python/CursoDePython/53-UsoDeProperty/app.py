from employee import Employee

if __name__ == "__main__":
    employee = Employee("Edson", 40000)
    print(employee.salary)

    employee.salary = 50000
    print(employee.salary)

    #employee.salary = -10000

    del employee.salary

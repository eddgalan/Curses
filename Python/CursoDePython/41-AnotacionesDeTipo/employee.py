from typing import Optional, Union


class Employee:
    name: str
    age: int
    salary: float

    def __init__(self, name: str, age: int, salary: float):
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self) -> str:
        return f"Name: {self.name}"

    def introduce(self) -> str:
        """
        Generates an introduction string containing the name and age of the individual.

        :return: A string introducing the individual and specifying their name and age.
        :rtype: str
        """
        return f"Hi, my name is {self.name}, Im {self.age} years old"

    def find_employee(self, employee_ids: list[int], employee_id: int) -> Optional[int]:
        """
        Finds the given employee ID within a list of employee IDs.

        :param employee_ids: A list of integers representing existing employee IDs.
        :param employee_id: An integer representing the ID of the employee to find.
        :return: The employee ID if found within the list; otherwise, None.
        """
        if employee_id in employee_ids:
            return employee_id
        return None

    def process_salary(self, salary: Union[int, float]) -> float:
        """
        Processes the given salary by converting it to a floating-point number.

        :param salary: The input salary value to be processed.
        :type salary: Union[int, float]
        :return: The salary converted to a floating-point number.
        :rtype: float
        """
        return float(salary)
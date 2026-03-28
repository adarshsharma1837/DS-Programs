from abc import ABC, abstractmethod

# Abstract Base Class
class Employee(ABC):
    def __init__(self, emp_id, name, basic_salary):
        self.__emp_id = emp_id          # private
        self.__name = name              # private
        self._basic_salary = basic_salary  # protected

    # Encapsulation: Getters and Setters
    def get_emp_id(self):
        return self.__emp_id

    def get_name(self):
        return self.__name

    def get_basic_salary(self):
        return self._basic_salary

    def set_basic_salary(self, salary):
        self._basic_salary = salary

    @abstractmethod
    def calculate_salary(self):
        pass


# Derived Class: Permanent Employee
class PermanentEmployee(Employee):
    def __init__(self, emp_id, name, basic_salary, allowances):
        super().__init__(emp_id, name, basic_salary)
        self.__allowances = allowances

    def calculate_salary(self):
        return self.get_basic_salary() + self.__allowances


# Derived Class: Contract Employee
class ContractEmployee(Employee):
    def __init__(self, emp_id, name, hourly_rate, hours_worked):
        super().__init__(emp_id, name, 0)  # basic salary not used
        self.__hourly_rate = hourly_rate
        self.__hours_worked = hours_worked

    def calculate_salary(self):
        return self.__hourly_rate * self.__hours_worked


# Payroll System Class
class PayrollSystem:
    def __init__(self):
        self.__employees = []

    def add_employee(self, employee):
        self.__employees.append(employee)

    def display_payroll(self):
        for emp in self.__employees:
            print(f"Employee ID: {emp.get_emp_id()}")
            print(f"Name: {emp.get_name()}")
            print(f"Salary: {emp.calculate_salary()}")
            print("-" * 30)


# Main Program
if __name__ == "__main__":
    # Creating objects
    emp1 = PermanentEmployee(101, "Alice", 50000, 10000)
    emp2 = ContractEmployee(102, "Bob", 500, 160)

    # Runtime polymorphism: base class reference
    employees = [emp1, emp2]

    payroll = PayrollSystem()
    for emp in employees:
        payroll.add_employee(emp)

    payroll.display_payroll()
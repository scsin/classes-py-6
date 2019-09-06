import abc

class Department:
    def __init__(self, name, code):
        self.name = name
        self.code = code


class Employee(abc.ABC):
    @abc.abstractmethod
    def __init__(self, code, name, salary):
        self.code = code
        self.name = name
        self.salary = salary

    def calc_bonus(self):
        # p = Seller(9234, 'Sara', 1500)
        # print(p.get_sales())
        return (self.sales * 0.15)

    def get_hours(self):
        return 8


class Manager(Employee):
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary)
    
    def calc_bonus(self):
        print(self.salary * 0.15)
        return self.salary * 0.15
    
    @property
    def get_department(self):
        self.department = Department('managers', 1)
        return self.department.name

    @get_department.setter
    def set_department(self, value):
        self.department = value


class Seller(Manager):
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary)
        self.sales = 0

    @property
    def get_sales(self):
        return self.sales

    @get_sales.setter
    def put_sales(self, value):
        self.sales += value

    def get_hours(self):
        return 8

    @property
    def get_department(self):
        self.department = Department('sellers', 2)
        return self.department.name

    @get_department.setter
    def set_department(self, value):
        self.department = value

z = Manager(9234, 'Sara', 1500)
print(z.get_department)

y = Seller(9234, 'Sara', 1500)
print(y.get_department)

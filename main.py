

class Departament:
    def __init__(self, name, code):
        self.name = name
        self.code = code


class Employee:
    def __init__(self, code, name, salary):
        self.__code = code
        self.__name = name
        self.__salary = salary
    def calc_bonus(self):
        pass

    def get_hours(self):
        pass


class Manager(Employee):
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary)
        self._departament = Departament('managers', 1)
    
    def calc_bonus(self):
        print(self.salary * 0.15)
        return self.salary * 0.15
    
    @property
    def departament(self):
        return self._departament

    @departament.setter
    def set_departament(self, value):
        self._departament = value

class Seller(Manager):
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary)
        self._departament = Departament('sellers', 2)
        self.sales = 0

    def get_hours(self):
        return 6

    @property
    def departament(self):
        return self._departament

    @departament.setter
    def set_departament(self, value):
        self._departament = value

x = Departament('Vendas', 828179809234)

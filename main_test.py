

class Departament:
    def __init__(self, name, code):
        self.name = name
        self.code = code
 

class Employee:
    def __init__(self, code, name, salary):
        self.__code = code
        self.__name = name
        self.__salary = salary
        # print(code, name, salary)
    def calc_bonus(self):
        # print(self.sales * 0.15) # CLASS SELLER
        # return self.sales * 0.15
        pass

    def get_hours(self):
        pass


class Manager(Employee):
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary)
        self.departament = Departament('managers', 1)
        # print(Departament('managers', 1))
        
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
        self.departament = Departament('sellers', 2)
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
x.get_departament


# @classmethod (método de classe tem o escopo da classe e não da instância)
# método de instância consegue acessar o escopo da classe
# @staticmethod método estático não tem o escopo da classe


# class Departament:
#        # print(f'Departamento: {name} \nCódigo: {code}')
#     @property
#     def get_departament(self): # RETORNA O NOME DO DEPARTAMENTO
#         return self.name
#     @property
#     def set_departament(self, setNameD): # muda o nome do departamento para as classes Manager e Seller
#         self._setNameD = setNameD

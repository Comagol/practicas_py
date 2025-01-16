"""
Ejercicio Herencia y Poliformismo
"""
#Super clase

class Animal:
    
    def __init__(self, name: str):
        self.name = name
    
    def sound(self):
        pass
        
        
#subclase
        
class Dog(Animal):
    def sound(self):
        print("Guau")
        
class Cat(Animal):
    def sound(self):
        print("Miau")
        
def print_sound(animal: Animal):
    animal.sound()
        
my_animal = Animal("Animal")
my_animal.sound()
my_dog = Dog("coach")
my_dog.sound()
my_cat = Cat("michi")
my_cat.sound()

#Polimorfismo y herencia

my_animal = Animal("Animal")
print_sound(my_animal)
my_dog = Dog("coach")
print_sound(my_dog)
my_cat = Cat("michi")
print_sound(my_cat)

"""
Ejercicio Extra
"""

class Employee:
    
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name
        self.employees = []
        
    def add(self, employee):
        self.employees.append(employee)
        
    def print_employees(self):
        for employee in self.employees:
            print(employee.name)
        
        
class Manager(Employee):
    
    def coordinate_projects(self):
        print(f"{self.name} esta coordinando todos los proyectos de la empresa")
    
class ProjectManager(Employee):

    def __init__(self, id: int, name: str, project: str):
        super().__init__(id, name)
        self.project = project

    def coordinate_project(self):
        print(f"{self.name} está coordinando su proyecto.")

class Programer(Employee):
    
    def __init__(self, id: int, name: str, language: str):
        super().__init__(id, name)
        self.language = language

    def code(self):
        print(f"{self.name} está programando en {self.language}.")

    def add(self, employee: Employee):
        print(f"Un programador no tiene empleados a su cargo. {employee.name} no se añadirá.")
        
        
my_manager = Manager(1, "Francisco Comabella")
my_project_manager = ProjectManager(2, "Pachu", "proyecto 1")
my_project_manager2 = ProjectManager(3, "Javier", "proyecto 2")
my_programer = Programer(4, "control", "Python")
my_programer2 = Programer(5, "ashe", "SQL")
my_programer3 = Programer(6, "carlos", "C+")
my_programer4 = Programer(7, "marta", "Ruby")

my_manager.add(my_project_manager)
my_manager.add(my_project_manager2)

my_project_manager.add(my_programer)
my_project_manager.add(my_programer3)

my_project_manager2.add(my_programer2)
my_project_manager2.add(my_programer4)

my_programer.add(my_programer3)

my_programer.code()
my_project_manager.coordinate_project()
my_manager.coordinate_projects()
my_manager.print_employees()
my_project_manager.print_employees()
my_programer.print_employees()
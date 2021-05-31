from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def show(self):
        pass

class Manager(Employee):
    def show(self):
        print("present")

m = Manager()
m.show()
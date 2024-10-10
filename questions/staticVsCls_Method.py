# Python Class Methods: An Introduction
# In Python, classes are a way to define custom data types that can store data and define functions that can manipulate that data. One type of function that can be defined within a class is called a "method." In this blog post, we will explore what Python class methods are, why they are useful, and how to use them.

# What are Python Class Methods?
# A class method is a type of method that is bound to the class and not the instance of the class. In other words, it operates on the class as a whole, rather than on a specific instance of the class. Class methods are defined using the "@classmethod" decorator, followed by a function definition. The first argument of the function is always "cls," which represents the class itself.

class Employee:
    company = "Apple" # class variable
    
    def show(self):
        print(f"The name is {self.name} and company {self.company}")
    @classmethod
    def changeCompany(cls, newCompany):
        cls.company = newCompany

e = Employee()
e.name = "Danish"
e.show()
e.changeCompany("Tesla")
e.show()
print(Employee.company)


# staticmethod - Static methods in Python are methods that belong to a class rather than an instance of the class.
class Math:
  def __init__(self, num):
    self.num = num

  def addtonum(self, n):
    self.num = self.num +n
    
  @staticmethod
  def add(a, b):
      return a + b

# result = Math.add(1, 2)
# print(result) # Output: 3
a = Math(5)
print(a.num)
a.addtonum(6)
print(a.num)

print(Math.add(7, 2)) 
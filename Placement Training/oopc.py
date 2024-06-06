# Object creation using __init__ method
class Person:
    def __init__(self, name):
        self.name = name
    
    def say_hi(self):
        print("Hello Mr.", self.name)

p = Person("Venkat")
p.say_hi()
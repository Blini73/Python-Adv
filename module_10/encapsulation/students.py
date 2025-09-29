class Student:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_age(self):
        return self._age

    def set_age(self, age):
        self._age = age

student1 = Student("Alice" 12)

print("Name: ", student1.get_name())
student1.set_name("Bob")
print("Updated Name: ", student1.get_name())

print("Age: ", student1.get_age())
student1.set_age(15)
print("Updated age: ", student1.get_age())
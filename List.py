class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def update_information(self, name=None, age=None, address=None):
        if name:
            self.name = name
        if age:
            self.age = age
        if address:
            self.address = address

    def display_information(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Address:",self.address)

person1 = Person(name="Vimal Varghese", age=22, address="248-b vytilla")

print("Initial Information:")
person1.display_information()

person1.update_information(age=23, address="123-C Cherthala")

print("\nUpdated Information:")
person1.display_information()

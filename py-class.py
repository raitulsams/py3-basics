class MyClass:
    def __init__(self, name, age):
        self.nickname = name
        self.current_age = age

    def __str__(self):
        return self.nickname + " is " + str(self.current_age)


obj = MyClass("Rahim", 32)


# print(obj)

# inheritence concept

class Person:
    def __init__(self, name, age, skin_color, gotBrains):
        self.name = name
        self.age = age
        self.skin_color = skin_color
        self.gotBrains = gotBrains

    def brains(self):
        if self.gotBrains:
            return "He got brain :)"
        else:
            return "He does not got brain :("

    def __str__(self):
        return self.name + " is " + str(
            self.age) + " years old and his skin color is " + self.skin_color + "and " + self.brains()


student1 = Person("sams", 20, "brown", False)
print(student1)

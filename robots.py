## Object oriented programming


class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

ozzy = Dog("Ozzy", 2)

print(ozzy.name)

print(ozzy.age)


class Roboter:
    pass

#if __name__=="__main__":
 #   x = Roboter()
#    y = Roboter()
#    y2 = y
 #   print(y == y2)
 #   print(y == x)
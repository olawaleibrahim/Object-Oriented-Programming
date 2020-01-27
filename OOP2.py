class House:  # Creating our first class which also served as the parent class later in the discussion
    def permission(self):
        print(f'You have acres of land to build with')
        return ' '


class Bungalow(House):  # Inheritance:  creating a subclass to inherit the properties of the House class
    def __init__(self, colour, length, width, height): #the __init__ method also called the constructor method
        self.colour = colour
        self.length = length
        self.width = width
        self.height = height

    def structure(self, length, width, height):
        print(
            f'The house has {self.length}, {self.width}, {self.height} dimensions')
        return 'House completed'


class Storey(House):  # Inheritance:  a subclass to inherit the properties of the House class
    def __init__(self, colour, length, width, height, floors, stairs):
        self.colour = colour
        self.length = length
        self.width = width
        self.height = height
        self.floors = floors
        self.stairs = stairs

    def structure(self):
        print(
            f'The house has {self.length}, {self.width}, {self.height} dimensions with {self.floors} floors')
        return 'House completed'

    def stairs_type(self):
        print(f'Your chosen stair type is {self.stairs}')
        return ' '


house1 = House() #creating an object from our House class
print(house1.permission())

#OOP gives us the ability to create multiple objects from a single class without code repetition
storey1 = Storey('red', 34, 56, 76, 3, 'curly')         
storey2= Storey('white', 304, 126, 64, 7, 'straight')
storey3 = Storey('blue', 22, 56, 76, 1, 'wavy')

bungalow1 = Bungalow('white', 26, 89, 46)
bungalow2 = Bungalow('brown', 126, 49, 26)

print(storey1.colour)
print(storey1.structure())


print(bungalow1.colour)
print(bungalow1.structure(32, 45, 67))
print(storey1.stairs_type())
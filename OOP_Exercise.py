class House:
    
    '''
    Class to build a house
    '''

    def __init__(self, height, width, length, colour):  #defining the initializer/constructor method
        
        '''
        Takes in the dimensions for constructing the House
        args:: height of building
               width of the building
               length ` ` ` ` ` ` ` `
               colour ` ` ` ` ` ` ` `
        '''

        self.height = height
        self.width = width
        self.length = length
        self.colour = colour

    def info(self):

        '''
        Method to describe house info
        '''
        return f"This house has dimensions {self.length} * {self.width} * {self.height} and is coloured {self.colour}"

class Storey(House):

    def __init__(self, height, width, length, colour, rooms, storeys):

        #using the super() function to inherit the House methods
        
        super(Storey, self).__init__(height, width, length, colour)

        '''
        The init constructor takes in the number of storeys and rooms in the house
        '''

        self.rooms = rooms
        self.storeys = storeys

        assert isinstance(storeys, int), f'{storeys} should be an integer for number of storeys'

    def extra_info(self):

        return f"This storey building has {self.rooms} rooms and {self.storeys}"

class Bungalow(House):

    def __init__(self, height, width, length, colour, rooms):

        #using the super() function to inherit the House methods
        
        super(Bungalow, self).__init__(height, width, length, colour)

        '''
        The init constructor takes in the number of rooms in the bungalow
        '''

        self.rooms_ = rooms

    def extra_info(self):

        return f"This bungalow has {self.rooms_} rooms"


def see_info(building):

    '''
    Function to check the info of a building
    '''

    return building.extra_info()

if __name__ == "__main__":
    
    house1 = House(height=200, width=1200, length=2000, colour='red')
    bungalow1 = Bungalow(height=200, width=1200, length=2000, colour='blue', rooms=22)
    storey1 = Storey(300, 500, 1200, 'green', 5, 2)
    
    #print(house1)
    #print(bungalow1)
    #print(storey1)
    print(f"House1 previous colour is : {house1.colour}")
    house1.colour = 'white'
    print(f"House1 new colour is : {house1.colour}")
    print(bungalow1.colour)
    print(storey1.colour)
    print(house1.info())
    print(bungalow1.info())
    print(storey1.info())
    print(f"Before: {bungalow1.extra_info()}")
    bungalow1.rooms = 34
    print(f"After: {bungalow1.extra_info()}")

    print(see_info(bungalow1))
    print(see_info(storey1))
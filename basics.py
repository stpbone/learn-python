#----PART 1: Creating classes, defining attributes, creating functions to change attributes

# create a class for my BMC bike 
class my_bikes:
    name = 'BMC'
    color = 'black' # set attributes and attribute names
    version = 'roadracer SL01'
    year = '2011'

# create a function (method) to change the class attribute 'name'
    def change_name(self, new_name): # note that the first argument is self
     self.name = new_name # access the class attribute with the self keyword

# define the class  
bike = my_bikes()

# print details about the bike by using the .selector
print(bike.name)
print(bike.color)
print(bike.version)
print(bike.year)

# print the current object name 
print(bike.name)

# change the name using the change_name method
bike.change_name("Trek")
print(bike.name)

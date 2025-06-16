# class Human:
#     def __init__(self, n, o):           #Method
#         self.name = n                   # Properties
#         self.occupation = o             # Properties
#
#     def do_work(self):              # Method
#         if self.occupation == "tennis player":
#             print(f'{self.name} is a tennis player')
#         elif self.occupation == "Actor":
#             print(f'{self.name} is an actor')
#
#     def speaks(self):               # Method
#         print(f'{self.name} says, How are you ?')
#
# Tom = Human("Tom Cruise", "Actor")  # when we create instance of class then it will can the first init method
#
# Tom.do_work()
# Tom.speaks()
#
# maria = Human("Maria sharapova", "tennis player")
# maria.do_work()
# maria.speaks()

#-----------🎯 Challenge-----------
#------------Create a Car class with attributes and a display method-----------

class car:
    def __init__(self, model, brand, color, year):
        self.model = model
        self.brand = brand
        self.color = color
        self.year = year

    def display(self):
        print(f'The {self.brand} {self.model} is a {self.color} car, manufactured in {self.year}')

ci = car("City", "Honda", "White", 2022)
ci.display()

ci = car("Fortuner", "Toyota", "Black", 2021)
ci.display()

ci = car("Nexon EV", "Tata", "Blue", 2024)
ci.display()

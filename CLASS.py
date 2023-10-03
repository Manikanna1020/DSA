class Vehicle: 
    def __init__(self, make, model):     ####### init - initiate funcations 
        self.make = make
        self.model = model 
    def moves(self):
        print('Moves along')
    def get_make_model(self):
        print(f"I am a {self.make}, {self.model}.")

my_car = Vehicle('Audi', 'A8')

# print(my_car.make)
# print(my_car.model)

my_car.moves()
my_car. get_make_model( )

your_car = Vehicle('BMW', 'Q3')
your_car.get_make_model()
your_car.moves()

class Airplane(Vehicle):
    def moves(self):
        print('Flies along')
class Truck(Vehicle):
    def moves(self):
        print("Rumbles along")

kanna = Airplane('JET', 'PLANE')
madu = Truck('VOLVO','ASHOKLEYAND')

kanna.moves()
kanna.get_make_model()
madu.moves()
madu.get_make_model()
























# Q3) Create a class to represent Vehicle objects. Attributes that you may want to include:
# ● Make and model
# ● Colour
# ● Seating capacity
# ● Maximum speed
# Include __str__ method to print a summary of the Vehicle.
# Include rev_engine method to print the noise the vehicle makes (print(“VRRRMMMM!”) is a good
# approximation :P)

class Vehicles:
    '''
    docstring
    '''
    # CLASS VARIABLES -----

    # CONSTRUCTOR -----
    def __init__(self, make_and_model, colour, capacity, max_speed):
        # OBJECT VARIABLES / ATTRIBUTES -----
        self.make_and_model = make_and_model
        self.colour = colour
        self.capacity = capacity
        self.max_speed = max_speed
    
    # METHODS / ACTIONS on OBJECTS -----


    # METHODS / ACTIONS on CLASS VARIABLES -----
    # @classmethod

    # STATIC METHODS / ACTIONS NOT on objects/class -----
    @staticmethod
    def rev_engine():
        return "Vrooooooom!"

    # SPECIAL METHODS / ACTIONS on existing __dunder__ methods
    def __str__ (self):
        return f"This {self.make_and_model} is {self.colour}, holds {self.capacity} people and drives at a maximum of {self.max_speed}/kms per hour."


# ----- INSTANTIATE OBJECTS -----
car1 = Vehicles("VW Beetle", "Blue", 5, 150)
car2 = Vehicles("Mini Coupe", "Red", 5, 200)

# ----- INVOKE & RETURN-----
print(car1)
print(car2)
print(Vehicles.rev_engine())
print(car1.colour)
print(help(staticmethod))


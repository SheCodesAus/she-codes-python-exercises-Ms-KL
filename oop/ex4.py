# Q4) Bonus challenge!
# Adapt your Vehicle class to keep track of the amount of fuel available. 
# There are no parameters here, get creative and see if you can think of a suitable way to approach this problem. 
# Things to consider:
# ● It’s totally fine to make an assumption about consistent fuel consumption per km.
# ● The vehicle can also be refuelled (and the fuel tank obviously has a maximum capacity).
# ● Perhaps the user should be warned if they are nearing an empty fuel tank.


# https://carfromjapan.com/article/car-maintenance/everything-drivers-need-know-fuel-tank-capacity/
# https://www.budgetdirect.com.au/car-insurance/research/average-fuel-consumption-australia.html

class Vehicles:
    '''
    docstring
    '''
    # CLASS VARIABLES -----
    
    # CONSTRUCTOR -----
    def __init__(self, make_and_model, colour, capacity, max_speed, distance_travel, current_speed, current_fuel, fuel_tank_max):
        # OBJECT VARIABLES / ATTRIBUTES -----
        self.make_and_model = make_and_model
        self.colour = colour
        self.capacity = capacity
        self.max_speed = max_speed
        self.distance_travel = distance_travel
        self.current_speed = current_speed
        self.current_fuel = current_fuel
        self.fuel_tank_max = fuel_tank_max
        
    
    # METHODS / ACTIONS on OBJECTS -----
    
    def fuel_consumption(self):
        '''
        average fuel consumption = 11.1L per 100km / 0.111L per1km
        '''
        status = ""
        avg_consumption_pkm = 0.111
        consumption = self.distance_travel * avg_consumption_pkm
        self.current_fuel -= consumption

        if self.current_fuel < 0:
            self.current_fuel = 0 
            status = "try to "
            
        travel_statement = f"You {status}travel {self.distance_travel}kms. You now have {self.current_fuel}L of fuel. "
        warning = self.fuel_warning()
        return travel_statement + warning

    def fuel_warning(self):
        '''
        doc
        '''
        if self.current_fuel == 0:
            return f"Your tank is empty. Time to get help."
        elif self.current_fuel <= (self.fuel_tank_max * 0.1):
            return f"Warning! You only have {self.current_fuel}L left. Time to refuel."
        else:
            return f""

    def refuel(self):
        '''
        doc
        '''
        self.current_fuel = self.fuel_tank_max
        return f"Thanks for refuelling. You have {self.current_fuel}L of fuel."

    # STATIC METHODS / ACTIONS NOT on objects/class -----
    @staticmethod
    def rev_engine():
        return "Vrooooooom!"

    # SPECIAL METHODS / ACTIONS on existing __dunder__ methods
    def __str__ (self):
        return f"This {self.make_and_model} is {self.colour}, holds {self.capacity} people and drives at a maximum of {self.max_speed}/kms per hour."


# ----- INSTANTIATE OBJECTS -----
# make_and_model, colour, capacity, max_speed, 
# distance_travel, current_speed, current_fuel, fuel_tank_max
car1 = Vehicles("VW Beetle", "Blue", 5, 150, 200, 60, 40,45)
car2 = Vehicles("Mini Coupe", "Red", 5, 200, 100, 30, 2, 50)

# ----- INVOKE & RETURN-----
# print("       ")
# print(car1)
# print(car2)
# print(Vehicles.rev_engine())
# print(car1.colour)
# print(help(staticmethod))
print("       ")
print("  --------   ")
print(car2)
print(f"Current Fuel: {car2.current_fuel}L")
print(car2.fuel_consumption())
print(f"Current Fuel: {car2.current_fuel}L")
print(car2.fuel_warning())
print(car2.refuel())
print(f"Current Fuel: {car2.current_fuel}L")
print(car2.fuel_consumption())
print(f"Current Fuel: {car2.current_fuel}L")



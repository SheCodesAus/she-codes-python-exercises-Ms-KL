
fuel_tank_max = 45
low_fuel = fuel_tank_max * .1
current_fuel = 2
print(low_fuel)

if current_fuel <= low_fuel:
    print("Warning! Fuel at 10%. Time to fill the tank up.")
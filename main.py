def get_city_distance():
  print("Choose a destination from the list below:")
  cities = {"Andijon": 351, "Samarqand": 306, "Nukus": 1095}
  print("Available destinations from Tashkent:")
  for city, distance in cities.items():
    print(city, ":", distance, "km")
  city = input("Enter the destination city: ")
  distance = cities[city]
  return distance

def convert():
  global distance, speed
  distance = get_city_distance() * 0.621371
  speed = speed * 0.621371
  return distance, speed

def get_trip_time(distance, speed):
  time = distance/speed
  return time

def fuelcost():
  global fuel_cost, fuel_price
  fuel_cost = (distance / fuel_effiency) * fuel_price
  return fuel_cost

def totalcost(cost):
  total_cost = fuelcost() + (time * cost_hour)
  return total_cost

print("Welcome to the Rental Car Company Trip Planner!\n")
print("Let's plan your trip!")

distance = get_city_distance()

print("Do you want to use metric or imperial units?")
units = input("Enter 'm' for metric or 'i' for imperial: ").lower()


print("Choose a car from the list below:\n")
print("Matiz: 45 mpg, 144 km/h, $11.77 per hour")
print("Ferrari: 38.2 mpg, 330 km/h, $1,000 per hour")
print("BMW X6: 40 mpg, 250 km/h, $200 per hour\n")

car = input("Enter the car you want to rent (M for Matiz, F for Ferrari, B for BMW):").lower()

if car == "m":
  speed = 144
  fuel_effiency = 45
  cost_hour = 11.77
  print("You have chosen Matiz.")
elif car == "f":
  speed = 330
  fuel_effiency = 38.2
  cost_hour = 1000
  print("You have chosen Ferrari.")
elif car == "b":
  speed = 250
  fuel_effiency = 40
  cost_hour = 200
  print("You have chosen BMW X6.")    

if units == "i":
  convert()
print()

print("What is the price of fuel per liter?")
fuel_price = float(input())

print("How long do you have available in hours?")
available_time = int(input())
print()
time = int(get_trip_time(distance, speed))
print("The trip will take", time , "hours.")
if time < available_time:
  print("You have enough time for the trip.")
else:
  print("You do not have enough time for the trip.")
print()

print("The cost of fuel for the trip will be $", fuelcost())
print("The total cost of the trip will be $", totalcost(cost))
print("Have a safe trip!")






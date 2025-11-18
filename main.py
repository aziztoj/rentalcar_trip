def get_city_distance():
  print("Choose a destination from the list below:")
  cities = {"andijon": 351, "samarqand": 306, "nukus": 1095}
  print("Available destinations from Tashkent:")
  for city, distance in cities.items():
    print(city, ":", distance, "km")
  city = input("Enter the destination city: ").lower()
  if city in cities:
    distance = cities[city]
  else:
    print("Invalid city. Please enter a valid city from the list.")
    city = input(" Enter the destination city: ").lower()
    distance = cities[city]
  return distance

def choose_car(units):
  if units == "True":  
      print("\nChoose a car (metric):")
      print("M = Matiz: 144 km/h, 19.1 km/l, $11.77/hr")
      print("F = Ferrari: 330 km/h, 16.2 km/l, $1000/hr")
      print("B = BMW X6: 250 km/h, 17.0 km/l, $200/hr")
  else:
      print("\nChoose a car (imperial):")
      print("M = Matiz: 89.4 mph, 45 mpg, $11.77/hr")
      print("F = Ferrari: 205.6 mph, 38.2 mpg, $1000/hr")
      print("B = BMW X6: 155.4 mph, 40 mpg, $200/hr")

  choice = input("Enter M, F, or B: ").lower()

  if units == "True":
      if choice == "m":
          return 144, 19.1, 11.77
      elif choice == "f":
          return 330, 16.2, 1000
      elif choice == "b":
          return 250, 17.0, 200
  else:
      if choice == "m":
          return 89.4, 45, 11.77
      elif choice == "f":
          return 205.6, 38.2, 1000
      elif choice == "b":
          return 155.4, 40, 200

def conversion(distance):
  miles = distance * 0.621371
  return miles

def get_trip_time(distance, speed):
  time = float(distance/speed)
  return time

def fuelcost(distance, fuel_efficiency, fuel_price):
  f_cost = (distance / fuel_efficiency) * fuel_price
  return f_cost

def totalcost(travel_time, hourly_cost, fuel_cost):
  total_cost = fuel_cost + (travel_time * hourly_cost)
  return total_cost

print("Welcome to the Rental Car Company Trip Planner!\n")
print("Let's plan your trip!")

distance = get_city_distance()

print("Do you want to use metric or imperial units?")
units = input("Enter 'm' for metric or 'i' for imperial: ").lower()
if units == "m":
  units = "True"
else:
  units = "False"
speed, fuel_efficiency, hourly_cost = choose_car(units)

if units == "i":
  distance = conversion(distance)
  print("The distance to your destination is", distance, "miles.")


print("What is the price of fuel per liter?")
fuel_price = float(input())

print("How long do you have available in hours?")
available_time = int(input())
print()
travel_time = int(get_trip_time(distance, speed))
print("The trip will take", travel_time , "hours.")
if travel_time < available_time:
  print("You have enough time for the trip.")
else:
  print("You do not have enough time for the trip.")
print()
fuel_cost = fuelcost(distance, fuel_efficiency, fuel_price)
print("The cost of fuel for the trip will be $", round(fuel_cost),2)
print("The total cost of the trip will be $", round(totalcost(travel_time, hourly_cost, fuel_cost),2))
print("")
print("Have a safe trip!")






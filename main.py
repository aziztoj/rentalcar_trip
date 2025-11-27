import time
units = 0
with open("trip_summary.txt", "w") as file:
    file.write("This is the details of your trip: \n")
file.close()

def get_city_distance():
  global city
  print("Choose a destination from the list below:")
  cities = {"andijon": 351, "samarqand": 306, "nukus": 1095}
  print("Available destinations from Tashkent:")
  for city, distance in cities.items():
    print(city, ":", distance, "km")
    time.sleep(1)
  city = input("Enter the destination city: ").lower()
  if city in cities:
    distance = cities[city]
  else:
    print("Invalid city. Please enter a valid city from the list.")
    time.sleep(2)
    city = input(" Enter the destination city: ").lower()
    distance = cities[city]
  return distance

def choose_car(units):
  global choice
  if units == "True":  
      print("\nChoose a car (metric):")
      print("M = Matiz: 144 km/h, 19.1 km/l, $11.77/hr")
      time.sleep(2)
      print("F = Ferrari: 330 km/h, 16.2 km/l, $1000/hr")
      time.sleep(2)
      print("B = BMW X6: 250 km/h, 17.0 km/l, $200/hr")
      time.sleep(2)
  else:
      print("\nChoose a car (imperial):")
      print("M = Matiz: 89.4 mph, 45 mpg, $11.77/hr")
      time.sleep(2)
      print("F = Ferrari: 205.6 mph, 38.2 mpg, $1000/hr")
      time.sleep(2)
      print("B = BMW X6: 155.4 mph, 40 mpg, $200/hr")
      time.sleep(2)

  choice = input("Enter M, F, or B: ").lower()
  while choice != "m" and choice != "f" and choice != "b":
    print("Invalid input. Please enter M, F, or B.")
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

def conversion():
  global distance
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
time.sleep(1)
print("Let's plan your trip!")
time.sleep(1)

distance = get_city_distance()

print("Do you want to use metric or imperial units?")

while units != "m" and units != "i":
  units = input("Enter 'm' for metric or 'i' for imperial: ").lower()
  if units == "m":
    units = "True"
    break
  elif units == "i":
    units = "False"
    distance = conversion()
    print("The distance to your destination is",round(distance,1), "miles.")
    break
  else:
    print("Invalid input. Please enter 'm' for metric or 'i' for imperial.")

speed, fuel_efficiency, hourly_cost = choose_car(units)


fuel_price = -1

while fuel_price <0:
  print("What is the price of fuel per liter?")
  fuel_price = float(input())
  if fuel_price < 0:
    print("Invalid input. Please enter a positive number.")
  elif fuel_price> 0:
     break
  else:
    print("Invalid input. Please enter a number.")
  

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
fuel_cost = round(float(fuelcost(distance, fuel_efficiency, fuel_price)),1)
total_cost = round(float(totalcost(travel_time, hourly_cost, fuel_cost)),1)
print("The cost of fuel for the trip will be $", round(fuel_cost,1))
print("The total cost of the trip will be $", total_cost)
print("")
time.sleep(2)

if choice == "m":
  choice = "Matiz"
elif choice == "f":
  choice = "Ferrari"
elif choice == "b":
  choice = "BMW X6"

with open("trip_summary.txt", "a") as file:
    file.write("Tashkent to " + city + ".\n")
    file.write("The distance to your destination is " + str(distance) + " km.\n\n")
    file.write("You will be driving a " + choice + ".\n")
    file.write("The trip will take " + str(travel_time) + " hours.\n\n")
    file.write("The cost of fuel for the trip will be $" + str(fuel_cost)+ ".\n")
    file.write("The total cost of the trip will be $" + str(total_cost) + ".\n")

print("Have a safe trip!")






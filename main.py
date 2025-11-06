def get_city_distance():
  print("Choose a destination from the list below:")
  cities = {"Andijon": 340, "Samarqand": 310, "Nukus": 1000}
  print("Available destinations from Tashkent:")
  for city, distance in cities.items():
    print(city, ":", distance, "km")
  city = input("Enter the destination city: ")
  distance = cities[distance]
  


def get_car_data():
  cars =  {"Matiz": 45: 144: 11.77, "Ferrari": 38.2: 330 : 1,000, "BMW X6": 40: 250: 200}
  print("Available cars:")
  for car, fuelef, speed, price in cars.items():
    print(car, ":", fuelef, "mpg", speed, "km/h", "$", price")




print("Welcome to the Rental Car Company Trip Planner!")
print("Let's plan your trip!")
print("Choose a car from the list below:")
get_car_data()
car = input("Enter the car you want to rent: ")
get_city_distance()
print("How long do you have available in hours?")
input()


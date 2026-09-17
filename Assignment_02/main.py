from rental import Vehicle, Renter, ElectricCar, Motorbike


car = Vehicle("Toyota", "Camry", "ABC123")
electric_car = ElectricCar("Tesla", "Model S", "TESLA123", 100)
motorbike = Motorbike("Honda", "CBR500R", "MOTO123", 500)
renter = Renter("Lwin", 123456)


print("Renter:", renter.name)
print("Licence:", renter.license_no)
print("Rented vehicles:", renter.rented)


# Demonstrate renting and returning.
print("\nBefore renting:", car)

car.rent()
print("After renting:", car)

car.return_vehicle()
print("After returning:", car)

try:
    Renter("", 12345)
except ValueError as error:
    print("\nInvalid name caught:", error)

try:
    Renter("Lwin", -1)
except ValueError as error:
    print("Invalid licence caught:", error)

print("\nAll vehicles:")
vehicles = [car, electric_car, motorbike]

for vehicle in vehicles:
    print(vehicle)
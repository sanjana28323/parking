print("VEHICLE PARKING FEE CALCULATOR")
print("\nVEHICLE TYPES:")
print("1. Two-wheeler")
print("2. Four-wheeler")
print("3. Heavy vehicle")

choice = int(input("\nEnter vehicle type (1-3): "))
hours = int(input("Enter parking duration in hours: "))
vehicle_number = int(input("Enter vehicle number:"))

if choice == 1:
    vehicle_type = "Two-wheeler"
    rate = 20

elif choice == 2:
    vehicle_type = "Four-wheeler"
    rate = 50

elif choice == 3:
    vehicle_type = "Heavy vehicle"
    rate = 100

else:
    print("Invalid vehicle type!")
    exit()

if hours <= 0:
    print("Invalid parking duration!")
else:
    total_fee = rate * hours

    print("\nPARKING DETAILS")
    print("vehicle number:",vehicle_number)
    print("Vehicle Type:", vehicle_type)
    print("Parking Duration:", hours, "hours")
    print("Total Parking Fee: Rs.", total_fee)
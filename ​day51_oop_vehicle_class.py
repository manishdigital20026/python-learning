# Day 51: Introduction to OOP - Vehicle Class & Objects

class Vehicle:
    # Constructor method: runs automatically when a new Vehicle object is created
    def __init__(self, plate_no, category, owner_name):
        self.plate_no = plate_no.upper()      # Attribute: Vehicle Plate
        self.category = category.upper()      # Attribute: BIKE or CAR
        self.owner_name = owner_name          # Attribute: Owner's Name
        self.status = "Parked"                # Default state attribute

    # Instance method: an action the Vehicle object can perform
    def display_info(self):
        print(f"[{self.category}] Plate: {self.plate_no} | Owner: {self.owner_name} | Status: {self.status}")

    # Method to mark the vehicle as exited
    def checkout(self):
        self.status = "Exited"
        print(f"[STATUS UPDATE] Vehicle {self.plate_no} has checked out.")


# --- Testing the Class ---
print("--- OOP Smart Parking: Vehicle Objects ---\n")

# Step 1: Create instances (objects) of the Vehicle class
car_1 = Vehicle("KA-01-MJ-2026", "Car", "Amit Sharma")
bike_1 = Vehicle("KA-04-E-1234", "Bike", "Pooja Verma")

# Step 2: Access object attributes and methods
print("Initial Vehicle States:")
car_1.display_info()
bike_1.display_info()

# Step 3: Trigger state change on a specific object
print("\nProcessing Exit:")
car_1.checkout()

print("\nUpdated States:")
car_1.display_info()
bike_1.display_info()

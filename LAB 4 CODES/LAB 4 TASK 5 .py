class Vehicle:
    def __init__(self, make, model, rentalprice):
        self.make = make
        self.model = model
        self.__rentalprice = rentalprice   
        self.available = True

    def check(self):
        if self.available:
            print(self.model, "is available for rent.")
        else:
            print(self.model, "is currently rented.")

    def calculate(self, days):
        total = self.__rentalprice * days
        print("Rental price for", days, "days is:", total)
        return total

    def rent(self):
        if self.available:
            self.available = False
            print(self.model, "has been rented.")
        else:
            print(self.model, "is already rented.")

    def returned(self):
        if not self.available:
            self.available = True
            print(self.model, "has been returned and is now available.")
        else:
            print(self.model, "was already available.")

    def display(self):
        print("Make:", self.make, ", Model:", self.model, ", Rental Price per day:", self.__rentalprice)

    def getrentalprice(self):
        return self.__rentalprice

class Car(Vehicle):
    def display(self):
        print("Vehicle Type: Car")
        super().display()

class SUVs(Vehicle):
    def display(self):
        print("Vehicle Type: SUVs")
        super().display()

class Truck(Vehicle):
    def display(self):
        print("Vehicle Type: Truck")
        super().display()

class Customer:
    def __init__(self, name, contact):
        self.name = name
        self.__contact = contact
        self.rentalhistory = []

    def add_rental(self, reservation):
        self.rentalhistory.append(reservation)

    def showhistory(self):
        print("\nRental History of", self.name, ":")
        if not self.rentalhistory:
            print("No rentals yet.")
        else:
            for r in self.rentalhistory:
                print("-", r.vehicle.model, "for", r.days, "days")

    def getcontact(self):
        return self.__contact

class RentalReservation:
    def __init__(self, customer, vehicle, days):
        self.customer = customer
        self.vehicle = vehicle
        self.days = days
        self.total = vehicle.calculate(days)

        vehicle.rent()
        customer.add_rental(self)

    def display(self):
        print("\nReservation Details:")
        print("Customer:", self.customer.name)
        print("Vehicle:", self.vehicle.model, "(", self.vehicle.make, ")")
        print("Duration:", self.days, "days")
        print("Total Cost:", self.total)

def showdetails(obj):
    print("\n--- Displaying Details ---")
    obj.display()

if __name__ == "__main__":
    
    c = Car("Honda", "Civic", 14000)
    s = SUVs("Toyota", "Prado", 18000)
    t = Truck("Nissan", "Titan", 15000)
    c.check()
    showdetails(c)

    cust = Customer("Amna Zahid", "amna@nu.edu.com")
    days = 3
    rent1 = RentalReservation(cust, c, days)
    showdetails(rent1)

    c.returned()
    cust.showhistory()


class Vehicle:
 
    def __init__(self,seatingcapacity):
        self.seatingcapacity=seatingcapacity
class Bus(Vehicle):
    
    def __init__(self, seatingcapacity):
        super().__init__(seatingcapacity)
        farecharge=seatingcapacity*100
        totalFare=(farecharge)+(0.1*farecharge)
        final=(totalFare)+(0.1*totalFare)

        print("The total amount of fare charge for Bus is:",totalFare)
        print("Final amount is:",final)    
Bus1=Bus(20.00)

    
       
        
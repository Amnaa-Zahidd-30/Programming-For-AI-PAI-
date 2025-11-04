class Drone:
    def __init__(self, droneId, maxloadinkg, status='idle'):
        self.droneId = droneId
        self.maxloadinkg = maxloadinkg
        self.__status = status
        self.currentPackage = None
        
class Package:
    def __init__(self, pid, weightinkg):
        self.pid = pid
        self.weightinkg = weightinkg

    def setstatus(self, newstatus):
        if newstatus in ('idle', 'delivering', 'charging'):
            self.__status = newstatus
        else:
            print("status not found!")

    def getstatus(self):
        # return status (also print for convenience)
        print("Current status:", self.__status)
        return self.__status

    def assignpackage(self, packobj):
        if self.__status == 'idle' and packobj.weightinkg <= self.maxloadinkg:
            self.currentPackage = packobj
            self.__status = 'delivering'
            print(f"Drone {self.droneId} assigned package {packobj.pid}")
        else:
            print(f"Drone {self.droneId} cannot take package {packobj.pid}")

class Fleetmanager:
    def __init__(self):
        self.objects = {}          
        self.pendingpackages = []  

    def adddrone(self, drone):
        self.objects[drone.droneId] = drone

    def addpackage(self, pack):
        self.pendingpackages.append(pack)

    def dispatchjobs(self):
        for pack in list(self.pendingpackages):  
            for d in self.objects.values():
                if d.getstatus() == 'idle':
                    d.assignpackage(pack)
                    self.pendingpackages.remove(pack)
                    break 

    def shutdown(self):
        for d in self.objects.values():
            d.setstatus('charging')
        print("Fleet Manager shutting down. All drones are now charging.")

d = Drone(78, 12, 'idle')
p = Package("P100", 10)

m = Fleetmanager()
m.adddrone(d)
m.addpackage(p)

m.dispatchjobs()
m.shutdown()

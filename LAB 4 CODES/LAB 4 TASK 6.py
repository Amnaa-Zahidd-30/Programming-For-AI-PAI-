class Employee:
    def __init__(self,name,salary,designation):
       self.name=name
       self.salary=salary
       self.designation=designation
      
    def calculatebonus(self):  
      if self.designation.lower()=="manager":
         bonus=0.2
         self.salary=self.salary+(0.2*self.salary) 
         print("Manager Salary After 20% Bonus is:",self.salary) 
            
       
      elif self.designation.lower()=="developer": 
         bonus=0.1
         self.salary=self.salary+(0.1*self.salary)
         print("Developer Salary After 10% Bonus is:",self.salary)

       
         

      
class Manager(Employee):
   def hire(self):
      print("Name:",self.name,', Salary:',self.salary,', Designation:',self.designation)
      print("Manager is hiring someone.")
         
class Developer(Employee):
   def writecode(self):
      print("\nName:",self.name,', Salary:',self.salary,', Designation:',self.designation)
      print("Developer is writing code.")

class SeniorManager(Manager):
   def calculatebonus(self):
    print("\nName:",self.name,', Salary:',self.salary,', Designation:',self.designation)
    if self.designation.lower()=="senior manager": 
      bonus=0.3
      self.salary=self.salary+(0.3*self.salary)
      print("Senior Manager Salary After 30% Bonus is:",self.salary)
      
         
                   
M=Manager("arham",50000,"MANAGER")
M.hire()
M.calculatebonus()

D=Developer("asma",60000,"DEVELOPER")
D.writecode()
D.calculatebonus()

S=SeniorManager("amna",90000,"SENIOR MANAGER")
S.calculatebonus()
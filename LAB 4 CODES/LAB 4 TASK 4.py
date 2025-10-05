class Student:

    def __init__(self,name,id):
        self.name=name
        self.id=id
        
    def display(self):
        print("\nStudent Name:",self.name,", Student Id:",self.id)

class Marks(Student):

    def __init__(self, algo,datascience,calculus,name,id):
        super().__init__(name,id)
        self.algo=algo
        self.datascience=datascience
        self.calculus=calculus

    def show(self):
        print("\nAlgo Marks:",self.algo,", Datascience Marks:",self.datascience,", Calculus Marks:",self.calculus)

class Result(Marks):

    def __init__(self, algo, datascience, calculus, name, id):
        super().__init__(algo, datascience, calculus, name, id)
        
    def calculate(self):
        total=self.algo+self.datascience+self.calculus
        print("\nTotal Marks:",total)
        print("\nAverage Marks:",total/3)
      
R1=Result(30,29,25,"amna",2310)

R2=Result(24,29,30,"hafsa",2345)

R3=Result(28,27,26,"ramsha",2378)


for x in R1,R2,R3:
    x.display()
    x.show()
    x.calculate()

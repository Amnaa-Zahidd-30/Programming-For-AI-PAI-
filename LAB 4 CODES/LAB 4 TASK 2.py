from abc import ABC,abstractmethod

class shape(ABC):
      @abstractmethod
      def area(self):
        pass
           
class rectangle(shape):
     def __init__(self,length,width):
         self.length=length
         self.width=width

     def area(self):
        a= self.length*self.width
        print("area of rectangle is:",a)
    
class square(shape):
    def __init__(self,side):
        self.side=side
    
    def area(self):
        b=self.side*self.side
        print("area of square is:",b)

class triangle(shape):
    def __init__(self,base,height):
        self.base=base
        self.height=height
        
    def area(self):
        c=(1/2)*(self.base*self.height)
        print("area of triangle is:",c)


r=rectangle(20,5)
r.area()
s=square(5)
s.area()
t=triangle(7,8)
t.area()




         
         



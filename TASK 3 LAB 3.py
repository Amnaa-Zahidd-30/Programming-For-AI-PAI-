
def employee():
 name=input("Enter your name:")
 salary=input("Enter your salary:")
 if salary=="":
    salary=10000
 else:
    salary=float(salary)

 netsalary=salary-(salary*0.02)
 print("Employee name: ",name)
 print("Salary after tax: ",netsalary)

employee()


 
 
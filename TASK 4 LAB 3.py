#TASK 4
list1=[]
list2=[]
for x in range(3):
   print("Enter the name of keys in your list 1:")
   keys=input()
   list1.append(keys)
for x in range(3):
   print("Enter the name of values in your list 2:")
   values=input()
   list2.append(values)
thisdict = {}
for i in range(len(list1)):
    thisdict[list1[i]] = list2[i]

print("keys with their respective values are: ", thisdict)

   




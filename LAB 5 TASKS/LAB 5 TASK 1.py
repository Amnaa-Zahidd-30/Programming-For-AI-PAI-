with open('random.txt','w')as fileObj:
   fileObj.write("Programming for AI!")

with open('random.txt','r')as fileObj:
   content=fileObj.read()
   print(content)


try:
    d=len(content)
    print("Number of total Characters in file:",d)
    h=len(content.split())
    print("Number of Word Count in file:",h)

except Exception as e:
   print("Exception occurs:",e)
       
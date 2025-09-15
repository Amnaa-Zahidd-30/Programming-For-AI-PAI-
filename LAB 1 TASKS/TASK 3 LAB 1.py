num = input("Enter a 4-digit number: ")   
swap = num[3] + num[2] + num[1] + num[0]
for d in swap:                    
    newdigit = (int(d) + 7) % 10      
    encrypted = str(newdigit)        
print("Encrypted number:", encrypted)

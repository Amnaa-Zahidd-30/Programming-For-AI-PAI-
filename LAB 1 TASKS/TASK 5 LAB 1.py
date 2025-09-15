name = input("Enter your name: ")
year = input("Enter your birth year: ")

first3 = name[:3].capitalize()   
last2 = year[-2:]                  

symbols = "@#%&*"
s = symbols[ord(name[0]) % len(symbols)]

password = first3 + last2 + symbols
print("Generated password:", password)

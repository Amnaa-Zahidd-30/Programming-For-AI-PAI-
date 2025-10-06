try:
    
    list1 = input("Enter the first list elements separated by spaces: ")
    list2 = input("Enter the second list elements separated by spaces: ")

    list1 = list1.split()
    list2 = list2.split()

    if len(list1) != len(list2):
        raise ValueError("Both lists must have the same number of elements!")
    mydict = {}
    for i in range(len(list1)):
        mydict[list1[i]] = list2[i]

    print("Dictionary created successfully:")
    print(mydict)

    with open('dictionary output.txt', 'w') as fileObj:
        
        for key, value in mydict.items():
            fileObj.write(f"{key} : {value}\n")

    print("Dictionary has been written to 'dictionary output.txt' successfully.")

except ValueError as ve:
    print("ValueError:", ve)
except FileNotFoundError:
    print("Error: File not found.")
except PermissionError:
    print("Error: No permission to write to the file.")
except Exception as e:
    print("An unexpected error occurred:", e)

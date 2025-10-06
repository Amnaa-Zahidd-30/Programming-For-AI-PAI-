try:
    search= input("Enter the word or phrase to search: ")
    replace= input("Enter the new word or phrase to replace with: ")

    with open('random.txt', 'r') as fileObj:
        content = fileObj.read()

    if search in content:
        print("Word found! Replacing...")
      
        updated = content.replace(search, replace)

        with open('random.txt', 'w') as fileObj:
            fileObj.write(updated)

        print("Replacement completed successfully.")
    else:
        print("Word not found in the file.")

except FileNotFoundError:
    print("Error: The file 'random.txt' does not exist.")
except PermissionError:
    print("Error: You do not have permission to read/write this file.")
except Exception as e:
    print("An unexpected error occurred:", e)

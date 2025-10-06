try:
    n = int(input("How many people do you want to enter? "))

    data = {}
    for i in range(n):
        name = input("Enter name: ")
        age = input("Enter age: ")
        data[name] = age

    print("Your data:", data)

    with open("data.txt", "w") as f:
        f.write(str(data))
    print("Data saved in file 'data.txt' successfully.")

    with open("data.txt", "r") as f:
        content = f.read()

    print("\nData read from file:")
    print(content)

    content = content.strip("{}")
    pairs = content.split(",")

    dict1 = {}
    for item in pairs:
        if ":" in item:
            parts = item.split(":")
            k = parts[0].strip().strip("'").strip('"')
            v = parts[1].strip().strip("'").strip('"')
            if v.isdigit():
                v = int(v)
            dict1[k] = v

    print("\nConverted back to dictionary:", dict1)

    maxage = max(dict1.values())
    print("\nMaximum age is:", maxage)

    print("Person(s) having maximum age:")
    for name, age in dict1.items():
        if age == maxage:
            print("-", name)

    print("\nPeople with same ages:")
    found = False
    for a in set(dict1.values()):
        sameage = [k for k, v in dict1.items() if v == a]
        if len(sameage) > 1:
            print("Age", a, ":", sameage)
            found = True
    if not found:
        print("No same ages found.")

except ValueError:
    print("Error: Invalid input, please enter correct values.")
except FileNotFoundError:
    print("Error: File not found.")
except PermissionError:
    print("Error: You do not have permission to write or read the file.")
except Exception as e:
    print("An unexpected error occurred:", e)

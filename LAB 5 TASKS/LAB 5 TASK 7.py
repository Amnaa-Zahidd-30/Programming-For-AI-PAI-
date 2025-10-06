def fix():
    try:
        with open("replacement_needed.txt", "r") as file:
            content = file.read()
        print("Original text from file:")
        print(content)

        corrected = ""
        for ch in content:
            if ch == "z":
                corrected += "s"
            else:
                corrected += ch

        print("Corrected text:")
        print(corrected)

        with open("replacement_needed.txt", "w") as file:
            file.write(corrected)
        print("\nFile updated successfully with corrected text.")

    except FileNotFoundError:
        print("Error: File 'replacement_needed.txt' not found. Please make sure it's in the same folder as this script.")
    except PermissionError:
        print("Error: You do not have permission to read or write the file.")
    except Exception as e:
        print("An unexpected error occurred:", e)

fix()

def writeq():
    try:
        sentence = input("Enter a sentence: ")

        if sentence.strip().endswith("?"):
            with open("questions.txt", "a") as file:
                file.write(sentence + "\n")
            print("Question saved in 'questions.txt'.")
        else:
            print("This is not a question. Nothing saved.")
            
    except FileNotFoundError:
        print("Error: File not found.")
    except PermissionError:
        print("Error: You do not have permission to write to this file.")
    except Exception as e:
        print("An unexpected error occurred:", e)

writeq()

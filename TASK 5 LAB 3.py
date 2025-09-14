# TASK 5
def check():
    print("Enter a word to see if its palindrome or not: ")
    s = input()
    first = 0
    last = len(s) - 1
    mid = len(s) // 2

    while first < mid:
        if s[first] != s[last]:
            print("not palindrome.")
            return  
        first += 1
        last -= 1

   
    print("palindrome.")

check()

       
   

                                 
     
  



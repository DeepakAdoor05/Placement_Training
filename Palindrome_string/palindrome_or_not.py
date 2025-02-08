def palindrome(text):
    if text == text[ : :-1] :
        print("Palindrome")
    else:
        print("Not Palindrome")

string = input() # Taking the number as string.
palindrome(string)
def check_palindrome(S):
    if S == S[::-1]:
        print(S)
    else:
        crop_S = S[-1:0:-1]
        new_string = crop_S + S
        if new_string == new_string[::-1]:
            print(new_string)

string = input()
check_palindrome(string)
def palindrome(n):
    reverse = 0
    no = n
    while n > 0 :
        last_digit = n % 10
        reverse = (reverse*10) + last_digit
        n = n//10
    if no == reverse:
        return "Palindrome"
    else:
        return "Not Palindrome"
    
number = int(input())
print(palindrome(number))
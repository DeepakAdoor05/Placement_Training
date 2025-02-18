def is_prime(num):
    flag = True
    if num > 1:
        for i in range(2,num):
            if (num%i) == 0:
                flag = False
                break
        return flag
    return False
n = 5   # Prime number
prime_count = 0
if False  is is_prime(n):
    print("Not a Prime no")
else:
    while n > 1 :
        if is_prime(n):
            prime_count += 1
        n -= 1
    print(prime_count)  # which term is the given prime number. 3rd term is 5 (2,3,5,7...)
def is_prime(num):
    flag = True
    if num > 1:
        for i in range(2,num):
            if (num%i) == 0:
                flag = False
                break
        return flag
    return False
n = 4
prime_count = 0
number = 2
while True:
    if is_prime(number):
        prime_count +=1
    if prime_count == n:
        break
    number += 1
print(number) # 4th term is '7'. (2,3,5,7,...)
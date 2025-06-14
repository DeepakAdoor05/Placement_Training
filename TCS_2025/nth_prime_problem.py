def is_prime(num):
    flag = True
    if num > 1:
        for i in range(2,num):
            if (num%i) == 0:
                flag = False
                break
        return flag
    return False
x, y = map(int, input().split())
prime_count = 0
number = 2
A = 0
B = 0
while True:
    if is_prime(number):
        # print(number)
        prime_count +=1
        if prime_count == x:
            A = number
        if prime_count  == y:
            B = number
    if A > 0 and B > 0:
        break
    number += 1
C = A*B-1
print(C)
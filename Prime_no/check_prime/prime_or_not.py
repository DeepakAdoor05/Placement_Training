def is_prime(num):
    flag = True
    if num > 1:
        for i in range(2,num):
            if (num%i) == 0:
                flag = False
                break
        return flag
    return False

print(is_prime(3))
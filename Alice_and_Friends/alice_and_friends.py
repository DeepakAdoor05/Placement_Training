# TCS-NQT-2022-Question
no_friends = int(input())
arr = list(map(int, input().split()))
count = 0
value_last = arr[-1]
if value_last == arr[0]:
    count = no_friends
else:
    for i in arr:
        if i == arr[0]:
            count += 1
print(no_friends-count)
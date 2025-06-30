n = int(input())
exp = int(input())

power = []
bonus = []
a = []
count = 0

for i in range(n):
    power.append(int(input()))
for j in range(n):
    bonus.append(int(input()))
for k in range(n):
    a.append([power[k],bonus[k]])
print(a)        # [[78, 10], [130, 0]]
a.sort()
for i in a:
    if i[0] > exp:  # 78 > 100
        break
    count += 1
    exp += i[1]     # 78 + 10
print(count)


# Input	Output	Output Description
# 2        2      Initial experience level is 123 points.
# 123             Defeat the first monster having power of 78 and bonus of 10. Experience level is now 123+10=133.
# 78              Defeat the second monster.
# 130
# 10
# 0
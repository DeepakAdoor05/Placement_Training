# Question: 
# Write a program that takes a string and moves all characters before its first vowel to the end, then appends "ay". 
# If the string contains no vowels, append "ay" directly. 

s = 'cheese'
for i in range(len(s)):
    if s[i] in 'aeiouAEIOU':
        s = s[i:]+s[:i]+'ay'
        break
else:
    s += 'ay'
print(s)

# input
# cheese

# output
# eesechay
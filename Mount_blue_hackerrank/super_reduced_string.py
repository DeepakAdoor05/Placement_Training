def superReducedString(s):
    stack = ['#']
    for i in s:
        if stack[-1] == i:  # If the element is same as top of stack
            stack.pop()     # Pop the last element and do not push the current element
        else:
            stack.append(i) # Else push the  element in the stack
    ans = ''
    for i in stack[1:]:     # Ignoring the first index
        ans += i            # Store the answer in the variable 'ans'
    if ans:
        return ans
    return "Empty String"

s = input()
print(superReducedString(s))
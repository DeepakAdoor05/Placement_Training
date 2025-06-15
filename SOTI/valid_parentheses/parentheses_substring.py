# Longest Valid parentheses substring


# stack approach

# def check_parentheses(s):
#     stack = []
#     max_length = 0
#     base = -1

#     for i, char in enumerate(s):
#         if char == '(':
#             stack.append(i)
#         else:
#             if not stack:
#                 base = i
#             else:
#                 stack.pop()
#                 if not stack:
#                     max_length = max(max_length, i - base)
#                 else:
#                     max_length = max(max_length, i - stack[-1])

#     return max_length

# Time Complexity: O(n)
# Space Complexity: O(n) (for the stack)

def check_parentheses(s):
    l_count = r_count = max_length = 0
    i = 0
    while i < len(s):
        if s[i] == "(":
            l_count += 1
        else:
            r_count += 1
        if l_count == r_count:
            max_length = max(max_length,l_count+r_count)
        elif r_count > l_count:
            l_count = r_count = 0     
        i += 1 

    l_count = r_count = 0
    i = len(s)-1
    while i >= 0:
        if s[i] == "(":
            l_count += 1
        else:
            r_count += 1
        if l_count == r_count:
            max_length = max(max_length,l_count+r_count)
        elif l_count > r_count:
            l_count = r_count = 0     
        i -= 1
    return max_length      

string = "((()"
print(check_parentheses(string))

# Time Complexity: O(n)
# Space Complexity: O(1) (constant extra space)
# def possible_strings_count(s):
#     list = []
#     for i in range(len(s)):
#         for j in range(i+1,len(s)+1):
#             list.append(s[i:j])
#     distinct_list = set(list)
#     return len(distinct_list)

def possible_strings_count(s):
    substring = set()
    for i in range(len(s)):
        for j in range(i+1,len(s)+1):
            substring.add(s[i:j])
            print(substring)
    print(substring)
    return len(substring)

S = input()
print(possible_strings_count(S))
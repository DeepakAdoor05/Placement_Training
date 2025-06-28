# def count_distinct_strings(arr):
#     unique = set()
#     for s in arr:
#         even = ''.join(sorted(s[::2]))
#         odd = ''.join(sorted(s[1::2]))
#         unique.add((even,odd))  # (even,odd): generate a tuple pair and perform set on it 
#     print(unique)
#     return len(unique)

def count_distinct_strings(arr):
    patterns = []
    for s in arr:
        even = ''.join(sorted(s[::2]))
        odd = ''.join(sorted(s[1::2]))
        patterns.append((even,odd)) # can use even+odd => 'acbd'
    print(patterns)
    return len(set(patterns))

array = ["abcd", "cbad", "bacd"]
print(count_distinct_strings(array))
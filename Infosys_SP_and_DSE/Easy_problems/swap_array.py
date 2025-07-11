# Using a temp variable
# def array_swap(arr1,arr2):
#     temp = arr1
#     arr1 = arr2
#     arr2 = temp
#     print("arr1 = ",arr1)
#     print("arr2 = ",arr2)

# 2nd way
def array_swap(arr1,arr2):
    return print(f'arr1 = {arr2} \narr2 = {arr1}')

# 3rd way
# def array_swap(arr1,arr2):
#     arr1, arr2 = arr2, arr1
#     print("arr1 = ",arr1)
#     print("arr2 = ",arr2)


arr1 = [1,2,3,4]
arr2 = [5,6,7,8]
array_swap(arr1,arr2)
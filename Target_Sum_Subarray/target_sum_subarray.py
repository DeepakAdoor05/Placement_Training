def find_subarray(arr,target):
    result = []
    for i in range(len(arr)):
        sum = 0
        subarray = []
        for j in range(i,len(arr)):
            sum += arr[j]
            subarray.append(arr[j])
            if sum == target:
                result.append(subarray[:])
                # result.append(subarray)       if subarray is simply given use break
                # break
    print(result)


arr = [1,2,3,4,5,67]
target = 5
find_subarray(arr,target)
class UserMainCode:
    def count_subarrays(input1,input2):
        count = 0
        for i in range(input2 - 2):
            first_element = input1[i]
            second_element = input1[i+1]
            third_element = input1[i+2]
            if first_element + third_element == second_element:
                count += 1
        return count

arr = [1,2,1,3,5,2,4,2]
n = 8
print(UserMainCode.count_subarrays(arr,n)) 
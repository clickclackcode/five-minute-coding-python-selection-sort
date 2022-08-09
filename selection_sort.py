import random

# generate a list of 10 random numbers between 1 and 100
nums = []
for i in range(10):
    num = random.randint(1, 100)
    nums.append(num)
    
print(f"Before sorting: {nums}")

# traverse the list
for i in range(len(nums)):
    
    # find the index of the smallest element after index i
    smallest_index = i
    for j in range(i + 1, len(nums)):
        if nums[j] < nums[smallest_index]:
            smallest_index = j
            
    # swap the element at smallest index with element at index i
    temp = nums[i]
    nums[i] = nums[smallest_index]
    nums[smallest_index] = temp
    
print(f"After sorting: {nums}")
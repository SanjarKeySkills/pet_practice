# Big O notation understanding task
#write the function  which receives array of numbers and return true, if at leat one duplicate will be in array and put
# 'false' in opposite case
#[1, 2, 3, 4, 5] -> false
#[1, 2, 3, 2, 4] -> (2 num duplicates)

def has_duplicate_brute_force(nums):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] == nums[j]:
                return True
    return False
# Big O: O(n^2)

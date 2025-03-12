# Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

HashSet = set()
for num in nums:
    if num in HashSet:
        return True
    HashSet.add(num)
return False
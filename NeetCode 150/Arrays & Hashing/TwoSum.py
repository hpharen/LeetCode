# LC 1
# Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.
# You may assume that every input has exactly one pair of indices i and j that satisfy the condition.
# Return the answer with the smaller index first.

HashMap = {}
for i, num in enumerate(nums):
    diff = target - num
    if diff in HashMap:
        return [HashMap[diff], i]
    HashMap[num] = i
return
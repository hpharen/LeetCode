# LC 242
# Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

sortedS = sorted(s)
sortedT = sorted(t)
if sortedS == sortedT:
    return True
return False
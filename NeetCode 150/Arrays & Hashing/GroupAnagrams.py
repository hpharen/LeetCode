# LC 49
# Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.
HashMap = defaultdict(list) # initialize defaultdict hashmap
for s in strs: # for each string in strs array
    count = [0] * 26 # create 26 

    for c in s: # for each character in each string
        count[ord(c) - ord("a")] += 1 # the counter for that character - ord("a") will always point to that character, incremented if found

    HashMap[tuple(count)].append(s) # string added to hashmap

return HashMap.values()
# LC 49
# Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.
HashMap = defaultdict(list)
for s in strs:
    count = [0] * 26

    for c in s:
        count[ord(c) - ord("a")] += 1

    HashMap[tuple(count)].append(s)

return HashMap.values()
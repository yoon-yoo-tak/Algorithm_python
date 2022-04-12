"""
리트코드 49 그룹 애너그램

"""
from collections import defaultdict
def groupAnagrams(strs: list):
    anagrams = defaultdict(list)
    for word in strs:
        anagrams[''.join(sorted(word))].append(word)
    return list(anagrams.values())
print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))

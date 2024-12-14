https://neetcode.io/problems/anagram-groups

from sortedcontainers import SortedDict

class Solution:
    def formAnagramChars(self, s):
        unique = SortedDict()
        for c in s:
            unique[c] = unique.get(c, 0) + 1
        return unique
        
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramMap = {} # unique map of characters and counts in sorted order: List[str]
        for ele in strs:
            unique = self.formAnagramChars(ele)
            if str(unique) in anagramMap:
                anagramMap[str(unique)].append(ele)
            else:
                anagramMap[str(unique)] = [ele]
        return [v for k, v in anagramMap.items()]

if __name__ == "__main__":

    # answer is [["hat"],["act", "cat"],["stop", "pots", "tops"]]
    continuousSubarrays(["act","pots","tops","cat","stop","hat"])
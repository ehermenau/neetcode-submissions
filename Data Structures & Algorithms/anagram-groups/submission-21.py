from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = defaultdict(list)
        for word in strs:
            count = [0] * 26 
            for char in word:
                position = ord(char) - ord('a') 
                count[position] += 1 
            key = tuple(count)
            output[key] += [word]

        return list(output.values())

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = {}
        for word in strs:
            key = "".join(sorted(word))
            if key in output:
                output[key] += [word]
            else:
                output[key] = [word] 
            
        return list(output.values())

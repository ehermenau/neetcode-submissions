class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        outer_list = []
        for word in strs:
            target = sorted(word)
            if outer_list:
                match = False
                for inner in outer_list:
                    if target == sorted(inner[0]):
                        inner.append(word)
                        match = True
                if not match:
                    outer_list.append([word])
            else:
                outer_list.append([word])

        return outer_list

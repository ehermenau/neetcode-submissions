class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            hash_index = s.find("#", i)
            length = int(s[i:hash_index])
            start = hash_index + 1
            end = start + length
            content = s[start:end]
            res.append(content)
            i = end

        return res
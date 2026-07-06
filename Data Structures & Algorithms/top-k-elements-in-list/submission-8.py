from collections import defaultdict 

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        holder = defaultdict(int)
        res = []
        for n in nums:
            holder[n] += 1
        target = sorted(list(holder.values()))[-k:]
        for key, v in holder.items():
            if v in target:
                res.append(key)

        return res

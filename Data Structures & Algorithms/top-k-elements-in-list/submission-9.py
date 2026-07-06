from collections import defaultdict 

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        holder = defaultdict(int)
        res = []
        for n in nums:
            holder[n] += 1
        for key, v in holder.items():
            if v in sorted(list(holder.values()))[-k:]:
                res.append(key)

        return res

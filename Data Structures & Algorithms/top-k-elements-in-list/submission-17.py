from collections import defaultdict 


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        holder = defaultdict(int)
        for n in nums:
            holder[n] += 1
        arr = []
        for key, v in holder.items():
            arr.append([v, key])

        arr.sort()
        res = []
        for x in arr[-k:]:
            res.append(x[1])

        return(res)

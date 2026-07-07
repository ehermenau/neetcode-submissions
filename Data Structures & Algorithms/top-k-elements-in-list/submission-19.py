from collections import defaultdict 


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        holder = defaultdict(int)
        arr = [[] for _ in range(len(nums) + 1)]
        for n in nums:
            holder[n] += 1 
        
        for key, val in iter(holder.items()):
            arr[val].append(key)

        res = []
        while k > len(res):
            res.extend(arr.pop(-1))

        return res
        
from collections import defaultdict 

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        holder = defaultdict(int)
        res = [0] * k
        for n in nums:
            holder[n] += 1

        print(dict(holder))
        for _ in range(k):
            highest = 0
            for key in holder:
                if holder[key] > highest:
                    highest = holder[key]
                    res[_] = key
                    largest = key
            holder.pop(largest)

        return res
 

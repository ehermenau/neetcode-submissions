# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        result = []
        arr = pairs[:]
        if len(arr) > 0:
            result.append(arr[:])
            for i in range(1, len(arr)):
                j = i
                while j > 0 and arr[j-1].key > arr[j].key:
                    arr[j-1], arr[j] = arr[j], arr[j-1]
                    j -= 1
                result.append(arr[:])
        return result


        
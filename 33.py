"""
33. Search in Rotated Sorted Array
"""
from typing import List

def binary_search(arr, lower, upper, target):
    if upper >= lower:
        mid = (upper + lower) // 2
        if arr[mid][0] == target:
            return arr[mid][1]
        elif arr[mid][0] > target:
            return binary_search(arr, lower, mid - 1, target)
        else:
            return binary_search(arr, mid + 1, upper, target)
    else:
        return -1

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        pairs = [
            (num, index)
            for index, num in enumerate(nums)
        ]
        pairs = sorted(pairs, key=lambda x: x[0])
        return binary_search(pairs, 0, len(pairs)-1, target)


if __name__ == "__main__":
    print(Solution().search([4,5,6,7,0,1,2], 0))
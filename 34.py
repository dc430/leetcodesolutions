"""
34. Find First and Last Position of Element in Sorted Array
"""
from typing import List


def binary_search(arr, lower, upper, target, indices):
    if upper >= lower:
        mid = (upper + lower) // 2
        print(mid, lower, upper)
        if arr[mid][0] == target:
            indices.append(arr[mid][1])
            if mid - 1 >= 0  and arr[mid-1][0] == target:
                binary_search(arr, lower, mid-1, target, indices)
            if mid+1 <= upper and arr[mid+1][0] == target:
                binary_search(arr, mid+1, upper, target, indices)
            return arr[mid][1]
        elif arr[mid][0] > target:
            return binary_search(arr, lower, mid - 1, target, indices)
        else:
            return binary_search(arr, mid + 1, upper, target, indices)
    else:
        return -1


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        default_indices = [-1, -1]
        if not nums:
            return default_indices
        pairs = [
            (num, index)
            for index, num in enumerate(nums)
        ]
        print([i for i in range(len(nums))])
        print(nums)
        indices = []
        binary_search(pairs, 0, len(nums) - 1, target, indices)
        if indices:
            res = [min(indices), max(indices)]
        else:
            res = default_indices
        return res


if __name__ == "__main__":
    print(Solution().searchRange([1,2,2,2,5], 6))

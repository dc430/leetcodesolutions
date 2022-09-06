"""
74. Search a 2D Matrix
"""
from typing import List


def binary_search(arr, lower, upper, target):
    if upper >= lower:
        mid = (upper + lower) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            return binary_search(arr, lower, mid - 1, target)
        else:
            return binary_search(arr, mid + 1, upper, target)
    return -1


def binary_search_rows(arr, lower, upper, target):
    if upper >= lower:
        mid = (upper + lower) // 2
        if mid + 1 <= upper and arr[mid][0] <= target < arr[mid + 1][0]:
            return mid, binary_search(arr[mid], 0, len(arr[mid]) - 1, target)
        elif mid + 1 > upper:
            return mid, binary_search(arr[mid], 0, len(arr[mid]) - 1, target)
        elif arr[mid][0] > target:
            return binary_search_rows(arr, lower, mid - 1, target)
        else:
            return binary_search_rows(arr, mid + 1, upper, target)
    return [-1, -1]


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        t = binary_search_rows(matrix, 0, len(matrix) - 1, target)
        if t[1] != -1:
            return True
        return False


if __name__ == "__main__":
    print(Solution().searchMatrix([[1]], 1))

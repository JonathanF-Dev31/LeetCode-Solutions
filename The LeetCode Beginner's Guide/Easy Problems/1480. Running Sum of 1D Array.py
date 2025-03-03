"""
To sum one by one item in the list od 1d
args:
    nums: list[int]
return:
    list[int]
"""

from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] = nums[i-1] + nums[i]
        return nums      
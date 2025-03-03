"""
To sum one by one row in the matrix and return the maximum sum
args:
    accounts: list[list[int]]
return:
    int
"""


from typing import List

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(sum(account) for account in accounts)
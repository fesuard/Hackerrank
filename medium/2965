https://leetcode.com/problems/find-missing-and-repeated-values/description/
You are given a 0-indexed 2D integer matrix grid of size n * n with values in the range [1, n2]. 
Each integer appears exactly once except a which appears twice and b which is missing. 
The task is to find the repeating and missing numbers a and b.
Return a 0-indexed integer array ans of size 2 where ans[0] equals to a and ans[1] equals to b.

from collections import defaultdict

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        repeating = missing = 0
        freq = defaultdict(int)
        for row in grid:
            for elem in row:
                freq[elem] += 1
        for num in range(1, len(grid) ** 2 + 1):
            if freq[num] == 2:
                repeating = num
            if freq[num] == 0:
                missing = num
        return [repeating, missing]

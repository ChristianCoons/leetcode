'''
2364. Count Number of Bad Pairs

You are given a 0-indexed integer array nums. A pair of indices (i, j) is a bad pair if i < j and j - i != nums[j] - nums[i].

Return the total number of bad pairs in nums.
'''
from typing import List

class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        output = 0
        subSets = {} 
        for i in range(0, len(nums)):
            distDiff = nums[i] - i
            subSets[distDiff] = subSets.get(distDiff, 0) + 1
        
        print(subSets)
        n = len(nums)
        allPosssible = (n/2)*(n-1)
        allGood = 0

        for key, val in subSets.items():
            if val > 1:
                allGood += (val/2)*(val - 1)
        
        print(allPosssible - allGood)
        return int(allPosssible - allGood)
                


solution = Solution()
solution.countBadPairs([4,1,3,3,4])
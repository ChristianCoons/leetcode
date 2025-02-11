'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
'''

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        left = 0
        leftMax = 0
        right = len(height) - 1
        rightMax = 0

        while left < right:
            if height[left] <= height[right]:
                if leftMax > height[left]:
                    water += (leftMax - height[left])
                else:
                    leftMax = height[left]
                left += 1
            elif height[left] > height[right]:
                if rightMax > height[right]:
                    water += (rightMax - height[right])
                else:
                    rightMax = height[right]

                right -= 1


        print(water)
        return water
    
solution = Solution()
solution.trap([0,1,0,2,1,0,1,3,2,1,2,1])
solution.trap([0,1,0,2,1,4,1,3,2,1,2,1])
solution.trap([0,1,0,2,1,4,1,3,2,1,3,1])
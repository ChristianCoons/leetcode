'''
1726. Tuple with Same Product
Medium
Given an array nums of distinct positive integers, 
return the number of tuples (a, b, c, d) 
such that a * b = c * d 
where a, b, c, and d are elements of nums, 
and a != b != c != d.
Constraints:
    1 <= nums.length <= 1000
    1 <= nums[i] <= 104
    All elements in nums are distinct.
'''
from typing import List

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        numTuples = 0
        productCount = {}

        for i in range(0, len(nums) - 1):
            for j in range(i+1, len(nums)):
                product = nums[i] * nums[j]
                #productDict[(nums[i], nums[j])] = product
                productCount[product] = productCount.get(product, 0) + 1
                if productCount[product] >= 2:
                    numTuples += (8*(productCount[product] - 1))

        #print(f"{productCount}")
                
        print(numTuples)
            

        return numTuples
    
    #Second attempt, this one looks through the dict to calc the count after making the Dict
    #Going to attempt to make it better by counting as we go through the dict
    def tupleSameProductDoubleLooks(self, nums: List[int]) -> int:
        numTuples = 0
        productCount = {}

        for i in range(0, len(nums) - 1):
            for j in range(i+1, len(nums)):
                product = nums[i] * nums[j]
                #productDict[(nums[i], nums[j])] = product
                productCount[product] = productCount.get(product, 0) + 1

        #print(f"{productCount}")

        for key, val in productCount.items():
            if val >= 1:
                numTuples += int(8*(val/2)*(val-1))
                
        #print(numTuples)
            

        return numTuples
    
    #Brute Forced Going over multiple times, just really bad first attempt Time Ran out Error
    def tupleSameProductBad(self, nums: List[int]) -> int:
        numTuples = 0
        productDict = {(nums[i],nums[j]): nums[i] * nums[j] for i in range(0, len(nums)) for j in range(i+1, len(nums))}
        

        #print(f"{productDict}")
        keys = list(productDict.keys())
        for i in range(0, len(keys)):
            #print(productDict[keys[i]])
            for j in range(i+1, len(keys)):
                if productDict[keys[i]] == productDict[keys[j]]:
                    numTuples += 1
        
        numTuples *= 8
        #print(numTuples)
            

        return numTuples

solution = Solution()

solution.tupleSameProduct([2,3,4,6])
solution.tupleSameProduct([2,3,4,5,6,10,15])
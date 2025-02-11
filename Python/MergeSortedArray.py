from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = m - 1
        j = n - 1
        k = m + n - 1
        while j >= 0:
            if i >= 0 and nums1[i] >= nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        print(nums1)


    def mergeWrong(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = 0
        j = 0

        while j < n:
            print(f"j: {nums2[j]} <= i: {nums1[i]}")
            if nums2[j] <= nums1[i] or nums1[i] == 0:

                nums1[:] = nums1[:i] + [nums2[j]] + (nums1[i:-1])
                j+=1
                i+=1
            else:
                i += 1


        print(nums1)
                    
        """
        Do not return anything, modify nums1 in-place instead.
        """

solution = Solution()
solution.merge([4,5,6,7,8,9,0,0,0,0,0], 6, [2,3,4,5,6], 5)
solution.merge([0,0,0,0,0], 0 , [2,3,4,5,6], 5)
solution.merge([4,5,6,7,8,9], 6, [], 0)
solution.merge([1,2,3,0,0,0], 3, [2,5,6], 3)
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        j = 0
        end = len(nums)
        while j < end:
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
            else:
                end -= 1
            j += 1


    def removeElementOverKill(self, nums: List[int], val: int) -> int:
        #print(nums)
        end = len(nums)
        i = 0
        while i < end:
            print(i)
            if nums[i] == val:
                nums[:] = nums[:i] + nums[i + 1:]
                print(nums)
                end -= 1
                i -= 1
            i += 1
        return end

        #print(nums)

solution = Solution()
solution.removeElement([1,2,3,3,4,5,6], 3)

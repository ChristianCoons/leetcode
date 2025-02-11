#region Description
/*
26. Remove Duplicates from Sorted Array
Easy
Topics
Companies
Hint

Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

    Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
    Return k.
*/
#endregion

namespace Solutions.RemoveDuplicatesFromSortedArray
{
public class Solution {
    public int RemoveDuplicates(int[] nums) {
        Console.WriteLine($"nums: [{string.Join(", ", nums)}]");
        int j = 1;
        for (int i = 1; i < nums.Length; i++)
        {
            if (nums[i] != nums[i - 1]){
                nums[j] = nums[i];
                j++;
            }
        }
        Console.WriteLine(j);
        return j;
    }

    public void RunTests(){
        RemoveDuplicates(new int[] {1,2,3,4,5,6,7,7,8,8,9,9,10});
    }
}
}
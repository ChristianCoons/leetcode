/*
Given an integer array nums sorted in non-decreasing order,
 remove some duplicates in-place such that each unique element 
 appears at most twice. The relative order of the elements 
 should be kept the same.

Since it is impossible to change the length of the array in 
some languages, you must instead have the result be placed 
in the first part of the array nums. More formally, if there 
are k elements after removing the duplicates, then the 
first k elements of nums should hold the final result. 
It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. 
You must do this by modifying the input array in-place 
with O(1) extra memory.
*/
namespace Solutions.RemoveDuplicates_2
{
public class Solution {
    public int RemoveDuplicates(int[] nums) {
        Console.WriteLine($"{string.Join(", ", nums)}");
        var countDict = new Dictionary<int, int>();
        int j = 0;
        for (int i = 0; i < nums.Length; i++)
        {
            if (countDict.ContainsKey(nums[i])) {
                countDict[nums[i]]++;
            } else {
                countDict[nums[i]] = 1;
            }

            if (countDict[nums[i]] <= 2){
                nums[j] = nums[i];
                j++;
            }
        }
        Console.WriteLine($"{string.Join(", ", nums)}");
        return j;
    }

    public void RunTests(){
        RemoveDuplicates(new int[] {1,1,1,2,4,5,5,6,6,6,6,7,8,9,9});
    }
}

}
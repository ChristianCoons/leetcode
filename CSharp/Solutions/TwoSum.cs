
namespace Solutions.TwoSum
{
    public class Solution 
    {
        public int[] TwoSum(int[] nums, int target) 
        {
            int[] sumNums = new int[2];
            for (int i = 0; i < nums.Length - 1; i++)
            {
                for (int j = i+1; j < nums.Length; j++)
                {
                    if (nums[i] + nums[j] == target)
                    {
                        sumNums[0] = i;
                        sumNums[1] = j;
                        return sumNums;
                    }
                }
                
            }
            return sumNums;
        }

        public void RunTests()
        {
            var result = TwoSum(new int[] {1,2,3,4,5,5,6,7,8,9}, 4);
            Console.WriteLine(string.Join(", ", result));
        }
    }

}
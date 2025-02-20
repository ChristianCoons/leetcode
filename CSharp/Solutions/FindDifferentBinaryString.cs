


namespace Solutions.FindDifferentBinaryString
{
public class Solution {
    public string FindDifferentBinaryString(string[] nums) {
        string res = "";
        Console.WriteLine(string.Join(", ", nums));

        for (int i = 0; i < nums.Length; i++)
        {
            if (nums[i][i] == '0'){
                res = res + "1";
            }
            else{
                res = res + "0";
            }
        }
        Console.WriteLine(res);
        return res;
    }

    public void RunTests(){
        FindDifferentBinaryString(new[] {"100", "010", "001"});
    }
}
}
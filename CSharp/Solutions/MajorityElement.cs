namespace Solutions.MajorityElement
{

public class Solution {
    public int MajorityElement(int[] nums) {
        int count = 1;
        int number = nums[0];
        Console.WriteLine(string.Join(", ", nums));
        for(int i = 1; i < nums.Length; i++){
            if(number == nums[i]){
                count++;
            }
            if(number != nums[i]){
                count--;
                if (count <= 0){
                    number = nums[i];
                    count++;
                }
            }
        }
        Console.WriteLine(number);
        return number;
    }
    public void RunTests(){
        MajorityElement(new int[] {2,2,1,1,1,2,2});
    }
}
}
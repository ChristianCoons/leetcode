

namespace Solutions.MaxProfit
{

public class Solution {
    public int MaxProfit(int[] prices) {
        Console.WriteLine($"{string.Join(", ", prices)}");
        int low = prices[0];
        int diff = 0;
        int maxDiff = 0;
        for (int i = 1; i < prices.Length; i++)
        {
            if (prices[i] < low){
                low = prices[i];
            }
            else{
                diff = prices[i] - low;
                if (diff > maxDiff){
                    maxDiff = diff;
                }
            }
        }
        Console.WriteLine(maxDiff);
        return maxDiff;
    }
    public void RunTests(){
        MaxProfit([10,5,7,3,7,6,10]);
    }
}
}

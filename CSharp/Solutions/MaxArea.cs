/*
11. Container With Most Water
Medium

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
*/


using System.Globalization;

namespace Solutions.MaxArea
{
public class Solution {
    public int MaxArea(int[] height) {
        Console.WriteLine(string.Join(", ", height));
        int i = 0;
        int j = height.Length - 1;
        int max = 0;
        int curr = 0;
        while (i != j){
            
            curr = height[i] > height[j] ? height[j] * (j - i) : height[i] * (j - i);
            if (curr > max){
                max = curr;
            }
            if (height[i] > height[j]){
                j--;
            }
            else{
                i++;
            }
        }

        Console.WriteLine(max);
        return max;
    }
    
    public void RunTests(){
        MaxArea(new int[] {4,10,11,40,50,1,2});
    }
}

}
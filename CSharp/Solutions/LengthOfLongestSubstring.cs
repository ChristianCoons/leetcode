/*
3. Longest Substring Without Repeating Characters
Medium

Given a string s, find the length of the longest
substring
without repeating characters.
*/
namespace Solutions.LengthOfLongestSubstring
{
public class Solution {
    public int LengthOfLongestSubstring(string s) 
    {
        string subString = "";
        int currentLen = 0;
        int subMax = 0;
        foreach( char c in s)
        {
            if (!subString.Contains(c))
            {
                subString += c;
                currentLen += 1;
                if(currentLen > subMax)
                {
                    subMax = currentLen;
                }
                //Console.WriteLine(subString);
            }
            else
            {
                subString = subString.Substring(subString.IndexOf(c) + 1);
                subString += c;
                currentLen = subString.Length;
            }
        }
        Console.WriteLine(subMax);
        return subMax;
    }
    public void RunTests(){
        LengthOfLongestSubstring("feabcbabeabc");
    }
}
}


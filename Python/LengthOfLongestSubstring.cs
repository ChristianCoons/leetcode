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
                Console.WriteLine(subString);
            }
            else
            {
                subString = subString.Substring(subString.IndexOf(c) + 1);
                subString += c;
                currentLen = subString.Length;
            }
        }

        return subMax;
    }
}
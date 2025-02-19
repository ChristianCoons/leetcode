/*
1415. The k-th Lexicographical String of All Happy Strings of Length n
Medium

A happy string is a string that:

    consists only of letters of the set ['a', 'b', 'c'].
    s[i] != s[i + 1] for all values of i from 1 to s.length - 1 (string is 1-indexed).

For example, strings "abc", "ac", "b" and "abcbabcbcb" are all happy strings and strings "aa", "baa" and "ababbc" are not happy strings.

Given two integers n and k, consider a list of all happy strings of length n sorted in lexicographical order.

Return the kth string of this list or return an empty string if there are less than k happy strings of length n.
*/

using Microsoft.VisualBasic;

namespace Solutions.GetHappyString
{
public class Solution {
    public string GetHappyString(int n, int k) {
        Console.WriteLine($"n: {n}, k: {k}");
        string res = "";
        int possible = 3;
        if (n <= 0 ){
            return res;
        }
        else if (n > 1){
            possible = possible * (int)(Math.Pow(2, n - 1));
            Console.WriteLine(possible);
        }

        if (k > possible){
            return res;
        }

        List<string> happyStrings = new List<string>();

        genHappyString(n, "", happyStrings);

        Console.WriteLine(string.Join(",", happyStrings));
        Console.WriteLine(happyStrings[k-1]);

        return happyStrings[k - 1];
    }

    public void genHappyString(int n, string currentString, List<string> happyStrings){
        if (currentString.Length == n){
            happyStrings.Add(currentString);
            return;
        }
        foreach (char c in new[] {'a','b','c'}){
            if (currentString.Length > 0 && currentString[currentString.Length - 1] == c){
                continue;
            }
            else{
                genHappyString(n, currentString + c, happyStrings);
            }
        }
        
    }

    public void RunTests()
    {
        GetHappyString(1,2);
        GetHappyString(2,4);
        GetHappyString(3,10);

    }


}
}
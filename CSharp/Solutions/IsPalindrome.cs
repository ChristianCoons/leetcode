namespace Solutions.IsPalindrome
{
public class Solution {
    public bool IsPalindrome(string s) {
        s = s.ToLower();
        s = string.Concat(s.Where(char.IsLetterOrDigit));
        int i = 0;
        int j = 0;
        bool isPal = true;
        if(s.Length % 2 == 0){
            i = s.Length/2 - 1;
            j = s.Length/2;
        }
        else{
            i = (int)(s.Length / 2) - 1;
            j = (int)(s.Length / 2) + 1;
        }

        while (i >= 0 && j < s.Length){
            if (s[i] != s[j]){
                isPal = false;
            }
            i--;
            j++;
        }
        
        Console.WriteLine(isPal);

        return isPal;
    }


    public void RunTests(){
        IsPalindrome("raCEcar");
        IsPalindrome("raCEacar");
        
    }
}

}
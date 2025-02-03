class Solution:
    def longestPalindrome(self, s: str) -> str:
        #print(f"Working on: {s}")

        lpCount = 0 #LongestPalindrome count
        lpWord = "" #LongestPalindrome Word
        for i in range(1, len(s)):

            #Start of Palindrom found, Palidrome wil be an even number, mid is between i-1 and i
            if s[i - 1] == s[i]:
                currentLP = f"{s[i - 1]}{s[i]}"
                #print(f"{currentLP}")

                j = i - 2
                k = i + 1
                while j >= 0 and k < len(s):
                    #print(f"{s[j]}, {s[k]}")
                    if s[j] == s[k]:
                        currentLP = f"{s[j]}{currentLP}{s[k]}"
                        #print(f"{currentLP}")
                        j -= 1
                        k += 1
                    else:
                        break
                #print(f"{j + 1}, {k - 1}")
                #print(f"{currentLP}")

                #Check and set new lp
                #print(f"{((k - 1) - (j + 1) + 1)} > {lpCount}")
                if ((k - 1) - (j + 1) + 1) > lpCount:
                    lpCount = ((k - 1) - (j + 1) + 1)
                    lpWord = currentLP
                    #print(f"New LP found: {lpWord}, count: {lpCount}")



            #Start of Palindrome found Palindorme will be an odd numer, i is the middle
            if i + 1 < len(s) and s[i - 1] == s[i + 1]:
                currentLP = f"{s[i - 1]}{s[i]}{s[i+1]}"
                #print(f"{currentLP}")
                j = i - 2
                k = i + 2

                while j >= 0 and k < len(s):
                    #print(f"{s[j]}, {s[k]}")
                    if s[j] == s[k]:
                        currentLP = f"{s[j]}{currentLP}{s[k]}"
                        #print(f"{currentLP}")
                        j -= 1
                        k += 1
                    else:
                        break
                #print(f"{j + 1}, {k - 1}")
                #print(f"{currentLP}")

                #Check and set new lp
                #print(f"{((k - 1) - (j + 1) + 1)} > {lpCount}")
                if ((k - 1) - (j + 1) + 1) > lpCount:
                    lpCount = ((k - 1) - (j + 1) + 1)
                    lpWord = currentLP
                    #print(f"New LP found: {lpWord}, count: {lpCount}")

        if lpCount == 0 and len(s) > 0:
            lpWord = s[0]
            lpCount = 1

        print(f"Word: {s}, LP: {lpWord}, count: {lpCount}")
        
        return lpWord


solution = Solution()
solution.longestPalindrome("xbaeeaby")
solution.longestPalindrome("dbbc")
solution.longestPalindrome("xbaebeaby")
solution.longestPalindrome("bb")
solution.longestPalindrome("abb")
solution.longestPalindrome("aba")
solution.longestPalindrome("caba")
solution.longestPalindrome("abac")
solution.longestPalindrome("dbbcabbaxff")
solution.longestPalindrome("a")
solution.longestPalindrome("abcd")
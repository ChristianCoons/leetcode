'''
1910. Remove All Occurrences of a Substring
Medium
Topics
Companies
Hint

Given two strings s and part, perform the following operation on s until all occurrences of the substring part are removed:

    Find the leftmost occurrence of the substring part and remove it from s.

Return s after removing all occurrences of part.

A substring is a contiguous sequence of characters in a string.
'''

class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        #print(s)
        parTuple = s.partition(part)
        while parTuple[1]:
            s = parTuple[0] + parTuple[2]
            parTuple = s.partition(part)
        #print(s)
        return s

solution = Solution()

solution.removeOccurrences("daabcbaabcbc", "abc")

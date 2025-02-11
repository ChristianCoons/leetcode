
#Overly Complicated O(n^2) Solution, should revist
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 :
            return s
        
        zzS = ""

        print(f"Working On: {s}, Rows: {numRows}")
        fStep = 2 * (numRows - 1)
        midStep = 0
        depth = 0
        while (fStep >= 0):
            i = depth
            if i < len(s):
                print(f"fStep: {fStep}, s[{i}]: {s[i]}")
                zzS = f"{zzS}{s[i]}"
            while i + fStep < len(s):
                
                if fStep != 0:
                    i += fStep    
                    if i < len(s):
                        print(f"fStep: {fStep}, s[{i}]: {s[i]}")
                        zzS = f"{zzS}{s[i]}"
                
                print(f"i: {i}, midStep: {midStep}")
                if midStep != 0 and midStep != fStep:
                    i += midStep
                    if i < len(s):
                        print(f"midStep: {midStep}, s[{i}]: {s[i]}")
                        zzS = f"{zzS}{s[i]}"
                        
                
                
            fStep = fStep - 2
            depth += 1
            midStep += 2

        print(f"{zzS}")
        return zzS

solution = Solution()

#solution.convert("0123456789", 11)
#solution.convert("0123456789", 10)
#solution.convert("0123456789", 9)
#solution.convert("0123456789", 8)
#solution.convert("0123456789", 7)
#solution.convert("0123456789", 6)
#solution.convert("0123456789", 5)
#solution.convert("0123456789", 4)
solution.convert("0123456789", 3)
#solution.convert("0123456789", 2)
#solution.convert("0123456789", 1)

solution.convert("01234", 4)
solution.convert("012", 4)
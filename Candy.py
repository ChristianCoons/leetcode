'''
There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

You are giving candies to these children subjected to the following requirements:

    Each child must have at least one candy.
    Children with a higher rating get more candies than their neighbors.

Return the minimum number of candies you need to have to distribute the candies to the children
'''
from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        candyArray = [1]
        
        for i in range(1, len(ratings)):
            candyArray.append(1)
            if ratings[i - 1] < ratings[i]:
                candyArray[i] = candyArray[i-1] + 1
        
        for j in range(len(ratings) - 2, -1, -1):
            if ratings[j] > ratings[j + 1]:
                if candyArray[j] < candyArray[j+1] + 1:
                    candyArray[j] = candyArray[j+1] + 1
        
        print(candyArray)
        return sum(candyArray)


                    




    #Nice first solution but its O(n^2) in worst case
    def candyBad(self, ratings: List[int]) -> int:
        def checkLeft(pos):
            #print(f"candyArray[{pos - 1}]:{candyArray[pos - 1]} <= candyArray[{pos}]:{candyArray[pos]}")
            if pos - 1 >= 0:
                if ratings[pos - 1] > ratings[pos] and candyArray[pos - 1] <= candyArray[pos]:
                    return True
                else:
                    return False
            else:
                return False
            
        
        def bump(pos):
            candyArray[pos] += 1
            if checkLeft(pos):
                bump(pos - 1)

        candyArray = [1]
        i = 1
        while i < len(ratings):
            if ratings[i-1] < ratings[i]:
                #print(f"ratings[i-1]:{ratings[i-1]} < ratings[i]:{ratings[i]}")
                candyArray.append(candyArray[i-1] + 1)
                #print(candyArray)
            elif ratings[i-1] == ratings[i]:
                #print(f"ratings[i-1]:{ratings[i-1]} == ratings[i]:{ratings[i]}")
                candyArray.append(1)
                #print(candyArray)
            elif ratings[i-1] > ratings[i]:
                #print(f"ratings[i-1]:{ratings[i-1]} > ratings[i]:{ratings[i]}")
                candyArray.append(1)
                if checkLeft(i):
                    bump(i - 1)
                #print(candyArray)
            i += 1

        tot = 0
        for k in range(0, len(candyArray)):
            tot += candyArray[k]

        #print(tot)
        return tot




        
solution = Solution()
#solution.candy([1,2,3,4,5])
#solution.candy([1,2,3,3,4,5])
#solution.candy([5,4,3,2,1])
#solution.candy([5,4,3,2,1,1,2,3,4,5,0])
solution.candy([2,1,2])
solution.candy([1,0,2])


        
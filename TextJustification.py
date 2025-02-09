'''Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left-justified, and no extra space is inserted between words.
'''


from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        sentences = []
        i = 0
        sentenceIndex = 0

        while i < len(words):
            width = len(words[i])
            wordLine = []
            wordLine.append(words[i])

            while i + 1 < len(words) and width + len(words[i + 1]) + 1 <= maxWidth:
                i += 1
                width += 1 + len(words[i])
                wordLine.append(words[i])
            
            
            spaces = len(wordLine) - 1
            extraSpaces = maxWidth - width
            spaceArray = []
            
            if spaces > 0:
                for j in range(0, spaces):
                    spaceArray.append(" ")
                
                index = 0
                for k in range(0, extraSpaces):
                    spaceArray[index] = spaceArray[index] + " "
                    if index < spaces - 1:
                        index += 1
                    else:
                        index = 0

            if i + 1 >= len(words) or len(wordLine) == 1:
                sentences.append(wordLine[0])
                for l in range(1, len(wordLine)):
                    sentences[sentenceIndex] = sentences[sentenceIndex] + " " + wordLine[l]
                for e in range(0, extraSpaces):
                    sentences[sentenceIndex] = sentences[sentenceIndex] + " "
            elif len(wordLine) > 0:
                sentences.append(wordLine[0])
                for l in range(1, len(wordLine)):
                    sentences[sentenceIndex] = sentences[sentenceIndex] + spaceArray[l - 1] + wordLine[l]
            
            sentenceIndex += 1
                
            #print(f"{wordLine}, spaces: {spaces}, extraSpace:{extraSpaces}")
            #print(f"spaceArray: {spaceArray}")
            #print(f"sentences: {sentences}")

            i+=1
        
        

        return sentences
            




solution = Solution()
solution.fullJustify(["This", "is", "an", "example", "of", "text", "justification.", "abbi", "g", "f", "e", "d", "c", "m", "l", "k", ], maxWidth = 16)

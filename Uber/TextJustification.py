"""
Given an array of words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is inserted between words.

Note:

A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.
Example 1:

Input:
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
Example 2:

Input:
words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
Explanation: Note that the last line is "shall be    " instead of "shall     be",
             because the last line must be left-justified instead of fully-justified.
             Note that the second line is also left-justified becase it contains only one word.
Example 3:

Input:
words = ["Science","is","what","we","understand","well","enough","to","explain",
         "to","a","computer.","Art","is","everything","else","we","do"]
maxWidth = 20
Output:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]
"""  


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        final = [[]]
        level = 0
        #final[level] = []
        for word in words:
            if sum([len(item) for item in final[level]])+ len(word) > (maxWidth - len(final[level])-1):
                level+=1
                final.append([word])
            else:
                final[level].append(word)
        return self.justify(final,maxWidth)
            
    def justify(self, wordList, maxWidth):
        final = []
        print(wordList)
        spaceSize = 1
        for lineNum in range(len(wordList)-1):
                spaceSize = 1
                numSpaces = len(wordList[lineNum])-1
                numChars = sum([ len(item) for item in wordList[lineNum]])
                length =  numChars + numSpaces
                if(length < maxWidth):
                    if numSpaces ==0:
                        spaceSize = 1
                    else:
                        spaceSize += (maxWidth-length)//numSpaces
                final.append("".join([ item + " "*spaceSize for item in wordList[lineNum]]).rstrip(" "))
        final.append("".join([ item + " "*(maxWidth - len(item)) for item in wordList[len(wordList)-1]]))
        return final
            
            
            
        
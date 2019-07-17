class Solution:
    def nextGreaterElement(self, n: int) -> int:
            strINT = str(n)
            n = [int(ele) for ele in strINT]
            i = len(n)-1
            larToRight = [len(n)-1 for ele in strINT]
            
            #to calculate the smallest larger integer to the right of an element
            for i in range(len(n)-1):
                j = i+1
                tempList = sorted(n[j:])
                while j < len(n):
                     if j == len(n)-1:
                           larToRight[i] = tempList[-1]
                           break
                     if tempList[j-i-1] < n[i]:
                           j+=1
                     else:
                           larToRight[i] = tempList[j-i-1]
                           break
            
            i = len(n)-1      

            #Loop that iterates from right to left that swaps first smaller element with smallest larger element to its right followed by sorting the remaining elements
            while i > 0:
                if n[i-1] < n[i]:
                       tempIdx  = n.index(larToRight[i-1]) 
                       tempEle =  n[i-1]
                       n[i-1] =  larToRight[i-1]
                       n[tempIdx] = tempEle
                       n[i:] = n[:i-1:-1] 
                       return int("".join([str(ele) for ele in n]))
                i-=1
      
            return -1
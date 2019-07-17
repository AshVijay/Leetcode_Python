"""
In a warehouse, there is a row of barcodes, where the i-th barcode is barcodes[i].

Rearrange the barcodes so that no two adjacent barcodes are equal.  You may return any answer, and it is guaranteed an answer exists.

 

Example 1:

Input: [1,1,1,2,2,2]
Output: [2,1,2,1,2,1]
Example 2:

Input: [1,1,1,1,2,2,3,3]
Output: [1,3,1,3,2,1,2,1]
 

Note:
 
1 <= barcodes.length <= 10000
1 <= barcodes[i] <= 10000
"""

class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        import heapq
        dict = {}
        for i in barcodes:
            if i not in dict.keys():
                dict[i] = 1
            else:
                dict[i] += 1
        heap = [[-value,key]  for key,value in dict.items()]
        heapq.heapify(heap)
        final = []
        while heap:
            element1 = heapq.heappop(heap)
            if heap:
             element2 = heapq.heappop(heap)
            else :
             final.append(element1[1])   
             return final   
            final.append(element1[1])
            final.append(element2[1])
            element1[0] +=1
            element2[0] +=1
            if element1[0] < 0:
                 heapq.heappush(heap,[element1[0],element1[1]])
            if element2[0] < 0:
                 heapq.heappush(heap,[element2[0],element2[1]])
        return final
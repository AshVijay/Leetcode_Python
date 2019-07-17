"""
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        final = []
        import heapq
        
        #To invalidate null elements
        tempList = []
        for i in range(len(lists)):
              if lists[i] != None:
                       tempList.append(lists[i])               
        lists = tempList
        if len(lists)==0:
             return None
            
        #Creating a heap
        inp = [node.val for node in lists]
        inp = [tup for tup in zip(inp,[ele for ele in range(len(lists))]) ]
        heapq.heapify(inp)
        
        #Priority queue operations
        while len(inp)!=0:
              smallest = heapq.heappop(inp)
              final.append(smallest[0])  
              lists[smallest[1]] = lists[smallest[1]].next
              if lists[smallest[1]]  != None:
                  heapq.heappush(inp, (lists[smallest[1]].val, smallest[1]))
        
        start = ListNode(final[0])
        cur = start
        
        #reconstructing the list from value list
        for i in range(1,len(final)): 
           node = ListNode(final[i])
           cur.next = node
           cur = node
        return start
              
        
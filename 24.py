"""
Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be changed.

 

Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.
"""

# Definition for singly-linked list.
# class ListNode: 
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head == None :
            return None
        elif head.next == None:
            return head 
        final = head.next
        self.recurse(head)
        return final
    
    def recurse(self,cur) :
        if(cur != None and cur.next != None): 
            temp1 = cur.next
            temp2 = temp1.next
            cur.next.next = cur
            if temp2 is not None and temp2.next is not None:
                cur.next = temp2.next
                self.recurse(temp2)
            elif temp2 is not None and temp2.next is None:
                cur.next = temp2
            else:
                cur.next = temp2
                
        else:
        
            return 0
            
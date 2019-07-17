"""
Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
"""



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution: 
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        final = head
        while( head.next  != None) :
              if (self.lookAhead(head,n+1)== True):
                    temp = head.next.next
                    head.next = temp               
                    break
              else :
                    head = head.next
        return final

    #Recursively check if the node is the 'n'th last node
    def lookAhead(self,head,n):
          while(n>0):
            if(head.next == None):
                break
            head = head.next
            self.lookAhead(head,n-1)
            
          if(n==1):
            return True
          else:
            return False
          
        
        

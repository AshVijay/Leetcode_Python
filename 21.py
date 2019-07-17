"""Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4

"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x): 
#         self.val = x
#         self.next = None




class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
         start= ListNode(0)
         cur = start
         while l1 != None and l2 != None:
                  if l1.val > l2.val :
                       cur.next = ListNode(l2.val)
                       cur = cur.next
                       l2 = l2.next 
                  elif l2.val > l1.val:
                       cur.next = ListNode(l1.val)
                       cur = cur.next
                       l1 = l1.next
                  else:
                       cur.next = ListNode(l1.val)
                       cur = cur.next 
                       cur.next = ListNode(l2.val)
                       cur = cur.next
                       l1 = l1.next
                       l2 = l2.next
         if l1 == None:
              while l2 != None:
                     cur.next = ListNode(l2.val)
                     cur = cur.next
                     l2 = l2.next
         
         else:
              while l1 != None:
                     cur.next = ListNode(l1.val)
                     cur = cur.next
                     l1 = l1.next
         return start.next              
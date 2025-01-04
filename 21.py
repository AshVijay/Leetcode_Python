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


#1

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


#2

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        k = 0
        headNode = ListNode(0, None) # save the headnode to return later
        cur = headNode

        # iterate till atleast one of the list is exhausted
        while list1 != None and list2 != None:
            if list1.val >= list2.val:
                newNode = ListNode(list2.val, None)
                cur.next = newNode
                list2 = list2.next
            else:
                newNode = ListNode(list1.val, None)
                cur.next = newNode
                list1 = list1.next
            cur = newNode    

        # if there any one of the lists are not exhausted        
        if list1 == None:
            cur.next = list2
        elif list2 == None:
            cur.next = list1

        return headNode.next
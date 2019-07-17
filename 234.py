"""

Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1 
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?

"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:    
        length = self.calcLength(head)
        if length == 1 or length == 0:
              return True
        prev = None
        count = 0 
        cur = head
    
        while count <= length//2:
             next = cur.next
             cur.next = prev
             prev = cur
             cur = next
             count+=1
             if count == length//2 :
                 if length%2==0:
                         head1 = prev
                         head2 = cur                       
                 else:
                         head1 = prev
                         head2 = cur.next   

        return self.checkPalindrome(head1,head2)
        

    def calcLength(self, head):
            count = 0 
            cur= head
            while cur!= None:
                    count+=1
                    cur = cur.next
            return count
        
    def checkPalindrome(self, head1,head2):
            while head1 != None and head2 != None:
               if head1 == None or head2 ==None :
                       return False
               if(head1.val != head2.val):
                       return False
               head1 = head1.next
               head2 = head2.next
            return True
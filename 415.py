"""
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
Accepted
"""


class Solution: 
    def addStrings(self, num1: str, num2: str) -> str:
         l1 = len(num1) if len(num1) > len(num2) else len(num2)
         l2 = len(num1) + len(num2)  - l1
         temp = num1
         if l1 != len(num1):
             num1= num2
             num2 = temp
         c= 1 
         carry = 0
         sum = 0
         while c <= l1:
                if c > l2:
                  second = 0
                else:
                  second = int(num2[-c])
                partial_sum  = (int(num1[-c])+second+carry)
                if partial_sum > 9 :
                        carry= 1
                        partial_sum = partial_sum - 10
                else:
                        carry = 0
                sum+= (10 ** (c-1)) * partial_sum
                c+=1
         if carry > 0 :
              sum+= 10 ** (c-1) 
         return str(sum)
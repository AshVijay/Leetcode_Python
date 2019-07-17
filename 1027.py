"""
Given an array A of integers, return the length of the longest arithmetic subsequence in A.

Recall that a subsequence of A is a list A[i_1], A[i_2], ..., A[i_k] with 0 <= i_1 < i_2 < ... < i_k <= A.length - 1, and that a sequence B is arithmetic if B[i+1] - B[i] are all the same value (for 0 <= i < B.length - 1).
"""
 

class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        n = len(A)
        import itertools
        res = 0
        for i in range(2,n+1):
            for sub_seq in itertools.combinations(A,i):
               sub_seq= list(sub_seq)
               if(self.check_arith(sub_seq)): 
                  if(res <= len(sub_seq)):
                      print(len(sub_seq),sub_seq)
                      res = len(sub_seq)
        
        return res
    
    def check_arith(self, lst):      
        temp_list = [ lst[ind[1]]-lst[ind[0]] for ind in itertools.product(list(range(len(lst)-1)),list(range(1,len(lst)))) if ind[0]==ind[1]-1 ]
        if (len(temp_list)==0 ):
            return False
        flag = 0
        check = temp_list[0]
        for i in temp_list:
        
          if i == check:
             flag = 1
          else :
             flag = 0
             break
        if(flag ==1):
              return True
        else :
              return False
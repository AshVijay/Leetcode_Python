class Solution:
    final = []
    def combinationSum2(self, candidates, target) :
        self.final = []
        self.recurse(candidates, target, [])
        return self.final
        
    def recurse(self, candidates , target , tempList):
        if target < 0 or len(candidates) == 0 :
              return 0
        elif target == 0 and sorted(tempList) not in self.final:
              self.final.append(sorted(tempList))   
        else: 
              tempCandidates = candidates
              
              for i in range(len(candidates)):          
                     print(i, candidates, tempCandidates)
                     tempEle  = candidates.pop(i)
                     tempList.append(tempEle)
                     self.recurse(candidates, target- tempEle, tempList)
                     tempList.pop(-1)   
                     candidates = tempCandidates
                     
obj = Solution()
obj.combinationSum2([10,1,2,7,6,1,5],8)
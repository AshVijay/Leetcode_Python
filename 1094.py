class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
            new_list = []
            for i in range(len(trips)) :
                new_list.append((trips[i][1],trips[i][0]))
                new_list.append((trips[i][2],-trips[i][0]))
            new_list.sort()
            #new_list = sorted(new_list, key= lambda x: x[0])
            temp = 0
            for i in range(len(new_list)):
                temp+= new_list[i][1]
                if temp > capacity :
                    return False
            return True 
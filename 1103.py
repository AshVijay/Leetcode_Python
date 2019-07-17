class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        count = 1
        index =0
        output = [0] * num_people
        while(candies > 0 ):
            if candies > count:
              output[index] += count
            else:
              output[index] += candies
            candies -= count
            count += 1 
            index += 1
            if(index == num_people ):
                index = 0
        
        return output
            
         
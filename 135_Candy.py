from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        children = len(ratings)
        ratings_set = set(ratings)
        
        # if all ratings are the same, return number of children
        num_stages = len(ratings_set)
        if num_stages == 1:
            return children
        
        # flatten ratings and sort
        ratings_dict = {}
        flattened_list = []
        for cur_weight, rating in enumerate(ratings_set):
            ratings_dict[rating] = cur_weight+1
            
        for rating in ratings:
            flattened_list.append(ratings_dict[rating])
        
        print(flattened_list)
        
        res_list = self.processList(flattened_list)
        
        total = sum(res_list)
        print(total)
        
        return total
    
    def processList(self, flattened_list: List[int]) -> List[int]:
        res_list = flattened_list.copy()
        
        listLen = len(flattened_list)
        # go -1, +2, -1, +2, -1, +2, ...
        
        firstIteration = True
        indexList = [-1]
        for _ in range(listLen*2):
            if firstIteration:
                indexList.append(indexList[-1]+2)
                firstIteration = False
            else:
                indexList.append(indexList[-1]-1)
                firstIteration = True
        indexList[0] = 0
        indexList[-2] = listLen-1
        indexList = indexList[:-1]
        print(indexList)
        
        prev = None
        
        iteration = 0
        for i in indexList:
            left_flat = flattened_list[i-1] if i-1 >= 0 else None
            cur = flattened_list[i]
            right_flat = flattened_list[i+1] if i+1 < len(flattened_list) else None
            
            left_sorted = res_list[i-1] if i-1 >= 0 else None
            mid_sorted = res_list[i]
            right_sorted = res_list[i+1] if i+1 < len(res_list) else None
            
            if not left_flat:
                flat_triple = sorted([cur, right_flat])
            elif not right_flat:
                flat_triple = sorted([left_flat, cur])
            else:
                flat_triple = sorted([left_flat, cur, right_flat])
                
            if not left_sorted:
                res_triple = sorted([mid_sorted, right_sorted])
            elif not right_sorted:
                res_triple = sorted([left_sorted, mid_sorted])
            else:
                res_triple = sorted([left_sorted, mid_sorted, right_sorted])
                
            
            if cur == flat_triple[0]:
                # min
                print(f"min: {cur}, {i}")
                res_list[i] = 1
                prev = 1

            elif cur == flat_triple[1]:
                # mid
                print(f"mid: {cur}, {i}")
                res_list[i] = res_triple[0]+1
                prev = res_triple[0]+1
                
                if res_triple[0] == res_triple[1]:
                    res_list[i] = res_triple[0]
                    prev = res_triple[0]

            elif cur == flat_triple[-1]:
                # max
                print(f"max: {cur}, {i}")
                if len(flat_triple) == 2:
                    # if last index, set as min
                    res_list[i] = res_triple[0]
                    prev = res_triple[0]
                else:
                    # otherwise, set as mid+1
                    res_list[i] = res_triple[1]+1
                    prev = res_triple[1]+1
            
            print(f"---> {res_list[i]}\n")

            if iteration % 2 == 0:
                if prev == res_list[i]
            
        print(res_list)
        
        iteration += 1
        
        return res_list
        
                 
                
if __name__ == '__main__':
    ratings = [5,4,4,2,2,4,4,5]
    sol = Solution()
    sol.candy(ratings)
    
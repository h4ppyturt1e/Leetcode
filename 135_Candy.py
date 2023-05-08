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
        
        res_list = flattened_list.copy()
        
        stageDict = {}
        for stage in range(1, num_stages+1):
            stageDict[stage] = []
        
        for i, rating in enumerate(flattened_list):
            stageDict[rating].append(i)
        
        res_list = flattened_list.copy()
        print(stageDict)
        
        for stage in range(1, num_stages+1):
            print('stage', stage)
            if stage == 1:
                print(f"sum: {sum(res_list)}, {res_list}")
                continue
            
            for i in stageDict[stage]:
                # if first element
                if i == 0:
                    min_val, max_val = sorted([res_list[i], res_list[i+1]])
                    # if cur is min or equal
                    if res_list[i] == min_val or min_val == max_val:
                        res_list[i] = 1
                    # if cur is max
                    else:
                        res_list[i] = min_val + 1
                
                # if last element
                elif i == len(res_list)-1:
                    min_val, max_val = sorted([res_list[i], res_list[i-1]])
                    # if cur is min or equal
                    if res_list[i] == min_val or min_val == max_val:
                        res_list[i] = 1
                    # if cur is max
                    else:
                        res_list[i] = min_val + 1
                
                # sandwiched elements
                else:
                    min_val, mid_val, max_val = sorted([res_list[i-1], res_list[i], res_list[i+1]])

                    # if cur is min
                    if res_list[i] == min_val:  
                        res_list[i] = 1
                    # if cur is mid
                    elif res_list[i] == mid_val:
                        res_list[i] = min_val + 1
                    # if cur is max
                    else:
                        res_list[i] = mid_val + 1
                
                print(f"sum: {sum(res_list)}, {res_list}")
                    
        
        
        total = sum(res_list)
        print(total)
        
        return total
        
                 
                
if __name__ == '__main__':
    ratings = [1,2,2,2,5,3,3,2,2,5,1,3,3,3]
    sol = Solution()
    sol.candy(ratings)
    
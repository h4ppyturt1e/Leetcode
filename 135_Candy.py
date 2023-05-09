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
            print(f"CURRENT STAGE: {stage}")
            if stage == 1:
                print(f"sum: {sum(res_list)}, {res_list}")
                continue
            
            for i in stageDict[stage]:
                cur = res_list[i]
                # if first element
                if i == 0:
                    min_val, max_val = sorted([res_list[i], res_list[i+1]])
                    min_flat, max_flat = sorted([flattened_list[i], flattened_list[i+1]])
                    # if cur is min or equal
                    if cur == min_val or min_flat == max_flat:
                        res_list[i] = 1
                    # if cur is max
                    else:
                        res_list[i] = min_val + 1
                
                # if last element
                elif i == len(res_list)-1:
                    min_val, max_val = sorted([res_list[i], res_list[i-1]])
                    min_flat, max_flat = sorted([flattened_list[i], flattened_list[i-1]])
                    # if cur is min or equal
                    if cur == min_val or min_flat == max_flat:
                        res_list[i] = 1
                    # if cur is max
                    else:
                        res_list[i] = min_val + 1
                
                # sandwiched elements
                else:
                    res_triple = sorted([res_list[i-1], res_list[i], res_list[i+1]])
                    flat_triple = sorted([flattened_list[i-1], flattened_list[i], flattened_list[i+1]])
                    
                    min_val, mid_val, max_val = res_triple
                    min_flat, mid_flat, max_flat = flat_triple
                    
                    if cur == min_flat: # includes case where all flats are equal
                        print("     min")
                        res_list[i] = 1 
                        
                    elif cur == mid_flat:
                        print("     mid")
                        res_list[i] = min_val + 1
                        
                        # case where flat values are equal and nothing was removed
                        if mid_val == min_val and min_flat == mid_flat == max_flat:
                            res_list[i] = min_val
                        
                        
                        
                    elif cur == max_flat and mid_flat != max_flat:
                        print("     max")
                        res_list[i] = mid_val + 1
                    else:
                        print("ERROR!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    
                    
                print(f"sum: {sum(res_list)}, {res_list}, {i}")
                    
        
        
        total = sum(res_list)
        # print(total)
        
        return total
        
                 
                
if __name__ == '__main__':
    ratings_list = [
        [1,0,2],
        [1,2,2],
        [5,4,4,2,2],
        [5,4,4,2,2,4,4,5],
        [1,2,2,2,5,3,3,2,2,5,1,3,3,3],
        [2,5,1,5,1,3,4,4,2,1,3,3,2,4,5],
        [1,1,1,2,2,2,3,3,3,4,4,4,5,5,5],
        [1,2,87,87,87,2,1]
    ]
    sol = Solution()
    
    res_list = []
    for rating in ratings_list:
        res_list.append(sol.candy(rating))
        print("=====================")

    print(res_list)
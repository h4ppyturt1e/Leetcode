from typing import List

class KVPair:
    def __init__(self, index, val):
        self.index = index
        self.val = val

    def __lt__(self, other):
        return self.val < other.val

    def __repr__(self):
        return f"({self.key}, {self.val})" 

    def __eq__(self, other) -> bool:
        return self.val == other.val and self.index == other.index
    
class Solution:
    def candy(self, ratings: List[int]) -> int:
        children = len(ratings)
        ratings_set = set(ratings)
        print(ratings_set)
        
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
                    min_res, max_res = sorted([res_list[i], res_list[i+1]])
                    min_flat, max_flat = sorted([flattened_list[i], flattened_list[i+1]])
                    # if cur is min or equal
                    if cur == min_res or min_flat == max_flat:
                        res_list[i] = 1
                    # if cur is max
                    else:
                        res_list[i] = min_res + 1
                
                # if last element
                elif i == len(res_list)-1:
                    min_res, max_res = sorted([res_list[i], res_list[i-1]])
                    min_flat, max_flat = sorted([flattened_list[i], flattened_list[i-1]])
                    # if cur is min or equal
                    if cur == min_res or min_flat == max_flat:
                        res_list[i] = 1
                    # if cur is max
                    else:
                        res_list[i] = min_res + 1
                
                # sandwiched elements
                else:
                    res_triple = sorted([KVPair(i-1, res_list[i-1]), KVPair(i, res_list[i]), KVPair(i+1, res_list[i+1])])
                    flat_triple = sorted([KVPair(i-1, flattened_list[i-1]), KVPair(i, flattened_list[i]), KVPair(i+1, flattened_list[i+1])])
                    
                    min_res, mid_res, max_res = res_triple
                    min_flat, mid_flat, max_flat = flat_triple
                    
                    if res_triple == flat_triple:
                        # no edits in past iterations
                        if cur == min_res.val:
                            res_list[i] = 1
                        elif cur == mid_res.val:
                            res_list[i] = min_res.val + 1
                        else:
                            res_list[i] = mid_res.val + 1
                            
                    else:
                        # edits in past iterations
                        # min
                        if cur == min_res.val or min_flat.val == mid_flat.val == max_flat.val:
                            res_list[i] = 1
                            
                        # mid
                        elif cur == mid_res.val:                            
                            # if previously min and now mid, set as min
                            if min_flat.index == mid_flat.index:
                                res_list[i] = min_res.val
                                print("min->mid")
                            
                            # if previously mid and still mid, set as min+1
                            elif mid_flat.index == mid_res.index:
                                res_list[i] = min_res.val + 1
                                print("mid->mid")
                                
                                # unless min and mid flats were originally equal
                                # and min is now not max
                                if min_flat.val == mid_flat.val and min_flat.index != max_res.index:
                                    res_list[i] = min_res.val
                                    print("odd case")

                        # max
                        elif cur == max_res.val:
                            # if previously min and now max, set as 1
                            if min_flat.index == max_res.index:
                                res_list[i] = 1
                                print("min->max")
                            
                            # if previously mid and now max, set as min+1
                            elif mid_flat.index == max_res.index:
                                res_list[i] = min_res.val + 1
                                print("mid->max")
                            
                            # if previously max and still max, set as mid+1
                            elif max_flat.index == max_res.index:
                                res_list[i] = mid_res.val + 1
                                print("max->max")
                                
                                # unless mid and max flats were originally equal
                                # and mid is now not min
                                if max_flat.val == mid_flat.val and mid_flat.index != min_res.index:
                                    res_list[i] = min_res.val + 1
                                    print("odd case")

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
        [1,2,87,87,87,2,1],
        [29,51,87,87,72,12]
    ]
    sol = Solution()
    
    res_list = []
    for rating in ratings_list:
        res_list.append(sol.candy(rating))
        print("=====================")

    print(res_list)
def sumRange(start, n): return (n * (start + start + n - 1)) // 2
class Solution:
    def minimumPossibleSum(self, n: int, target: int) -> int:        
        halfMark = target // 2
        
        if halfMark > n:
            totalSum = 0
            cur = 1
            totalNums = 0
            halfMark = target // 2
            while totalNums < n:
                if cur == halfMark + 1:
                    cur = target
                totalSum += cur
                # print(cur, end=",")
                cur += 1
                totalNums += 1
        
        else:
            firstHalf = sumRange(1, halfMark)
            
            secondHalf = sumRange(target, n - halfMark)
            # print(f"n: {n}, target: {target}, halfMark: {halfMark}, firstHalf: {firstHalf}, secondHalf: {secondHalf}")
            totalSum = firstHalf + secondHalf
        
        return totalSum % (10 ** 9 + 7)
    

if __name__ == '__main__':
    soln = Solution()
    tests = [(2,3), (3,3), (8,6), (63623,82276)]
    ans =   [ 4,     8,     1, 948940307]
    for i in range(len(tests)):
        curTest = tests[i]
        curAns = ans[i]
        res = soln.minimumPossibleSum(curTest[0], curTest[1])
        print(f"n: {curTest[0]}, target: {curTest[1]}")
        print(f"result: {res}, expected: {curAns}\n")
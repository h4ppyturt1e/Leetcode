def sumRange(start, n): return (n * (start + start + n - 1)) // 2
class Solution:
    def minimumPossibleSum(self, n: int, target: int) -> int:        
        halfMark = target // 2
        
        if halfMark > n:
            return sumRange(1, n) % (10 ** 9 + 7)
    
        return (sumRange(1, halfMark) + sumRange(target, n - halfMark)) % (10 ** 9 + 7)

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
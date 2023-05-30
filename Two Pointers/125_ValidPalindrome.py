class Solution:
    def isPalindrome(self, s: str) -> bool:
        combined = "".join([c.lower() for c in s if c.isalpha() or c.isdigit()])
        print(combined)
        left = combined[:len(combined)//2] if len(combined) % 2 == 0 else combined[:len(combined)//2+1]
        right = combined[len(combined)//2:][::-1]
        return left == right
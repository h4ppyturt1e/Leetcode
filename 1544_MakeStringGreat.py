class Solution:
    def makeGood(self, s: str) -> str:
        if len(s) < 2:
            return s
        
        s = list(s)
        
        i = 0
        len_s = len(s)

        while i < len_s-1:
            ci, ci2 = s[i], s[i+1]
            # same letter , one lower, one upper
            if ci.lower() == ci2.lower() and \
                ((ci.islower() and ci2.isupper()) or \
                (ci.isupper() and ci2.islower())):
                s = s[:i] + s[i+2:]
                len_s -= 2
                i -= 1 if i != 0 else i
            else:
                i += 1
        return "".join(s)
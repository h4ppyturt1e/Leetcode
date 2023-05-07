class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        disc = 1 - discount / 100
        res = ""
        
        print(disc)
        
        # enumerate the sentence
        for word in sentence.split():
            if (word[0] == "$" and word[1:].isdigit()):
                val = float(word[1:]) * disc
                print(val)
                res += f"${val:.2f} "
                continue
            res += f"{word} "
        
        return res[:-1]
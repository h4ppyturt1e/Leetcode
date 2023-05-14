from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortedDict = {}
        
        for word in strs:
            sortedWord = str(sorted(word))
            if sortedWord not in sortedDict:
                sortedDict[sortedWord] = [word]
            else:
                sortedDict[sortedWord].append(word)
        
        return [sortedDict[word] for word in sortedDict]
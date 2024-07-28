from typing import List
from collections import Counter

class Solution:
    def firstWord(self, n : int, dictionary : List[str]) -> str:
        # code here
        d = Counter(dictionary)
        for k in d:
            if d[k]>1:
                return "Invalid";
        # print(d)
        dictionary.sort()
        # print(dictionary)
        return dictionary[0]
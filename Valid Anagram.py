class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter = {}
        for char in s:
            counter[char] = counter.get(char, 0) + 1
        
        for char in t:
            if counter.get(char, 0) == 0:
                return False
            counter[char] -= 1
        for k in counter:
            if counter[k] != 0:
                return False
        return True

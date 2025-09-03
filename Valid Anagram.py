class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        present = False
        j = len(s)
        k = [i for i in range(j)]
        if j != len(t):
            return False
        for i in range(j):
            for char in t:
                if s[i] == char:
                    if i not in k:
                        return False
                    present = True
                    k.remove(i)
                    break
            if not present:
                return False
            else:
                present = False
        return True


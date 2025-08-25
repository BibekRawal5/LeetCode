
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        word = strs[0]
        j = - 1
        for i in range(1, len(strs)):
            for k, char in enumerate(word):
                if k >= len(strs[i]):
                    break
                if char == strs[i][k]:
                    j = k
                else:
                    if k != j:
                        j = -1
                        break
            print("hello ", j)
        if j == -1:
            return ''
        else:
            return word[: j + 1]

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        word = strs[0]
        j = - 1
        looped = False
        for i in range(1, len(strs)):
            looped = True
            for k, char in enumerate(word):
                print("K: ", k)
                if k >= len(strs[i]):
                    break
                if char == strs[i][k]:
                    j = k
                else:
                    if k != j:
                        if k == 0:
                            print(char)
                            j = -1
                            break
                        else:
                            break
            print("hello ", j)
        if not (looped):
            return word
        if j == -1:
            return ''
        else:
            return word[: j + 1]

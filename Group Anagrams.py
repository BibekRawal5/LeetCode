class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        is_done = {}
        answer = []
        counter = {}
        for i in range(len(strs)):
            if(is_done.get(strs[i], 0) > 0):
                continue
            is_done[strs[i]] = is_done.get(strs[i], 0) + 1
            counter[strs[i]] = {}
            for char in strs[i]:
                counter[strs[i]][char] = counter[strs[i]].get(char, 0) + 1
            cur = [strs[i]]
            for w in range(i+ 1, len(strs)):
                tmp = counter[strs[i]].copy()
                for char in strs[w]:
                    tmp[char] = tmp.get(char, 0) - 1
                is_anagram = True
                for k in tmp:
                    if tmp[k] != 0:
                        is_anagram = False
                if(is_anagram):
                    cur.append(strs[w])
                    is_done[strs[w]] = is_done.get(strs[w], 0) + 1

            
            answer.append(cur)
        return answer
                             

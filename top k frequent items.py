
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #MY
        counter = defaultdict(int)
        for n in nums:
            counter[n] += 1
        values = sorted(counter.values())
        n = 0
        answer = []
        while n < k:
            cur_val = values[-1-n]
            for key,v in counter.items():
                if v == cur_val:
                    answer.append(key)
                    n += 1
        return answer

        #bucket sort best answer
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for num, cnt in count.items():
            freq[cnt].append(num)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res

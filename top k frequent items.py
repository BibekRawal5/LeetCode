#MY
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
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



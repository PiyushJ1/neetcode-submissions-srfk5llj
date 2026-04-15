class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        kv = Counter(nums)

        d = dict(sorted(kv.items(), key=lambda x: x[1], reverse=True))
        ans = []
        
        for key, v in d.items():
            ans.append(key)


        return ans[:k]


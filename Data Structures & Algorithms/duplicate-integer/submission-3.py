class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # seen = {}
        # for num in nums:
        #     seen[num] = seen.get(num, 0) + 1
        
        # for num, freq in seen.items():
        #     if freq > 1:
        #         return True
        
        # return False

        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        
        return False





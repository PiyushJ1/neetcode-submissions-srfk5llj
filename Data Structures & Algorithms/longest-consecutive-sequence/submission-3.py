class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        ans = Counter(nums)
        final = []
        for k, v in ans.items():
            final.append(k)
        
        count = 1
        final = sorted(final)
        print(final)
        for i in range(len(final) - 1):
            if final[i + 1] - final[i] == 1:
                count += 1
            elif count < len(final) - i:
                print(i, len(final))
                count = 1
            else:
                break

        return count
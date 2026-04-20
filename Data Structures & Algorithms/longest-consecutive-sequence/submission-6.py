class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums) # get the unique values
        longest = 0 # length of longest sequence found

        for num in numSet: # loop through each num in the set
            if num - 1 not in numSet: # if the num is the FIRST number in the seq
                length = 1 
                while num + length in numSet: # increment length if there is a consecutive num in set
                    length += 1
                longest = max(longest, length) # get max of the two vals
        
        return longest

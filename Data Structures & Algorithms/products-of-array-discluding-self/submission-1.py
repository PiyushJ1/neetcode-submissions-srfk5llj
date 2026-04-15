class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []

        for i, num1 in enumerate(nums):
            prod = 1
            for j, num2 in enumerate(nums):
                if i != j:
                    prod *= num2
                
            output.append(prod)
        
        return output
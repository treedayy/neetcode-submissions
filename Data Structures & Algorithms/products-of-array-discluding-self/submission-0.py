class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(len(nums)):
            output.append(1)
            for n in range(len(nums)):
                if i != n:
                    output[i]*=nums[n]
        
        return output
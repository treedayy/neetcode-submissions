class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        left = []
        right = []
        for i in range(len(nums)):
            if i == 0:
                left.append(1)
            else:
                left.append(left[i-1] * nums[i-1])
        index = len(nums)-1
        while index >= 0:
            if index == len(nums)-1:
                right.append(1)
            else:
                right.append(right[len(right)-1] * nums[index+1])
            index-=1
        right = list(reversed(right))
        for i in range(len(nums)):
            output.append(1)
            output[i]=right[i]*left[i]

        return output
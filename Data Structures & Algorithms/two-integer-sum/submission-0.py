class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in d:
                li=[d[difference], i]
                return li
            else:
                d[nums[i]]=i
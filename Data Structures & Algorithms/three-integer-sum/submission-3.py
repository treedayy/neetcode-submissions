class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        i = 0
        j = i+1
        k = len(nums)-1
        li = []
        nums = sorted(nums)
        while (i <= len(nums)-3):
            if (i > 0 and nums[i] == nums[i-1]):
                i+=1
                j=i+1
                continue
            while (j < k):
                if (nums[i] + nums[j] + nums[k]) == 0:
                    result = [nums[i], nums[j], nums[k]]
                    li.append(result)
                    j+=1
                    k-=1
                    while (nums[j] == nums[j-1] and j < k):
                        j+=1
                elif (nums[i] + nums[j] + nums[k]) > 0:  
                    k-=1
                elif (nums[i] + nums[j] + nums[k]) < 0:
                    j+=1
            i+=1
            j=i+1
            k=len(nums)-1
        return li
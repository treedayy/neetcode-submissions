class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = 0
        newli = set(nums)
        print(newli)
        for i in newli:
            if (i-1) not in newli:
                length = 1
                while (i+length) in newli:
                    length += 1
                count = max(length, count)

            
        
        return count
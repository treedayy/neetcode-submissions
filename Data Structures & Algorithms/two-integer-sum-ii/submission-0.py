class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1
        li = []

        while (left < right):
            if ((numbers[left]+numbers[right]) == target):
                li.append(left+1)
                li.append(right+1)
                break
            elif ((numbers[left]+numbers[right]) > target):
                right-=1
            elif ((numbers[left]+numbers[right]) < target):
                left+=1
            
        return li
class Solution:
    def trap(self, height: List[int]) -> int:
        leftMax = []
        rightMax = []
        area = 0
        
        for i in range(len(height)):
            if i == 0:
                leftMax.append(height[i])
            else:
                leftMax.append(max(leftMax[i-1], height[i]))
        
        print(leftMax)
        rightmost = len(height)-1
        while rightmost >= 0:
            if rightmost == len(height)-1:
                rightMax.append(height[rightmost])
            else:
                rightMax.append(max(rightMax[-1], height[rightmost]))
            rightmost-=1
        rightMax = list(reversed(rightMax))
        print(rightMax)
            
        for i in range(len(height)):
            area += min(leftMax[i], rightMax[i]) - height[i]

        return area
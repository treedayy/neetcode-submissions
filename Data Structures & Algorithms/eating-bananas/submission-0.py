import math 
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k_min = 1
        k_max = max(piles)

        
        while k_min <= k_max:
            hours = 0
            mid = (k_min + k_max) // 2
            for i in piles:
                hours += math.ceil(i/mid)
            if hours <= h:
                k_max = mid - 1
            else:
                k_min = mid + 1

        return k_min
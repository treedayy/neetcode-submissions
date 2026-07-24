class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        l, r = 0, 1

        result = 0

        chars = set()
        
        for r in range(n):
            while s[r] in chars:
                chars.remove(s[l])
                l+=1

            chars.add(s[r])

            result = max(result, r - l + 1)
        
        return result
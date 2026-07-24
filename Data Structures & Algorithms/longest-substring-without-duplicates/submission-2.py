class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        l, r = 0, 1

        result = 0

        chars = {}
        
        for r in range(n):
            while s[r] in chars:
                del chars[s[l]]
                l+=1
            key = s[r]
            chars[key] = r

            result = max(result, r - l + 1)
        
        return result
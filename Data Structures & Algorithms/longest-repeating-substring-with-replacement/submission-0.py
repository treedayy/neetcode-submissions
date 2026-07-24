class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        l, r = 0, 1

        result = 0

        chars = {}

        for r in range(n):
            key = s[r]
            if key in chars:
                chars[key] += 1
            else:
                chars[key] = 1
            while ((r-l) - max(chars.values())) >= k:
                chars[s[l]] -= 1
                l+=1
            result = max(result, r - l + 1)
        
        return result
        
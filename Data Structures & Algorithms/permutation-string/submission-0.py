class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)

        chars = {}
        chars2 = {}

        for c in s1:
            key = c
            if key in chars:
                chars[key] += 1
            else:
                chars[key] = 1
        
        print(chars)

        for i in range(len(s2)):
            key = s2[i]
            if key in chars2:
                chars2[key] += 1
            else:
                chars2[key] = 1
            
            if i >= n:
                chars2[s2[i-n]] -= 1
                if chars2[s2[i-n]] == 0:
                    del chars2[s2[i-n]]

            if i >= n-1 and chars2 == chars:
                return True


        return False
            
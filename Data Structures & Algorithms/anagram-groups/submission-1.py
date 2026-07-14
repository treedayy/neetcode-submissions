class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        #for i in strs:
            #key = ''.join(sorted(i))
            #if key not in d:
            #    d[key] = []
            #d[key].append(i)

        for i in strs:
            count = [0] * 26
            for c in i:
                count[ord(c)-ord('a')] += 1
            key = tuple(count)    

            if key not in d:
                d[key] = []
            d[key].append(i)

        print(d)
        
        li=list(d.values())
        return li
        
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        li=[]
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        print(d)

        for i, val in d.items():
            li.append((val, i))
        
        li = list(reversed(sorted(li)))
        print(li)
        newli = []
        n=1
        for i in range(k):
            print(i)
            newli.append(li[i][1])
        return newli
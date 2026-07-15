class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        #li=[]
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        print(d)

        #for i, val in d.items():
        #    li.append((val, i))
        buckets = [[] for _ in range(len(nums) + 1)]
        #li = list(reversed(sorted(li)))
        for i, val in d.items():
            buckets[val].append(i)
        #print(li)
        buckets = list(reversed(buckets))
        print(buckets)
        newli = []
        for b in buckets:
            for num in b:
                newli.append(num)
        return newli[:k]
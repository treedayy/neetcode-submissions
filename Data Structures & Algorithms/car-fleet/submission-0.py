class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = 0
        lastFleetTime = 0
        n = len(position)
        li = []
        for i in range(n):
            li.append((position[i], speed[i]))
        li.sort()
        print(li)
        n-=1
        while n >= 0:
            position = li[n][0]
            speed = li[n][1]
            time = (target-position) / speed
            if time > lastFleetTime:
                fleets+=1
                lastFleetTime=time
            n-=1

        return fleets









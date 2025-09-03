class Solution(object):
    def minRefuelStops(self, target, startFuel, stations):
        """
        :type target: int
        :type startFuel: int
        :type stations: List[List[int]]
        :rtype: int
        """
        if len(stations) == 0:
            if startFuel < target:
                return -1
            else:
                return 0
        
        stops = 0
        cur = startFuel
        for dist, fuel in stations:
            if cur == target:
                return stops

            if cur < dist:
                return -1
            
            cur += fuel
            stops += 1
            

                

        

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
        
        stations.append([target, 0])
        stops = 0
        car_fuel = startFuel
        prev = 0
        passed_pumps = []
        covered = 0

        for pos, fuel in stations:
            dist = pos - prev
            prev = pos

            if car_fuel < dist:
                while passed_pumps and car_fuel < dist:
                    car_fuel += -heapq.heappop(passed_pumps)
                    stops += 1
                if car_fuel < dist:
                    return -1
            
            car_fuel -= dist
            heapq.heappush(passed_pumps, -fuel)

        return stops
            

                

        

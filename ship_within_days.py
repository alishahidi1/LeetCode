class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)

        cap_min = r

        def canShip(cap):
            day = 1
            cap_now = cap
            
            for w in weights:
                if cap_now < w:
                    day += 1
                    cap_now = cap
                cap_now -= w
            return day <= days
        
        while l <= r:
            cap = (l + r) // 2
            if canShip(cap):
                cap_min = min(cap_min, cap)
                r = cap - 1
            else:
                l = cap + 1
        return cap_min


class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x
        while l <= r:
            mid = (l + r) // 2
            square = mid*mid
            if square > x:
                r = mid -1
            elif square < x:
                l = mid + 1
            else: 
                return mid
        return r
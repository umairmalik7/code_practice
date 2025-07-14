import math
class Solution:
    def lcmAndGcd(self, a : int, b : int) -> List[int]:
        # code here
        gcd = math.gcd(a,b)
        lcm = (a*b) // gcd
        return [lcm, gcd]
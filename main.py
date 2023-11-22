import math
class Solution(object):
    def isPowerOfFour(self, n):
        a = sqrt(abs(n)) % 4
        if n < 0:
            return False
        elif a == 0 and n % 3 != 0 and n % 5 != 0: 
            return True
        elif n == 1 or n == 4:
            return True
        else:
            return False

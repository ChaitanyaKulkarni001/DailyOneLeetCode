# Problem : Given two binary strings a and b, return their sum as a binary string.
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a=str(a)
        b=str(b)
        def binaryToDecimal(n):
            return int(n,2)
        c= int(binaryToDecimal(a))
        d= int(binaryToDecimal(b))
        e= bin(c+d)
        ans = e[2:]
        return ans

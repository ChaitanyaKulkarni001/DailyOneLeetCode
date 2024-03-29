# Given an integer n, return the number of trailing zeroes in n!.
# Note that n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1.

class Solution:
    def trailingZeroes(self, n: int) -> int:
        fact=1
        for i in range(1,n+1):
            fact =fact*i
        # print(fact)
        j=0
        while  (fact % 10== 0):
            j+=1
            fact=fact//10
        return j

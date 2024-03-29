# Problem => You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
# Increment the large integer by one and return the resulting array of digits.

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1]=digits[-1]+1
        i=-1
        while True:
            if digits[i]==10:
                digits[i]=0
                try:
                    digits[i-1]=digits[i-1]+1
                except Exception as e:
                    digits.insert(0,1)
                i=i-1
            else:
                break
        return digits

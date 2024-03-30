# Problem : A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        lower=s.lower()
        # print(lower)
        # print(ord('0'))
        # print(ord('p'))
        # print(lower)
        smallalpha=""
        for i in lower:
            if (97<=ord(i) and ord(i)<=122)  or( 48<=ord(i) and ord(i)<=57):
                smallalpha = smallalpha + i
                # continue
                # s.remove()
        # print(smallalpha)
        reverse = smallalpha[::-1]
        # print(reverse)
        if smallalpha==reverse:
            return True
            # print("True")
        # print("False")
        return False

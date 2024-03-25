# Problem -> https://leetcode.com/problems/ransom-note/description/?envType=study-plan-v2&envId=top-interview-150
# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
# Each letter in magazine can only be used once in ransomNote.


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        lst = []
        for i in ransomNote:
            lst.append(i)
        for i in magazine:
            # print(i)
            if i in lst:
                lst.remove(i)

        if lst == []:
            return True
        return False

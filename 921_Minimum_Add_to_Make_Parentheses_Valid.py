class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        myList = []
        count = 0
        for i in s :
            if i == "(":
                myList.append(i)
            else:
                if len(myList) == 0:
                    # return len(myList) - string.index(i) - 1
                    count += 1
                    
                else:
                    myList.pop()
        count += len(myList)
        return count

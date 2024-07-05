class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        number = numRows
        lists = [[] for _ in range(number)]

        i = 0
        j = 0
        reverse = False

        # Populate lists in zigzag manner
        while i < len(s):
            lists[j].append(s[i])
            if reverse:
                j -= 1
                if j == 0:
                    reverse = False
            else:
                j += 1
                if j == number - 1:
                    reverse = True
            i += 1
            
        return ''.join([''.join(sublist) for sublist in lists])

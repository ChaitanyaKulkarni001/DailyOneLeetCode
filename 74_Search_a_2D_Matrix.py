class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        linearList = [i for linear  in matrix for i in linear]
        # print(linearList)

        left= 0
        right = len(linearList) - 1
        # mid = (left+right)/2
        while left<=right:

            mid = (left+right)//2
            # print(mid)
            if target == linearList[mid]:
                # print(target)
                return True
            elif target<linearList[mid]:
                right=mid -1
                # print(right," right")
                # print(mid," mid")
            else:
                left = mid +1
        return False

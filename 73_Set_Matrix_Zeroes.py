class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zeroes = []
        for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                        if matrix[i][j] == 0:
                                zeroes.append([i,j])
        print(zeroes)
        iis = []
        # jjs = []
        for [i,j] in zeroes:
                for k in range(len(matrix[0])+1):
                    iis.append([i,k])
                for m in range(len(matrix)+1):
                    iis.append([m,j])   
        # print(iis)
        for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                        if [i,j] in iis:
                            matrix[i][j] = 0     
        # print(matrix)
        # if matrix == Output:
        #     print("True")

            73. Set Matrix Zeroes.p

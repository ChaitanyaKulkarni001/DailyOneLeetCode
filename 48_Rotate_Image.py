You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

matA = [[1,2,3],[4,5,6],[7,8,9]]
n =3
for i in range(n):
    for j in range(i,n):
        matA[i][j], matA[j][i] = matA[j][i],matA[i][j]
        
# print(matA)
for i in range(n):
    matA[i] = matA[i][::-1]

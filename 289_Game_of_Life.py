import copy

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        neighbours =copy.deepcopy(board)
    
        result = copy.deepcopy(board)
        valid_places = []
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                valid_places.append([i,j])
        moves = [[1,1],[0,1],[-1,1],[1,0],[-1,0],[1,-1],[0,-1],[-1,-1],]
        # print(valid_places)
        for i in range(len(board)):
            for j in range(len(board[0])):
                numbers = []
                moves_of_number = []
                
                # neighbours[i][j] = []
                for [m,n] in moves:
                    if [i+m,j+n] in valid_places:
                        numbers.append(board[i+m][j+n])

                neighbours[i][j] = numbers
        # print(neighbours)
        # print("neighbours of 1st",neighbours[0][1])
        # print("Valid_places",valid_places)
        # print("board is ",board)
        # print("neighbors is ",neighbours)
        for i in range(len(board)):
            for j in range(len(board[i])):
                number = result[i][j]
                live_sells = neighbours[i][j].count(1)
                # print(live_sells)
                if number == 1:
                    if live_sells < 2 or live_sells > 3:
                        board[i][j] = 0
                        continue
                    # else:
                    #     result[i][j] = 1
                        
                else:
                    if live_sells == 3:
                        board[i][j] = 1
                        

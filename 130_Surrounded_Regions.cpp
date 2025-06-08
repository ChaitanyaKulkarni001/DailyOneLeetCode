
class Solution {
    private:
    void dfs(int row,int column,vector<vector<char>>& board,vector<vector<char>>& vis){
        vis[row][column] = 'Y';

            int delRow[] = {-1,0,1,0};
            int delColumn[] = {0,1,0,-1};

            for (int i =0 ;i<4;i++){
                int newRow = row+delRow[i];
                int newColumn = column+delColumn[i];

                if (newRow>=0 && newRow<board.size() && newColumn>=0 && newColumn<board[0].size()&& vis[newRow][newColumn]!='Y' && board[newRow][newColumn]== 'O'){
                    dfs(newRow,newColumn,board,vis);
                }
            }


    }
public:
    void solve(vector<vector<char>>& board) {
        vector<vector<char>> vis(board);
        // vector<vector<int>> vis(board);

        int rows = board.size();
        int columns = board[0].size();

        for (int i = 0 ; i < columns;i++){
            if (board[0][i] == 'O' && vis[0][i]!='Y')             dfs(0,i,board,vis);
            
        // }
        // for (int i = 0 ; i < columns;i++){
            if (board[rows-1][i] == 'O' && vis[rows-1][i]!='Y')            dfs(rows-1,i,board,vis);
           
            
        }


        for (int i = 0 ; i < rows;i++){
            if (board[i][0] == 'O' && vis[i][0]!='Y') dfs(i,0,board,vis);
            
        // }
        // for (int i = 0 ; i < rows;i++){
            if (board[i][columns-1] == 'O' && vis[i][columns-1]!='Y')
            dfs(i,columns-1,board,vis);
            
        }


        for (int i =0 ;i<rows;i++){
            for (int j = 0 ; j<columns;j++){
                if (vis[i][j]!='Y' && board[i][j] == 'O'){
                    board[i][j] = 'X';
                }
            }
        }
        


    }
};

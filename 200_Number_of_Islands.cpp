class Solution {
public:
    void bfs(int row,int column,vector<vector<int>>  &vis, vector<vector<char>> &grid,int gridRows,int gridColumns){
    vis[row][column] = 1;

    queue <pair<int,int>> q;
    q.push({row,column});

    while (!q.empty()){
        
        int row = q.front().first;
        int column  = q.front().second;
        q.pop();
        for (int i =-1 ;i<=1;i++){
            for (int j = -1;j<=1;j++){

                if ( (i == 0 && j !=0 )|| ( j==0 && i!=0 )){

                    int nrow = row + i;
                    int ncolumn = column + j;
                    
                    
                    if (nrow>=0 && nrow < gridRows && ncolumn>=0 && ncolumn < gridColumns && grid[nrow][ncolumn] =='1' && !vis[nrow][ncolumn]){
                        vis[nrow][ncolumn] = 1;
                        q.push({nrow,ncolumn});
                    }
                }
            }
        }
    }

}

    int numIslands(vector<vector<char>>& grid) {
     int gridRows = grid.size();
        int gridColumns  = grid[0].size();
        vector<vector<int>> vis(gridRows,vector<int>(gridColumns,0));
        int cnt = 0;
        for (int row = 0;row< gridRows;row++){
            for (int column = 0;column<gridColumns;column++){
                if (!vis[row][column] && grid[row][column] =='1'){
                    bfs(row,column,vis,grid, gridRows,gridColumns);
                    cnt++;
                }
            }
        }
        return cnt;   
    }
};

#include<iostream>
#include<queue>
#include<vector>

using namespace std;
class Solution{
    public:
    queue <int> q;
    vector < int > bfs;
    vector<int> bfsOfGraph(int V, vector<int> adj[] ){
        vector<int> vis(V,0);
        vis[0] = 1;
        queue<int> q;
        q.push(0);
        while(!q.empty()){
            int node = q.front();
            q.pop();
            
            bfs.push_back(node);

            for (auto it  :adj[node]){
                if (!vis[it]){
                    vis[it] =1;
                    q.push(it);
                }

            }
            
        }
        return bfs;
    }
};
int main(){	
    vector<int> vis(5,0);
    cout << vis[0]<< " " << vis[4];
    return 0;
}

class Solution {
    unordered_map<string, vector<pair<string,double>>> adjList;
    unordered_map<string, bool> visited;
    double queryAns;
public:
    bool dfs(string start, string end, double currProduct){
        if (adjList.find(start) == adjList.end() || adjList.find(end) == adjList.end()){
            return false;
        }

        if (start == end && adjList.find(start)!=adjList.end()){
            queryAns = currProduct;
            return true;
        }

        bool temp = false;
        visited[start] = true;

        for ( int i = 0;i<adjList[start].size();i++){
                if (!visited[adjList[start][i].first]){
                    temp = dfs(adjList[start][i].first,end,currProduct*adjList[start][i].second);
                    if (temp) break;
                }
        }
        visited[start] = false;
        return temp;
    }
    vector<double> calcEquation(vector<vector<string>>& equations, vector<double>& values, vector<vector<string>>& queries) {
        vector<double> ans(queries.size());
        set<string> validVariables;
        for (int i =0 ; i < equations.size();i++){
            adjList[equations[i][0]].push_back({equations[i][1],values[i]});
            adjList[equations[i][1]].push_back({equations[i][0],1/values[i]});
            visited[equations[i][0]] = false;
            visited[equations[i][1]] = false;
        }

        for (int i = 0;i<queries.size();i++){
        queryAns = 1;
        bool pathFound = dfs(queries[i][0],queries[i][1],1);

        if (pathFound) ans[i] = queryAns;
        else ans[i] = -1;
            
        }
        return ans;
    }
};

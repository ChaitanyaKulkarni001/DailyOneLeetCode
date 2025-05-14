class Solution {
public:
     vector<vector<int>> generate(int numRows) {
        vector<vector<int>> result;

        for (int currentRow = 0; currentRow < numRows; ++currentRow) {
            vector<int> temp = {1};
            long long prev = 1;

            for (int i = 1; i <= currentRow; ++i) {
                prev = prev * (currentRow - i + 1) / i;
                temp.push_back(static_cast<int>(prev));
            }

            result.push_back(temp);
        }

        return result;
    }
};

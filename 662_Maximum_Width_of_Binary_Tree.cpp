/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
using ULL = unsigned long long ;
    int widthOfBinaryTree(TreeNode* root) {
        
        queue <pair<TreeNode*,ULL>> q;
        q.push({root,0});
        ULL first,last,ans=0;
        while (!q.empty()){

            int size = q.size();
            ULL mmin = q.front().second;
            for (int i = 0;i<size;i++){
                pair<TreeNode*,ULL> temp = q.front();
                q.pop();

                if (i == 0){
                     first  = temp.second-mmin;
                }
                if (i == size-1)
                     last = temp.second-mmin;

                if (temp.first->left) q.push({temp.first->left, 2*(temp.second-mmin)+1});
                if (temp.first->right) q.push({temp.first->right, 2*(temp.second-mmin)+2});

            }
            ans = max(ans,last-first+1);

        }
        return ans;
    }
};

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
    vector<double> averageOfLevels(TreeNode* root) {
         queue<TreeNode*> q;
        vector<double> result;

        // vector<int> 
        q.push(root);

        while(!q.empty()){
            int levelSize = q.size();
        double levelSum=0;
        for(int i=0;i<levelSize;i++){

        
             TreeNode* node = q.front();
        q.pop();
          levelSum += node->val;
        // cout << node->val << " ";

        // pushing left child and rightchild if they exists.
        if (node->left != nullptr)
            q.push(node->left);
        if (node->right != nullptr)
            q.push(node->right);
        }
       result.push_back(levelSum/levelSize);
}
    return result;
    }
};

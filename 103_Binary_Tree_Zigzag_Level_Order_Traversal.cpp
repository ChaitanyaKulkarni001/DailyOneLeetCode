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
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        if (root==nullptr){
            return {};
        }
           vector<vector<int>> res;
        queue<TreeNode*> q ;
        q.push(root);
        bool invert = true;
        vector<int> internal ;
        int currentLevel = 0;
        while (!q.empty()){
            res.push_back({});
            int size = q.size();
            for (int i=0;i<size;i++){
            TreeNode* temp = q.front();
            q.pop();
            // internal.push_back(temp->val);
                res[currentLevel].push_back(temp->val);

            // cout << temp->val << " ";
           
               
                if (temp->left!=nullptr) q.push(temp->left);
                if (temp->right!=nullptr) q.push(temp->right);
             
            
            
            // for (int i=0;i<internal.size();i++){
            //     cout << "INTERNAL "<< internal[i]<<" ";
            // }
            // res.push_back(internal);
        }
        if (!invert){
            reverse(res[currentLevel].begin(),res[currentLevel].end());
        }
        invert=!invert;
        currentLevel++;
        
    }
        
    
    
    return res;
    }
    
};

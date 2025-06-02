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
queue<TreeNode*> q;
void Traverse(TreeNode* root){

            // while (true){
                // cout << root->val << " ";
                q.push(root);
                if (root->left!=nullptr) Traverse(root->left);
                if (root->right!=nullptr) Traverse(root->right);
            }
void flatten(TreeNode* root) {
            if (root==nullptr){
                return ;
            }
            Traverse(root);
            TreeNode* Pointer = root;
            q.pop();
            while (!q.empty()){
                TreeNode* temp = q.front();
                q.pop();
                Pointer->right = temp;
                Pointer->left = nullptr;
                Pointer = Pointer->right;
            }
        // }
    }
};

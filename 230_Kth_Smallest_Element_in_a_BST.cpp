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
    vector <int> numbers;
        void traverse(TreeNode* root){
            if  (root!=nullptr){
                traverse(root->left);
                numbers.push_back(root->val);
                traverse(root->right);
            }
        }
        int kthSmallest(TreeNode* root, int k) {
            traverse(root);
            // sort(numbers.begin(),numbers.end());
            return numbers[k-1];
        }
};

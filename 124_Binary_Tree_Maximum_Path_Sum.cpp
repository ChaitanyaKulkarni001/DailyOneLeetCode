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
   
int travel(TreeNode* root, int& sum){
        int leftSum = 0;
        int rightSum = 0;
        if (root == nullptr){
            return 0;
        }
        
        if (root ->left)  leftSum = max(0,travel(root->left,sum));
        if (root ->right)  rightSum =  max(travel(root->right,sum),0);

        sum = max(sum,leftSum+rightSum+root->val);
        return root->val + max(leftSum,rightSum);
    }
    int maxPathSum(TreeNode* root) {
    int sum = INT_MIN;
    travel(root,sum);
    return sum;

    }
};

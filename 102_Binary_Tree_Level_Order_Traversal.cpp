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
    vector<vector<int>> usingqueue(TreeNode* root){
            if (root == nullptr){
                return {};
            }

            queue<TreeNode*> q;
            q.push(root);
            vector<vector<int>> finalAns;
            int currentLevel =0;
            vector<int> currentNodes;
            while (!q.empty()){
                finalAns.push_back({});
                int size = q.size();

                for (int i=0;i<size;i++){
                    TreeNode* tn = q.front();
                    q.pop();

                    finalAns[currentLevel].push_back(tn->val);

                    if (tn->left != nullptr){
                        q.push(tn->left);
                    }
                    if (tn->right!=nullptr){
                        q.push(tn->right);
                    }
                }
                currentLevel++;
            }
            return finalAns;
    }
    vector<vector<int>> levelOrder(TreeNode* root) {
       return  usingqueue(root);
    }
};

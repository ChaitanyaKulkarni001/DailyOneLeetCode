/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};
*/

class Solution {
public:
    Node* printer(Node *node, unordered_map<Node *, Node *> &mp)
    {
        vector<Node *> Neighbour;
        Node *clone = new Node();
        clone->val = node->val;
        mp[node] = clone;
        for (auto it : node->neighbors)
        {
            if (mp.find(it) != mp.end())
            {
                Neighbour.push_back(mp[it]);
            }
            else
            {
                Neighbour.push_back(printer(it, mp));
            }
           
        }
         clone->neighbors = Neighbour;
            return clone;
    }

    Node* cloneGraph(Node* node) {
         if (node == nullptr)
        return node;
    Node *newNode = new Node(); // node->

    if (node->neighbors.size() == 0)
    {
        newNode->val = node->val;
        return newNode;
    }
    // newNode->val = node->val;
    unordered_map<Node *, Node *> mp;
    // mp[node] = newNode;
    // copy(node,newNode);
    // q.push(node);
    return printer(node, mp);
    }
};

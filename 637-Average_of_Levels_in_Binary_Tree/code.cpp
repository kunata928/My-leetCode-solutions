/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

class Solution {
public:
    vector<double> averageOfLevels(TreeNode* root) {
        queue<TreeNode* > queue;
        vector<double> res;
        queue.push(root);
        while(! queue.empty()){
            long tmp = 0;
            int size = queue.size();
            for (int i = 0; i < size; ++i){
                TreeNode* t = queue.front();
                queue.pop();
                if (t -> left){
                    queue.push(t -> left);
                }
                if (t -> right){
                    queue.push(t -> right);
                }
                tmp += t -> val;
            }
            res.push_back((double)tmp/size);
        }
        return res;
    }
};
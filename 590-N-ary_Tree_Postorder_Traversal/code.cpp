/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> children;

    Node() {}

    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};
*/
class Solution {
public:
    vector<int> postorder(Node* root) {
        if (root == NULL){
            return {};
        }
        
        vector<int> res;
        stack<Node*> st;
        st.push(root);
        while(!st.empty()){
            Node* tmp = st.top();
            st.pop();
            for (int i = 0; i < tmp->children.size(); i++){
                st.push(tmp->children[i]);
            }
            res.push_back(tmp->val);
        }
        reverse(res.begin(), res.end());
        return res;
        
        
    }
};
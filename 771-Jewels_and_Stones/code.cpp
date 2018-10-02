class Solution {
public:
    int numJewelsInStones(string J, string S) {
        int summ=0; 
        int i;int j;
        for (i=0; i < J.length(); i++){
            for (j=0; j < S.length(); j++){
                if (J[i]==S[j]){
                    summ++;
                }
            }
        }
        return summ;
    }
};
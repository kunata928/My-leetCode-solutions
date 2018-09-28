#include <math.h>
class Solution {
public:
    vector<vector<int>> flipAndInvertImage(vector<vector<int>>& A) {
        int i,j;
        int N = A.size();
                
        for (i=0; i < N; i++){
            for (j=0; j < (N+1)/2 ; ++j){
                int tmp = A[i][j];
                A[i][j] = !A[i][N-j-1];
                A[i][N-j-1] = !tmp;
            }
        }
        return A;
    }
};
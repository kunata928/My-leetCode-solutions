#include <algorithm>
class Solution {
public:
    int maxIncreaseKeepingSkyline(vector<vector<int>>& grid) {
        int N = grid.size();
        int sum = 0;
        vector<int> Top(N);
        vector<int> Left(N);      
        int i,j;
        
        for(i=0; i<N; i++){
            for(j=0; j<N; j++){
                if (grid[i][j] > Left[i]){
                    Left[i] = grid[i][j];
                }
                if (grid[i][j] > Top[j]){
                    Top[j] =  grid[i][j];
                }
            }
        }
        
        for(i=0; i<N; i++){
            for(j=0; j<N; j++){
                sum += min(Left[i],Top[j]) - grid[i][j];
            }
        }
        
        return sum;
    }
};
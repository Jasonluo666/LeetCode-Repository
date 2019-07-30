class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        if(matrix.size() < 2)
            return;
        
        int n = matrix.size() - 1;
        int iteration = (int) (n / 2);
        
        // iteration from 0,0 -> center n/2,n/2
        for(int i = 0; i <= iteration; i++){
            for(int j = 0; j < n - 2 * i; j++){
                cout << i << j << endl;
                int temp = matrix[i][i + j];
                matrix[i][i + j] = matrix[n - i - j][i];
                matrix[n - i - j][i] = matrix[n - i][n - i - j];
                matrix[n - i][n - i - j] = matrix[i + j][n - i];
                matrix[i + j][n - i] = temp;
            }
        }
    }
};
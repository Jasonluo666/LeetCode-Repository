class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        map<char, bool> row_hash[9];
        map<char, bool> col_hash[9];
        map<char, bool> block_hash[9];
        
        for(int i = 0; i < board.size(); i++)
            for(int j = 0; j < board[0].size(); j++){
                if(board[i][j] == '.')
                    continue;
                
                int block_no = ((int) (i / 3)) * 3 + (int) (j / 3);
                
                if(row_hash[i].find(board[i][j]) == row_hash[i].end()
                  and col_hash[j].find(board[i][j]) == col_hash[j].end()
                  and block_hash[block_no].find(board[i][j]) == block_hash[block_no].end()){
                    row_hash[i][board[i][j]] = true;
                    col_hash[j][board[i][j]] = true;
                    block_hash[block_no][board[i][j]] = true;
                }
                else
                    return false;
            }
        
        return true;
    }
};
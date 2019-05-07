class Tire(object): # using Tire DS
    def __init__(self):
        self.root = {}
        self.ans = []
        
    def insert(self, word):
        pointer = self.root
        for element in word:
            if element in pointer:
                pointer = pointer[element]
            else:
                pointer[element] = {}
                pointer = pointer[element]
        pointer['*'] = True
    
    def search(self, board, i, j, node=None, word=""):
        if node is None:
            node = self.root
        
        if not 0 <= i < len(board) or not 0 <= j < len(board[0]) or board[i][j] == '*' or board[i][j] not in node:
            return
        
        temp = board[i][j]
        board[i][j] = '*'
        
        this_node = node[temp]
        this_word = word + temp
        if '*' in this_node and this_node['*'] == True:
            self.ans.append(this_word)
            this_node['*'] = False
        
        self.search(board, i + 1, j, this_node, this_word)
        self.search(board, i - 1, j, this_node, this_word)
        self.search(board, i, j + 1, this_node, this_word)
        self.search(board, i, j - 1, this_node, this_word)
        
        board[i][j] = temp
        

class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        
        tire = Tire()
        for word in words:
            tire.insert(word)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                tire.search(board, i, j)
        
        return tire.ans
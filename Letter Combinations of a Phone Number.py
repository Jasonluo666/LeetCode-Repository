class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        
        ans = []
        num2letter = ['abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
        
        for number in digits:
            pre_ans = []
            
            # append new letters to the previous letter sequences -> like expending a tree
            if not ans:
                for letter in num2letter[int(number) - 2]:
                    pre_ans.append(letter)
            else:
                for letter in num2letter[int(number) - 2]:
                    for exist_letter in ans:
                        pre_ans.append(exist_letter + letter)
            
            ans = pre_ans.copy()
        
        return ans
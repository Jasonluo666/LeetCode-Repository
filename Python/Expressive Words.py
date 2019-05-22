class Solution(object):
    def expressiveWords(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        
        def validate(S, word):
            i = j = 0
            while i < len(S):
                if j < len(word) and S[i] == word[j]:
                    i += 1
                    j += 1
                elif S[i - 1: i + 2] == S[i] * 3 or S[i - 2: i + 1] == S[i] * 3:
                    i += 1
                else:
                    return False
            return i == len(S) and j == len(word)
        
        
        
        return sum([validate(S, x) for x in words])
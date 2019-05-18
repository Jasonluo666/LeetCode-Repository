class Solution(object):
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        count = 0
        ans = 0
        one, two = None, None
        index = 0
        
        while index < len(tree):
            fruit = tree[index]
            if one is None:
                one = fruit
            elif two is None:
                if fruit != one:
                    two = fruit
            elif not (fruit == one or fruit == two):
                ans = max(ans, count)
                count = -1
                
                one = tree[index - 1]
                two = fruit
                
                index -= 1
                while tree[index] == one:
                    index -= 1
            count += 1
            index += 1
        
        ans = max(ans, count)
        return ans
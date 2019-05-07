class Solution:
    def numTrees(self, n: int) -> int:
        # DP -> cache the computed values
        cache = {}
        
        # depth first search -> build possible sub-trees
        def BST(min_val, max_val):
            if min_val >= max_val:
                return 1
            
            current_ans = 0
            for root_val in range(min_val, max_val + 1):
                if (min_val, root_val - 1) not in cache.keys():
                    cache[(min_val, root_val - 1)] = BST(min_val, root_val - 1)
                if (root_val + 1, max_val) not in cache.keys():
                    cache[(root_val + 1, max_val)] = BST(root_val + 1, max_val)
                
                current_ans += cache[(min_val, root_val - 1)] * cache[(root_val + 1, max_val)]
            return current_ans
        
        return BST(1, n)
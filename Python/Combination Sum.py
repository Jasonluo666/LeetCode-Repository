class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        
        self.ans = []
        def recursive(target, sorted_candidates, chosen):
            if target == 0:
                chosen = sorted(chosen)
                if chosen not in self.ans:
                    self.ans.append(chosen)
            elif target < 0:
                return
            else:
                for element in sorted_candidates:
                    if element <= target:
                        recursive(target - element, sorted_candidates, chosen + [element])
                    else:
                        break
        
        recursive(target, sorted(candidates), [])
        return self.ans
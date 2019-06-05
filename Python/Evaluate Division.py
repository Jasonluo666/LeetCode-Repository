class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        
        equationmap = {}
        varmap = {}
        for index in range(len(equations)):
            num1, num2 = equations[index]
            k = values[index]
            
            equationmap[(num1, num2)] = k
            varmap[num1] = varmap[num2] = True
        
        ans = []
        for query in queries:
            num1, num2 = query
            
            switch = {}
            queue = [(num1, 1)]
            flag = False
            while len(queue) > 0:
                num, k = queue[0]
                queue = queue[1:]
                
                if num == num2 and num1 in varmap and num2 in varmap:
                    ans.append(k)
                    flag = True
                    break
                
                for key in equationmap.keys():
                    if num in key:
                        if key[1] == num:
                            other, new_k = key[0], 1 / equationmap[key]
                        else:
                            other, new_k = key[1], equationmap[key]
                        if other not in switch:
                            switch[other] = True
                            queue.append((other, k * new_k))
            if not flag:
                ans.append(-1.0)
        
        return ans
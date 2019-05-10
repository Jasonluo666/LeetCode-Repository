class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        if not buildings:
            return []
        
        import heapq    # use heap -> track the right boundary
        
        ans = [[buildings[0][0], buildings[0][2]]]
        heights = [buildings[0][2]]
        trace_heap = [(buildings[0][1], buildings[0][2], 0)]
        heapq.heapify(trace_heap)
        current_max = buildings[0][2]
        
        for index, building in enumerate(buildings[1:]):
            current_index = building[0]
            
            while len(trace_heap) > 0:
                next_node = heapq.heappop(trace_heap)
                
                if next_node[0] >= current_index:
                    heapq.heappush(trace_heap, next_node)
                    break
                else:
                    heights.remove(next_node[1])
                    
                    if not trace_heap:
                        if ans[-1][0] != next_node[0]:
                            ans.append([next_node[0], 0])
                        else:
                            ans[-1][1] = 0
                        current_max = 0
                    elif next_node[1] == current_max:
                        next_max = max(heights)
                        
                        if next_max != current_max:
                            if ans[-1][0] != next_node[0]:
                                ans.append([next_node[0], next_max])
                            else:
                                ans[-1][1] = next_max
                            current_max = next_max
            
            if building[2] > current_max:
                if ans[-1][0] != building[0]:
                    ans.append([building[0], building[2]])
                else:
                    ans[-1][1] = building[2]
                current_max = building[2]
            heapq.heappush(trace_heap, (building[1], building[2], index))
            heights.append(building[2])
            
        while len(trace_heap) > 0:
            next_node = heapq.heappop(trace_heap)
            heights.remove(next_node[1])
                    
            if not trace_heap:
                if ans[-1][0] != next_node[0]:
                    ans.append([next_node[0], 0])
                else:
                    ans[-1][1] = 0
            elif next_node[1] == current_max:
                next_max = max(heights)

                if next_max != current_max:
                    if ans[-1][0] != next_node[0]:
                        ans.append([next_node[0], next_max])
                    else:
                        ans[-1][1] = next_max
                    current_max = next_max
        return ans
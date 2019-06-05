class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        
        # count prerequisites of courses
        pre = [0 for _ in range(numCourses)]
        # who needs which courses
        need_by = {}
        for course, prere in prerequisites:
            if prere not in need_by:
                need_by[prere] = [course]
            else:
                need_by[prere].append(course)
            pre[course] += 1
        
        ans = []
        queue = [index for index in range(len(pre)) if pre[index] == 0]
        
        while len(queue) > 0:
            course = queue[0]
            queue = queue[1:]
            
            pre[course] = -1
            ans.append(course)
                
            if course in need_by:
                for element in need_by[course]:
                    pre[element] -= 1
                    if pre[element] == 0:
                        queue.append(element)
        
        if len(ans) < numCourses:
            return []
        else:
            return ans
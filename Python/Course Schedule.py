class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        
        prereq = [[] for _ in range(numCourses)]
        for prerequisite in prerequisites:
            prereq[prerequisite[0]].append(prerequisite[1])
        
        index = 0
        count = 0
        while index < numCourses:
            if prereq[index] is None:
                index += 1
                continue
            
            if len(prereq[index]) == 0:
                for course in range(numCourses):
                    if prereq[course] is not None and index in prereq[course]:
                        prereq[course].remove(index)
                prereq[index] = None
                count += 1
                index = 0
            else:
                index += 1
        
        return count == numCourses
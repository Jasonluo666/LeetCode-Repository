class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        
        sorted_people = sorted(people, key=lambda x:(-x[0], x[1]))
        ans = []
        for person in sorted_people:
            ans.insert(person[1], person)
        
        return ans
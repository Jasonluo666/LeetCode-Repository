# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot(object):
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution(object):
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        
        global directions, trace
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        trace = {}
        
        def dfs(robot, cur_direct, x, y):
            global directions, trace
            
            if (x, y) not in trace:
                trace[(x, y)] = True
                robot.clean()
            
            for _ in range(4):
                new_x, new_y = x + directions[cur_direct][0], y + directions[cur_direct][1]
                if (new_x, new_y) not in trace and robot.move():
                    dfs(robot, cur_direct, new_x, new_y)

                robot.turnRight()
                cur_direct += 1
                cur_direct %= 4

            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()
        
        dfs(robot, 0, 0, 0)
        return
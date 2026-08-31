'''
We will create a hashmap to quickly identify prerequisites for each numCourses
We can look at this problem as like a graph, where the connection between nodes signify a prereq. If there's a cycle, the schedule is impossible, but otherwise yes.
'''
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # create the prereq hashmap
        prereq_map = {i: [] for i in range(numCourses)} # every course number map to an empty List
        for course, prereq in prerequisites: # fill in the hashmap
            prereq_map[course].append(prereq)

        visited = set() # processed courses for loop detection

        def dfs(course):
            if course in visited:
                return False # Cycle detected. Not possible
            if not prereq_map[course]:
                return True # No prerequisite for this course

            # Else: course have prereq. Need to check those prereq courses for their requirement
            visited.add(course)
            for prereq in prereq_map[course]:
                if not dfs(prereq):
                    return False # a prereq or deeper has a cycle

            # Beyond this point, all prereq are possible. Perform post recursion clean up
            visited.remove(course) # remove from this stack so that later course won't mistake it as a cycle
            prereq_map[course] = [] # quick shortcut to save time if any later course use it as a prereq
            
            return True

        # check every courses to take into account of independent courses
        for course in range(numCourses):
            if not dfs(course):
                return False

        # confirmed: you can finish all courses in order
        return True
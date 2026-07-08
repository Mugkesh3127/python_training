from collections import defaultdict

def canFinish(numCourses, prerequisites):
    # Build adjacency list
    graph = defaultdict(list)

    for course, prereq in prerequisites:
        graph[course].append(prereq)

    visited = set()      # Courses already checked
    visiting = set()     # Courses in current DFS path

    def dfs(course):
        # Cycle found
        if course in visiting:
            return False

        # Already processed
        if course in visited:
            return True

        visiting.add(course)

        for prereq in graph[course]:
            if not dfs(prereq):
                return False

        visiting.remove(course)
        visited.add(course)

        return True

    # Check every course
    for course in range(numCourses):
        if not dfs(course):
            return False

    return True


# Example 1
numCourses = 2
prerequisites = [[1, 0]]

print(canFinish(numCourses, prerequisites))
# Output: True


# Example 2
numCourses = 2
prerequisites = [[1, 0], [0, 1]]

print(canFinish(numCourses, prerequisites))
# Output: False
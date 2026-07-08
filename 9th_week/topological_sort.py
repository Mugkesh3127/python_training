from collections import defaultdict, deque

def topological_sort(numCourses, prerequisites):
    # Build graph and in-degree array
    graph = defaultdict(list)
    indegree = [0] * numCourses

    for course, prereq in prerequisites:
        graph[prereq].append(course)
        indegree[course] += 1

    # Queue of courses with no prerequisites
    queue = deque()

    for i in range(numCourses):
        if indegree[i] == 0:
            queue.append(i)

    order = []

    while queue:
        course = queue.popleft()
        order.append(course)

        # Reduce in-degree of neighboring courses
        for neighbor in graph[course]:
            indegree[neighbor] -= 1

            if indegree[neighbor] == 0:
                queue.append(neighbor)

    # If all courses are processed, return the order
    if len(order) == numCourses:
        return order
    else:
        return []  # Cycle exists


# Example
numCourses = 4
prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]

print(topological_sort(numCourses, prerequisites))
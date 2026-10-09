from collections import deque


def can_finish_courses(courses, reqs):
    indegree = [0] * courses
    graph = [[] for _ in range(courses)]

    # Build graph and indegree array
    for course, pre in reqs:
        graph[pre].append(course)
        indegree[course] += 1

    # Start with all courses that have no prerequisites
    queue = deque(i for i in range(courses) if indegree[i] == 0)

    finished = 0

    while queue:
        course = queue.popleft()
        finished += 1

        for nxt in graph[course]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                queue.append(nxt)

    # If we've processed all courses, there's no cycle
    return finished == courses

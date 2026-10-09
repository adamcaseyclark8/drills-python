r"""TODO: port to Python.

Original JavaScript (code/graphs/course-schedule.js):

const canFinishCourses = (courses, reqs) => {
    const indegree = new Array(courses).fill(0);
    const graph = Array.from({ length: courses }, () => []);

    // Build graph and indegree array
    for (const [course, pre] of reqs) {
        graph[pre].push(course);
        indegree[course]++;
    }

    // Start with all courses that have no prerequisites
    const queue = [];
    for (let i = 0; i < courses; i++) {
        if (indegree[i] === 0) queue.push(i);
    }

    let finished = 0;

    while (queue.length > 0) {
        const course = queue.shift();
        finished++;

        for (const next of graph[course]) {
            indegree[next]--;
            if (indegree[next] === 0) queue.push(next);
        }
    }

    // If we’ve processed all courses, there’s no cycle
    return finished === courses;
};

module.exports = canFinishCourses;

"""

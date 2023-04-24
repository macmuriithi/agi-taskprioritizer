from queue import PriorityQueue

class TaskPrioritizer:
    def __init__(self, tasks, dependencies, difficulty):
        self.tasks = tasks
        self.dependencies = dependencies
        self.difficulty = difficulty

    def prioritizeTasks(self):
        taskOrder = [] # The order in which to perform the tasks
        visited = set() # The tasks that have been visited
        taskQueue = PriorityQueue() # The tasks that are ready to be processed

        # Add all tasks to the queue
        for task in self.tasks:
            taskQueue.put((self.difficulty[task], task))

        # Perform a topological sort
        while not taskQueue.empty():
            # Get the task with the highest priority
            task = taskQueue.get()[1]

            # Add the task to the task order
            taskOrder.append(task)

            # Add any dependent tasks to the queue if they are ready to be processed
            if task in self.dependencies:
                for dependentTask in self.dependencies[task]:
                    isReady = True
                    for t in self.tasks:
                        if t in self.dependencies and dependentTask in self.dependencies[t]:
                            isReady = False
                            break

                    if isReady and dependentTask not in visited:
                        taskQueue.put((self.difficulty[dependentTask], dependentTask))

            # Mark the task as visited
            visited.add(task)

        return taskOrder


tasks = ['A', 'B', 'C', 'D', 'E', 'F']
dependencies = {
    'A': ['B', 'C'],
    'D': ['B', 'E'],
    'E': ['C', 'F'],
}
difficulty = {
    'A': 3,
    'B': 1,
    'C': 2,
    'D': 4,
    'E': 2,
    'F': 1,
}

prioritizer = TaskPrioritizer(tasks, dependencies, difficulty)
taskOrder = prioritizer.prioritizeTasks()

print(taskOrder)

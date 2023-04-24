# Task Prioritizer

Task Prioritizer is a Python class that provides a method for prioritizing tasks based on their dependencies and difficulty levels  using a directed acyclic graph (DAG) and topological sort. It takes in three parameters: a list of tasks, a dictionary of dependencies, and a dictionary of difficulty levels.

```
  A(3)
 / \
B(1) C(2)
 \ / \
D(4) E(2)
       \
        F(1)
```

## Example Usage

```python
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
task_order = prioritizer.prioritize_tasks()

print(task_order)
```

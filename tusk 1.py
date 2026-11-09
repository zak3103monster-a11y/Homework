class Task:
    def __init__(self, name):
        self.name = name
        self.done = False

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add(self, task):
        self.tasks.append(task)

t = Task("Домашня робота")
m = TaskManager()
m.add(t)
print(t.name, t.done)

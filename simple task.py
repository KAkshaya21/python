class Task:
    def __init__(self, description, priority):
        self.description = description
        self.priority = priority

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, priority):
        task = Task(description, priority)
        self.tasks.append(task)

    def remove_task(self, description):
        for task in self.tasks:
            if task.description == description:
                self.tasks.remove(task)
                return True
        return False

    def list_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task.description} - Priority: {task.priority}")

    def prioritize_tasks(self):
        self.tasks.sort(key=lambda x: x.priority, reverse=True)
        print("Tasks prioritized successfully.")

    def recommend_task(self, priority):
        recommended_tasks = [task for task in self.tasks if task.priority == priority]
        if recommended_tasks:
            print(f"Recommended tasks with priority '{priority}':")
            for task in recommended_tasks:
                print(f"- {task.description}")
        else:
            print(f"No tasks found with priority '{priority}'.")

# Sample usage
task_manager = TaskManager()

task_manager.add_task("Buy groceries", "High")
task_manager.add_task("Complete project report", "Medium")
task_manager.add_task("Schedule a meeting with the team", "Low")
task_manager.add_task("Prepare presentation for the meeting", "Medium")
task_manager.add_task("Pay the bills", "High")
task_manager.add_task("Exercise", "Low")

task_manager.list_tasks()

task_manager.remove_task("Exercise")

task_manager.list_tasks()

task_manager.prioritize_tasks()

task_manager.list_tasks()

task_manager.recommend_task("High")

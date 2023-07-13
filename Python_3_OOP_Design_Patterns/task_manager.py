class Iterator:
    def __init__(self, collection):
        self._collection = collection
        self._index = 0
    
    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._collection):
            item = self._collection[self._index]
            self._index += 1
            return item
        else:
            raise StopIteration
    

class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.completed = False

    def complete(self):
        self.completed = True

    def __str__(self):
        status = "✅" if self.completed else "❌"
        return f"Название: {self.title}\nОписание: {self.description}\nСтатус: {status}\n"


class TaskList:
    _instance = None

    def __init__(self):
        self.tasks = []

    @classmethod
    def get_instance(cls):
        if not cls._instance:
            cls._instance = TaskList()
        return cls._instance

    def add_task(self, task):
        self.tasks.append(task)

    def complete_task(self, task_index):
        if task_index < len(self.tasks):
            self.tasks[task_index].complete()

    def display_tasks(self):
        iter_tasks = Iterator(self.tasks)
        for it in iter_tasks:
            print(it)


# Создание экземпляра списка задач
task_list = TaskList.get_instance()

# Создание задач и добавление их в список
task1 = Task("LeetCode", "Решить 100 задач")
task2 = Task("Hackerrank", "Решить 50 задач")
task_list.add_task(task1)
task_list.add_task(task2)

# Изменение статуса задачи и вывод списка задач
task_list.complete_task(0)
task_list.display_tasks()


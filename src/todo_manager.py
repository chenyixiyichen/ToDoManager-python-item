import os  # os模块提供了与操作系统交互的功能，比如文件路径操作，文件的存在性检查等


class ToDoManager:
    def __init__(self, file_name='../data/todo.txt'):
        self.file_name = file_name
        self.tasks = []  # 初始化列表为空
        self.load_tasks()  # 调用load_tasks方法，从文件中加载任务

    def add_task(self, task):
        # 添加任务方法，将任务添加到任务列表中
        self.tasks.append(task)
        self.save_tasks()  # 调用save_tasks方法，将更新后的任务列表保存到文件

    def view_tasks(self):
        # 查看任务方法，返回当前的任务列表
        return self.tasks  # 返回存储在self.task列表中的任务

    def delete_task(self, task_index):
        # 删除任务方法，删除指定索引位置的任务
        if 0 <= task_index <len(self.tasks):  # 检查索引是否有效，防止越界错误
            self.tasks.pop(task_index)
            self.save_tasks()

    def load_tasks(self):
        # 加载任务方法，将文件中加载任务到内存
        if os.path.exists(self.file_name):  # 检查文件是否存在
            with open(self.file_name, 'r', encoding='utf-8') as f:
                self.tasks = f.read().splitlines()  # 读取文件内容，并按行进行分隔，赋值给任务列表

    def save_tasks(self):
        # 保存任务方法，将任务列表保存到文件中
        with open(self.file_name, 'w', encoding='utf-8') as f:
            for task in self.tasks:
                f.write(task + '\n')


import tkinter as tk  # 导入tkinter库，用于创建GUI界面
from tkinter import messagebox  # 从tkinter导入messagebox，用于弹出消息框
from todo_manager import ToDoManager  # 导入自定义的ToDoManager类，用于管理代办事项


class ToDoApp:
    def __init__(self, root):
        # 构造函数，在创建ToDoApp对象时自动调用
        self.manager = ToDoManager()  # 创建ToDoManager的实例，用于管理任务

        self.root = root  # 将root窗口对象赋值给实例变量self.root
        self.root.title("To-Do List Manager")  # 设置窗口标题
        self.root.geometry('400x300')

        # 创建任务显示区
        self.task_listbox = tk.Listbox(self.root, height=10, width=40)  # 创建一个列表框，用于显示任务
        self.task_listbox.pack(pady=10)  # 将列表框放入窗口，并设置上下间距

        # 添加任务的输入框
        self.task_entry = tk.Entry(self.root, width=40)  # 创建一个文本输入框，用于创建新任务
        self.task_entry.pack(pady=5)  # 将输入框放入窗口，并设置上下间距

        # 添加按钮
        self.add_button = tk.Button(self.root, text="添加任务", command=self.add_task)  # 创建添加任务的按钮
        self.add_button.pack(pady=5)  # 将按钮放入窗口，并设置上下间距

        # 删除按钮
        self.delete_button = tk.Button(self.root, text="删除任务", command=self.delete_task)
        self.delete_button.pack(pady=5)  # 将按钮放入窗口，并设置上下间距

        # 初始化任务显示
        self.load_tasks()  # 调用load_tasks方法，加载并显示当前的任务

    def load_tasks(self):
        # 加载任务方法，从ToDoManager获取任务并显示在列表框中
        self.task_listbox.delete(0, tk.END)  # 清空列表框中的现有任务
        tasks = self.manager.view_tasks()  # 从ToDoManager获取当前任务列表
        for task in tasks:
            self.task_listbox.insert(tk.END, task)  # 将每个任务添加到列表框中

    def add_task(self):
        # 添加任务方法，从输入框获取任务并添加到任务列表中
        task = self.task_entry.get()  # 获取输入框中的文本
        if task:  # 如果输入框不为空
            self.manager.add_task(task)  # 调用ToDoManager中的add_task方法添加任务
            self.load_tasks()  # 重新加载任务列表并更新显示
            self.task_entry.delete(0, tk.END)  # 清空输入框
        else:  # 如果输入框为空
            messagebox.showwarning("警告", "请输入一个任务!")  # 弹出警告消息框，提示用户输入任务

    def delete_task(self):
        # 删除任务方法，删除选中的任务
        try:
            selected_task_index = self.task_listbox.curselection()[0]  # 获取用户在列表框中选中的任务索引
            self.manager.delete_task(selected_task_index)
            self.load_tasks()  # 重新加载任务列表并更新显示
        except IndexError:  # 如果没有选中任何任务
            messagebox.showwarning("警告", "请选择要删除的任务！")  # 弹出警告消息框，提示用户选择任务


if __name__ == '__main__':
    root = tk.Tk()  # 创建主窗口
    app = ToDoApp(root)  # 创建ToDoApp的实例，并传入主窗口
    root.mainloop()

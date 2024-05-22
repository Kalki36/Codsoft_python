import tkinter as tk
import tkinter.messagebox

class ToDoApp:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List App")
        self.tasks = []

        self.task_entry = tk.Entry(self.master, width=50)
        self.task_entry.pack(pady=10)

        self.add_button = tk.Button(self.master, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=5)

        self.task_list = tk.Listbox(self.master, width=50, height=10)
        self.task_list.pack(pady=10)

        self.delete_button = tk.Button(self.master, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(pady=5)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_list.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)

    def delete_task(self):
        selected_task = self.task_list.curselection()
        if selected_task:
            self.tasks.pop(selected_task[0])
            self.task_list.delete(selected_task[0])

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
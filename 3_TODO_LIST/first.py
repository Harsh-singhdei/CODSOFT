import tkinter as tk
from tkinter import messagebox

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Manager")
        self.root.geometry("400x400")
        self.root.configure(bg="#f0f0f0")

        self.tasks = []

        self.title_label = tk.Label(root, text="To-Do List Manager", bg="#f0f0f0", font=("Helvetica", 16))
        self.title_label.pack(pady=10)

        self.task_entry = tk.Entry(root, width=40, font=("Helvetica", 14))
        self.task_entry.pack(pady=10)

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task, bg="#4CAF50", fg="white", font=("Helvetica", 12))
        self.add_button.pack(pady=5)

        self.tasks_frame = tk.Frame(root, bg="#f0f0f0")
        self.tasks_frame.pack(pady=10, fill=tk.BOTH, expand=True)

        self.update_task_list()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append({'task': task, 'completed': False})
            self.task_entry.delete(0, tk.END)
            self.update_task_list()
        else:
            messagebox.showwarning("Input Error", "Please enter a task.")

    def update_task_list(self):
        for widget in self.tasks_frame.winfo_children(): 
            widget.destroy()

        for idx, task in enumerate(self.tasks):
            task_text = task['task']
            if task['completed']:
                task_text += " (Completed)"

            task_label = tk.Label(self.tasks_frame, text=task_text, bg="#f0f0f0", fg="black" if not task['completed'] else "gray", font=("Helvetica", 12))
            task_label.grid(row=idx, column=0, sticky="w")

            complete_button = tk.Button(self.tasks_frame, text="Complete", command=lambda idx=idx: self.complete_task(idx), bg="#2196F3", fg="white", font=("Helvetica", 10))
            complete_button.grid(row=idx, column=1, padx=5)

            delete_button = tk.Button(self.tasks_frame, text="Delete", command=lambda idx=idx: self.delete_task(idx), bg="#f44336", fg="white", font=("Helvetica", 10))
            delete_button.grid(row=idx, column=2, padx=5)

    def complete_task(self, task_index):
        self.tasks[task_index]['completed'] = True
        self.update_task_list()

    def delete_task(self, task_index):
        self.tasks.pop(task_index)
        self.update_task_list()

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()

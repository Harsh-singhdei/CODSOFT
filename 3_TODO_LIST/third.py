import tkinter as tk
from tkinter import messagebox

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Manager")
        self.root.geometry("600x600")
        self.root.configure(bg="#e0f7fa")

        self.tasks = []

        self.title_label = tk.Label(root, text="To-Do List Manager", bg="#00695c", fg="white", font=("Helvetica", 20, "bold"))
        self.title_label.pack(pady=20, padx=10, fill=tk.X)

        self.task_entry_frame = tk.Frame(root, bg="#e0f7fa")
        self.task_entry_frame.pack(pady=10)

        self.task_entry = tk.Entry(self.task_entry_frame, width=40, font=("Helvetica", 14), bg="#ffffff", fg="#00695c", highlightbackground="#004d40", highlightcolor="#004d40", highlightthickness=1, relief="solid")
        self.task_entry.pack(side=tk.LEFT, padx=(0, 10))

        self.add_button = tk.Button(self.task_entry_frame, text="Add Task", command=self.show_priority_options, bg="#00796b", fg="white", font=("Helvetica", 12, "bold"), relief="flat", padx=10, pady=5)
        self.add_button.pack(side=tk.LEFT)

        self.sort_button = tk.Button(root, text="Sort by Priority", command=self.sort_tasks, bg="#ff9800", fg="white", font=("Helvetica", 12, "bold"), relief="flat", padx=10, pady=5)
        self.sort_button.pack(pady=10)

        self.priority_frame = tk.Frame(root, bg="#b2ebf2", bd=2, relief="solid")
        self.priority_frame.pack(pady=10, fill=tk.X)
        self.priority_frame.pack_forget()

        self.tasks_frame = tk.Frame(root, bg="#e0f7fa")
        self.tasks_frame.pack(pady=10, fill=tk.BOTH, expand=True)

        self.update_task_list()

    def show_priority_options(self):
        task = self.task_entry.get()
        if not task:
            messagebox.showwarning("Input Error", "Please enter a task.")
            return
        
        self.priority_frame.pack(pady=10, fill=tk.X)
        
        for widget in self.priority_frame.winfo_children():
            widget.destroy()
        
        tk.Label(self.priority_frame, text="Select Priority (1 is highest)", bg="#b2ebf2", font=("Helvetica", 14)).pack(pady=10)
        
        self.priority_var = tk.IntVar()
        self.priority_var.set(1)

        for i in range(1, 6):
            self.create_custom_checkbox(self.priority_frame, f"Priority {i}", i)

        tk.Button(self.priority_frame, text="Set Priority", command=self.add_task, bg="#00796b", fg="white", font=("Helvetica", 12, "bold"), relief="flat", padx=10, pady=5).pack(pady=10)

    def create_custom_checkbox(self, parent, text, value):
        frame = tk.Frame(parent, bg="#b2ebf2")
        frame.pack(anchor="w", padx=20, pady=5)
        
        canvas = tk.Canvas(frame, width=20, height=20, bg="#b2ebf2", highlightthickness=0)
        canvas.pack(side=tk.LEFT)
        
        def toggle_check():
            if self.priority_var.get() == value:
                self.priority_var.set(0)
            else:
                self.priority_var.set(value)
            update_checkbox()
        
        def update_checkbox():
            canvas.delete("all")
            if self.priority_var.get() == value:
                canvas.create_rectangle(2, 2, 18, 18, outline="#00796b", fill="#00796b")
            else:
                canvas.create_rectangle(2, 2, 18, 18, outline="#00796b")
        
        canvas.bind("<Button-1>", lambda event: toggle_check())
        
        label = tk.Label(frame, text=text, bg="#b2ebf2", font=("Helvetica", 12))
        label.pack(side=tk.LEFT, padx=10)
        label.bind("<Button-1>", lambda event: toggle_check())
        
        update_checkbox()


    def add_task(self):
        task = self.task_entry.get()
        if task:
            priority = self.priority_var.get()
            self.tasks.append({'task': task, 'completed': False, 'priority': priority})
            self.task_entry.delete(0, tk.END)
            self.update_task_list()
            self.priority_frame.pack_forget()
        else:
            messagebox.showwarning("Input Error", "Please enter a task.")
            self.priority_frame.pack_forget()

    def update_task_list(self):
        for widget in self.tasks_frame.winfo_children():
            widget.destroy()

        self.tasks.sort(key=lambda x: x['priority'])

        for idx, task in enumerate(self.tasks):
            task_text = f"{task['task']} (Priority: {task['priority']})"
            if task['completed']:
                task_text += " (Completed)"

            task_label = tk.Label(self.tasks_frame, text=task_text, bg="#e0f7fa", fg="black" if not task['completed'] else "gray", font=("Helvetica", 12))
            task_label.grid(row=idx, column=0, sticky="w", padx=10, pady=5)

            complete_button = tk.Button(self.tasks_frame, text="Complete", command=lambda idx=idx: self.complete_task(idx), bg="#0288d1", fg="white", font=("Helvetica", 10, "bold"), relief="flat")
            complete_button.grid(row=idx, column=1, padx=5, pady=5)

            delete_button = tk.Button(self.tasks_frame, text="Delete", command=lambda idx=idx: self.delete_task(idx), bg="#d32f2f", fg="white", font=("Helvetica", 10, "bold"), relief="flat")
            delete_button.grid(row=idx, column=2, padx=5, pady=5)

            priority_button = tk.Button(self.tasks_frame, text="Set Priority", command=lambda idx=idx: self.set_priority(idx), bg="#ffeb3b", fg="black", font=("Helvetica", 10, "bold"), relief="flat")
            priority_button.grid(row=idx, column=3, padx=5, pady=5)

    def complete_task(self, task_index):
        self.tasks[task_index]['completed'] = True
        self.update_task_list()

    def delete_task(self, task_index):
        self.tasks.pop(task_index)
        self.update_task_list()

    def set_priority(self, task_index):
        self.priority_frame.pack(pady=10, fill=tk.X)
        
        for widget in self.priority_frame.winfo_children():
            widget.destroy()
        
        tk.Label(self.priority_frame, text="Select Priority (1 is highest)", bg="#b2ebf2", font=("Helvetica", 14)).pack(pady=10)
        
        self.priority_var = tk.IntVar()
        self.priority_var.set(self.tasks[task_index]['priority'])

        for i in range(1, 6):
            tk.Radiobutton(self.priority_frame, text=f"Priority {i}", variable=self.priority_var, value=i, bg="#b2ebf2", font=("Helvetica", 12)).pack(anchor="w", padx=20)

        tk.Button(self.priority_frame, text="Set Priority", command=lambda: self.save_priority(task_index), bg="#00796b", fg="white", font=("Helvetica", 12, "bold"), relief="flat", padx=10, pady=5).pack(pady=10)

    def save_priority(self, task_index):
        self.tasks[task_index]['priority'] = self.priority_var.get()
        self.update_task_list()
        self.priority_frame.pack_forget()

    def sort_tasks(self):
        self.tasks.sort(key=lambda x: x['priority'])
        self.update_task_list()

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()

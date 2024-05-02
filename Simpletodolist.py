import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List App")
        
        self.tasks = []
        
        self.task_var = tk.StringVar()
        
        self.create_widgets()

    def create_widgets(self):
        # Task entry
        task_entry = tk.Entry(self.master, textvariable=self.task_var, width=30)
        task_entry.grid(row=0, column=0, padx=10, pady=10)
        
        # Add Task button
        add_button = tk.Button(self.master, text="Add Task", command=self.add_task)
        add_button.grid(row=0, column=1, padx=5, pady=10)
        
        # Task list
        self.task_listbox = tk.Listbox(self.master, width=40, height=10)
        self.task_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=5)
        
        # Buttons for marking tasks as complete and deleting tasks
        mark_complete_button = tk.Button(self.master, text="Mark Complete", command=self.mark_complete)
        mark_complete_button.grid(row=2, column=0, padx=5, pady=5)
        
        delete_button = tk.Button(self.master, text="Delete Task", command=self.delete_task)
        delete_button.grid(row=2, column=1, padx=5, pady=5)

    def add_task(self):
        task = self.task_var.get().strip()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_var.set("")
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def mark_complete(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task_index = selected_task_index[0]
            self.task_listbox.itemconfig(task_index, {'bg': 'light green'})
        else:
            messagebox.showwarning("Warning", "Please select a task to mark as complete.")

    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task_index = selected_task_index[0]
            self.task_listbox.delete(task_index)
            del self.tasks[task_index]
        else:
            messagebox.showwarning("Warning", "Please select a task to delete.")

def main():
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

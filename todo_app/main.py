import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import customtkinter as ctk
from datetime import datetime


# Create table
def create_table():
    connection = sqlite3.connect("TODO.db")
    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS tasks (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    task TEXT,
                    add_date DATE,
                    due_date DATE,
                    status TEXT)""")

    connection.commit()
    cursor.close()
    connection.close()
# Constants
my_font = ("Arial", 18)

# Create App
class App(ctk.CTk):
    def __init__(self, size):
        super().__init__()
        # Configuration
        self.title("TODO APP")
        self.geometry(f"{size[0]}x{size[1]}")
        self.minsize(width=size[0], height=size[1])

        # App widgets
        self.menu = Menu(self)
        self.menu.pack(side=tk.LEFT, expand=True, fill="both")
        
        self.table = Table(self, self.menu)
        self.table.pack(side=tk.LEFT, expand=True, fill="both")


class Menu(ctk.CTkFrame):
    def __init__(self, parent: App):
        super().__init__(parent)
        # Menu entries 
        entry_width = 200
        entry_height = 50 
        self.task = ctk.CTkEntry(self, fg_color="blue", text_color=("black", "white"),placeholder_text="TASK", justify="center", width=entry_width, height=entry_height, font=my_font)
        self.task.pack(fill="x", padx=15, pady=25)

        self.due_date = ctk.CTkEntry(self, fg_color="blue", text_color=("black", "white"),placeholder_text="DUE DATE", justify="center", width=entry_width, height=entry_height, font=my_font)
        self.due_date.pack(fill="x", padx=15, pady=25)

        self.status = ctk.CTkComboBox(self, justify="center", text_color=("black", "white"), values=["Pending", "Completed"], width=entry_width, height=entry_height, font=my_font)
        self.status.set("Status")
        self.status.pack(padx=15, pady=25)

        # Switch widget to control the theme
        current_theme = ctk.get_appearance_mode()
        self.theme = ctk.CTkSwitch(self, text=current_theme, command=self.switch_event)
        self.theme.pack(side="bottom")


    def switch_event(self):
        current_theme = ctk.get_appearance_mode()
        if current_theme == "Light":
            ctk.set_appearance_mode("Dark")
            self.theme.configure(text="Dark")
        else:
            ctk.set_appearance_mode("Light")
            self.theme.configure(text="Light")


class Table(ctk.CTkFrame):
    def __init__(self, parent:App, menu: Menu):
        super().__init__(parent)
        # Table buttons
        button = Button(self, menu)
        button.pack(side="bottom")
        # Treeview style
        self.style = ttk.Style()
        self.style.configure("Treeview", font=('Helvetica', 12))  
        self.style.configure("Treeview.Heading", font=('Helvetica', 14, 'bold'), foreground="#581845")
        self.style.configure("Treeview", rowheight=30)

        self.table = ttk.Treeview(self, columns=("Task", "Add Date", "Due Date", "Status"), show='headings')
        self.table.heading("Task", text="Task", anchor="center")
        self.table.heading("Add Date", text="Add Date", anchor="center")
        self.table.heading("Due Date", text="Due Date", anchor="center")
        self.table.heading("Status", text="Status", anchor="center")

        # Center the columns
        self.table.column("Task", anchor="center")
        self.table.column("Add Date", anchor="center")
        self.table.column("Due Date", anchor="center")
        self.table.column("Status", anchor="center")

        # Pack the table
        self.table.pack(fill="both", expand=True)

        # Load table
        self.load_tasks()
    

    def load_tasks(self):
        # Delete the content
        for row in self.table.get_children():
            self.table.delete(row)

        # Add data
        connection = sqlite3.connect("TODO.db")
        cursor = connection.cursor()
        cursor.execute("""SELECT * FROM tasks""")
        rows = cursor.fetchall()
        for row in rows:
            item_id, task, add_date, due_date, status = row
            add_date = datetime.strptime(add_date, "%Y-%m-%d").date()  # Convert string to date
            due_date = datetime.strptime(due_date, "%Y-%m-%d").date()  # Convert string to date
            self.table.insert("", tk.END, values=(task, add_date, due_date, status), tags=(item_id,))


        connection.commit()
        cursor.close()
        connection.close()


class Button(ctk.CTkFrame):
    def __init__(self, parent: Table, menu: Menu):
        super().__init__(parent)
        self.parent = parent
        self.menu = menu
        self.grid_columnconfigure((0, 1, 2), weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.add = ctk.CTkButton(self, text="ADD", fg_color="blue", hover_color="#124b9c",command=self.add)
        self.add.grid(row=0, column=0, padx=10, pady=10)

        self.update = ctk.CTkButton(self, text="UPDATE", fg_color="green", hover_color="#0a9c1e", command=self.update)
        self.update.grid(row=0, column=1, padx=10, pady=10)

        self.delete = ctk.CTkButton(self, text="DELETE", fg_color="red", hover_color="#c20b0e", command=self.delete)
        self.delete.grid(row=0, column=2, padx=10, pady=10)
        
        # Counter to manage the update button click
        self.update_count = 0
    def add(self):
        task = self.menu.task.get()
        due_date = self.menu.due_date.get()
        status = self.menu.status.get()
        add_date = datetime.now().date().isoformat()
        print(status)

        # Add task to the data base
        try:
            due_date = datetime.strptime(due_date, "%Y-%m-%d").date().isoformat()
            # Handling the entries
            if task =="" or status == "Status":
                messagebox.showerror("Error", "Must fill all entries!")
            else:
                connection = sqlite3.connect("TODO.db")
                cursor = connection.cursor()
                cursor.execute("""INSERT INTO tasks (task, add_date, due_date, status)
                                VALUES (?, ?, ?, ?)""",(task, add_date, due_date, status))

                connection.commit()
                cursor.close()
                connection.close()
                self.menu.task.delete(0, tk.END)
                self.menu.due_date.delete(0, tk.END)
                self.menu.status.set("Status")
                messagebox.showinfo("Success", "Task added successfully!")
                self.parent.load_tasks()
                        
        except ValueError:
            messagebox.showwarning("Input Error", "Please enter the due date in YYYY-MM-DD format")
        
    

    def update(self):
        self.update_count += 1
        selected_item = self.parent.table.selection()[0]
        item_id = self.parent.table.item(selected_item, 'tags')[0]
        if self.update_count % 2 != 0:
            # Display the task
            connection = sqlite3.connect("TODO.db")
            cursor = connection.cursor()
            cursor.execute("""SELECT * FROM tasks WHERE id=?""", (item_id, ))
            rows = cursor.fetchall()
            _, task, _, due_date, status = rows[0]
            due_date = datetime.strptime(due_date, "%Y-%m-%d").date()  # Convert string to date
            self.menu.task.insert(0, task)
            self.menu.due_date.insert(0, due_date)
            self.menu.status.set(status)
            connection.commit()
            cursor.close()
            connection.close()
        else:
            # Get update
            new_task = self.menu.task.get()
            new_due_date = self.menu.due_date.get()
            new_status = self.menu.status.get()
            try:
                new_due_date = datetime.strptime(new_due_date, "%Y-%m-%d").date().isoformat()
                # Handling the entries
                if new_task =="" or new_status == "Status":
                    messagebox.showerror("Error", "Must fill all entries!")
                else:
                    # Apply update
                    connection = sqlite3.connect('todo.db')
                    cursor = connection.cursor()
                    cursor.execute("UPDATE tasks SET task=?, due_date=?, status=? WHERE id=?", (new_task, new_due_date, new_status, item_id))
                    connection.commit()
                    cursor.close()
                    connection.close()
                    self.menu.task.delete(0, tk.END)
                    self.menu.due_date.delete(0, tk.END)
                    self.menu.status.set("Status")
                    messagebox.showinfo("Success", "Task Updated successfully!")
                    self.parent.load_tasks()
            except ValueError:
                messagebox.showwarning("Input Error", "Please enter the due date in YYYY-MM-DD format")
    
    def delete(self):
        selected_item = self.parent.table.selection()[0]
        item_id = self.parent.table.item(selected_item, 'tags')[0]
        connection = sqlite3.connect('todo.db')
        cursor = connection.cursor()
        cursor.execute("DELETE FROM tasks WHERE id=?", (item_id,))
        connection.commit()
        cursor.close()
        connection.close()
        self.parent.table.delete(selected_item)
        messagebox.showinfo("Success", "Task deleted successfully!")


if __name__ == "__main__":
    create_table()
    app = App(size=(900, 600))
    app.mainloop()
import tkinter as tk
from tkinter import ttk, messagebox
import csv
import matplotlib.pyplot as plt

# Colors
theme_bg = "#2C3E50"
theme_fg = "#ECF0F1"
button_bg = "#E74C3C"
entry_bg = "#34495E"
list_bg = "#1ABC9C"
list_fg = "#2C3E50"

# Expense Tracker App
class ExpenseTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Expense Tracker")
        self.root.geometry("600x400")
        self.root.config(bg=theme_bg)

        # Heading
        self.heading_label = tk.Label(root, text="Expense Tracker", font=("Arial", 16, "bold"), bg=theme_bg, fg="white")
        self.heading_label.pack(pady=5)

        # **Container Frame for Input Fields & Buttons**
        self.container = tk.Frame(root, bg=theme_bg)
        self.container.pack(side=tk.LEFT, padx=30, pady=30, fill=tk.Y)

        # Labels and Entry Fields (inside container)
        ttk.Label(self.container, text="Description:", background=theme_bg, foreground=theme_fg).pack(anchor="w", pady=4)
        self.desc_entry = ttk.Entry(self.container, font=("Arial", 12))
        self.desc_entry.pack(pady=2, fill=tk.X)

        ttk.Label(self.container, text="Amount:", background=theme_bg, foreground=theme_fg).pack(anchor="w", pady=4)
        self.amount_entry = ttk.Entry(self.container, font=("Arial", 12))
        self.amount_entry.pack(pady=2, fill=tk.X)

        # Buttons (inside container)
        self.add_button = tk.Button(self.container, text="Add Expense", bg=button_bg, fg="white", command=self.add_expense)
        self.add_button.pack(pady=5, fill=tk.X)

        self.save_button = tk.Button(self.container, text="Save Expenses", bg=button_bg, fg="white", command=self.save_expenses)
        self.save_button.pack(pady=5, fill=tk.X)

        self.plot_button = tk.Button(self.container, text="Plot Expenses", bg=button_bg, fg="white", command=self.plot_expenses)
        self.plot_button.pack(pady=5, fill=tk.X)

        # Expense List (Right side)
        self.expense_list = tk.Listbox(root, bg=list_bg, fg=list_fg, font=("Arial", 12), height=12)
        self.expense_list.pack(side=tk.RIGHT, padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Load previous expenses
        self.load_expenses()

    def add_expense(self):
        description = self.desc_entry.get()
        amount = self.amount_entry.get()

        if description and amount:
            try:
                float(amount)  # Validate amount
                self.expense_list.insert(tk.END, f"{description}: ₹{amount}")
                self.desc_entry.delete(0, tk.END)
                self.amount_entry.delete(0, tk.END)
            except ValueError:
                messagebox.showerror("Error", "Amount must be a number!")
        else:
            messagebox.showerror("Error", "Please enter description and amount")

    def save_expenses(self):
        with open("expenses.csv", "w", newline="") as file:
            writer = csv.writer(file)
            for i in range(self.expense_list.size()):
                writer.writerow([self.expense_list.get(i)])
        messagebox.showinfo("Success", "Expenses saved successfully!")

    def load_expenses(self):
        try:
            self.expense_list.delete(0, tk.END)
            with open("expenses.csv", "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    self.expense_list.insert(tk.END, row[0])
        except FileNotFoundError:
            pass

    def plot_expenses(self):
        expenses = {}
        for i in range(self.expense_list.size()):
            item = self.expense_list.get(i)
            if ":" in item:
                desc, amt = item.split(": ₹")
                expenses[desc] = expenses.get(desc, 0) + float(amt)

        if expenses:
            plt.figure(figsize=(8, 5))
            plt.bar(expenses.keys(), expenses.values(), color='skyblue')
            plt.xlabel("Categories")
            plt.ylabel("Amount (₹)")
            plt.title("Expense Distribution")
            plt.xticks(rotation=45, ha="right")
            plt.show()
        else:
            messagebox.showinfo("Info", "No expenses to plot!")

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = ExpenseTracker(root)
    root.mainloop()

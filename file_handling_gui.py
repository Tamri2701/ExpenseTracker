import tkinter as tk
from tkinter import ttk, messagebox

# Function to write data to a file
def write_to_file():
    try:
        # Get the input text from Entry widget
        data = input_entry.get()
        
        # Open the file in append mode
        with open("data.txt", "a") as file:
            file.write(data + "\n")
        
        # Clear the entry field and refresh file data
        input_entry.delete(0, tk.END)
        messagebox.showinfo("Success", "Data written to file!")
        load_data_from_file()
    
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Function to read data from the file and display in Listbox
def load_data_from_file():
    try:
        # Clear the Listbox before loading new data
        listbox.delete(0, tk.END)
        
        # Read data from the file
        with open("data.txt", "r") as file:
            lines = file.readlines()
        
        # Insert each line from file into the Listbox
        for line in lines:
            listbox.insert(tk.END, line.strip())
    
    except FileNotFoundError:
        messagebox.showwarning("Warning", "No file found! Start by adding some data.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Set up the main window
root = tk.Tk()
root.title("File Handling GUI")
root.geometry("500x400")
root.config(bg="#f0f0f0")

# Style configuration using ttk
style = ttk.Style()
style.configure("TButton", font=("Arial", 12), padding=10)
style.configure("TLabel", font=("Arial", 12))
style.configure("TEntry", font=("Arial", 12))

# Add widgets for input and file interaction
input_label = ttk.Label(root, text="Enter some text:")
input_label.pack(pady=10)

input_entry = ttk.Entry(root, width=40)
input_entry.pack(pady=5)

write_button = ttk.Button(root, text="Write to File", command=write_to_file)
write_button.pack(pady=10)

read_button = ttk.Button(root, text="Load Data from File", command=load_data_from_file)
read_button.pack(pady=10)

# Add Listbox to display file data
listbox_label = ttk.Label(root, text="Data from File:")
listbox_label.pack(pady=10)

listbox = tk.Listbox(root, height=10, width=50, font=("Arial", 12))
listbox.pack(pady=10)

# Load existing data when the program starts
load_data_from_file()

# Run the Tkinter event loop
root.mainloop()

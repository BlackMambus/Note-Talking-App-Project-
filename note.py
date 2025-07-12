import tkinter as tk
from tkinter import filedialog, messagebox

# Create the main application window
root = tk.Tk()
root.title("Simple Notes App")
root.geometry("600x500")

# Create a Text widget for writing notes
text_area = tk.Text(root, font=("Arial", 14), wrap="word")
text_area.pack(expand=True, fill="both")

# Functions for file operations
def save_note():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(text_area.get(1.0, tk.END))
        messagebox.showinfo("Saved", "Note saved successfully!")

def open_note():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
        text_area.delete(1.0, tk.END)
        text_area.insert(tk.END, content)

def clear_note():
    if messagebox.askyesno("Clear", "Are you sure you want to clear the note?"):
        text_area.delete(1.0, tk.END)

# Create a menu bar
menu_bar = tk.Menu(root)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Open", command=open_note)
file_menu.add_command(label="Save", command=save_note)
file_menu.add_separator()
file_menu.add_command(label="Clear", command=clear_note)
file_menu.add_command(label="Exit", command=root.quit)
menu_bar.add_cascade(label="File", menu=file_menu)

# Attach the menu to the window
root.config(menu=menu_bar)

# Run the application
root.mainloop()


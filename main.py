import tkinter as tk
from tkinter import messagebox, filedialog
import os

# Function to save the notes
def save_notes():
    map_name = map_entry.get().strip()
    hero_name = hero_entry.get().strip()
    code = code_entry.get().strip()
    
    if not map_name or not hero_name or not code:
        messagebox.showerror("Error", "Please enter Map, Hero, and Code")
        return
    
    # Define the directory where the notes will be saved
    save_dir = os.path.join(os.path.expanduser("~"), "Desktop", "overwatch_notes")
    os.makedirs(save_dir, exist_ok=True)  # Create the directory if it doesn't exist

    # Define the full path for the file to save with the format Map_Hero_Code.txt
    file_name = f"{map_name}_{hero_name}_{code}.txt"
    file_path = os.path.join(save_dir, file_name)

    # Get the content of the text area and save it to the file
    with open(file_path, "w") as file:
        file.write(text_area.get(1.0, tk.END).strip())
    
    messagebox.showinfo("Success", f"Notes saved to {file_path}")

# Function to open a file
def open_notes():
    # Open the file dialog starting at the overwatch_notes folder
    open_dir = os.path.join(os.path.expanduser("~"), "Desktop", "overwatch_notes")
    if not os.path.exists(open_dir):
        messagebox.showerror("Error", f"Directory {open_dir} does not exist")
        return
    
    file_path = filedialog.askopenfilename(initialdir=open_dir, title="Open Note", filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")))
    
    if not file_path:
        return  # User canceled the file dialog
    
    # Extract the map, hero, and code from the filename (assuming format Map_Hero_Code.txt)
    file_name = os.path.basename(file_path)
    try:
        map_name, hero_name, code = file_name.rsplit('_', 2)
        code = code.replace(".txt", "")
        map_entry.delete(0, tk.END)
        map_entry.insert(0, map_name)
        hero_entry.delete(0, tk.END)
        hero_entry.insert(0, hero_name)
        code_entry.delete(0, tk.END)
        code_entry.insert(0, code)
    except ValueError:
        messagebox.showerror("Error", "File name format should be Map_Hero_Code.txt")
        return
    
    # Load the file content into the text area
    with open(file_path, "r") as file:
        content = file.read()
    
    text_area.delete(1.0, tk.END)  # Clear the current text
    text_area.insert(tk.END, content)

# Set up the main application window
root = tk.Tk()
root.title("Overwatch VOD Notepad")
root.geometry("500x600")
root.attributes('-topmost', True)  # Always on top

# Set the font to mimic Notepad
text_font = ("Courier", 12)


# Create a frame at the top for the map, code, and buttons
top_frame = tk.Frame(root)
top_frame.pack(side=tk.TOP, fill=tk.X, pady=5)

# Label for map input
map_label = tk.Label(top_frame, text="Map:")
map_label.pack(side=tk.LEFT, padx=5, anchor='s')

# Entry widget for the user to input the map
map_entry = tk.Entry(top_frame, width=12)
map_entry.pack(side=tk.LEFT, anchor='s')

# Label for the code input
code_label = tk.Label(top_frame, text="Code:")
code_label.pack(side=tk.LEFT, padx=5, anchor='s')

# Entry widget for the user to input the code
code_entry = tk.Entry(top_frame, width=8)
code_entry.pack(side=tk.LEFT, anchor='s')

# Label for the hero input
hero_label = tk.Label(top_frame, text="Hero:")
hero_label.pack(side=tk.LEFT, padx=5, anchor='s')

# Entry widget for the user to input the hero
hero_entry = tk.Entry(top_frame, width=10)
hero_entry.pack(side=tk.LEFT, anchor='s')

# Save button to save the notes
save_button = tk.Button(top_frame, text="Save", command=save_notes)
save_button.pack(side=tk.RIGHT, padx=5, anchor='s')

# Open button to open existing notes
open_button = tk.Button(top_frame, text="Open", command=open_notes)
open_button.pack(side=tk.RIGHT, padx=5, anchor='s')

# Create the main text area for note-taking
text_area = tk.Text(root, font=text_font, wrap=tk.WORD)
text_area.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

# Run the Tkinter event loop
root.mainloop()

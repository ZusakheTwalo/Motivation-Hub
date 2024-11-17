import tkinter as tk
from tkinter import ttk, simpledialog, messagebox
import csv

fileName = "motivationHub.csv"

def createPost():
    author = simpledialog.askstring("Create Post", "Enter your name:")
    post = simpledialog.askstring("Create Post", "Enter your motivational quote:")
    if author and post:
        with open(fileName, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([author, post, 0, ""])
        messagebox.showinfo("Success", "Post created successfully!")

def viewPost():
    window = tk.Toplevel()
    window.title("View Posts")
    window.geometry("600x400")
    window.configure(bg="#87CEEB")  # Sky blue background

    text_area = tk.Text(window, wrap=tk.WORD, font=("Helvetica", 12))
    text_area.pack(expand=True, fill='both')

    with open(fileName, 'r') as file:
        reader = csv.reader(file)
        posts = "\n".join(
            [f"Post ID: {index + 1}\nAuthor: {row[0]}\nMessage: {row[1]}\nLikes: {row[2]}\nComments: {row[3]}\n" + "="*50
             for index, row in enumerate(reader)]
        )
        text_area.insert(tk.END, posts)
    text_area.config(state=tk.DISABLED)

def likePost():
    postID = simpledialog.askinteger("Like Post", "Enter the post ID to like:")
    if postID:
        lines = []
        with open(fileName, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                lines.append(row)
        with open(fileName, 'w', newline='') as file:
            writer = csv.writer(file)
            for index, row in enumerate(lines):
                if index + 1 == postID:
                    row[2] = int(row[2]) + 1
                writer.writerow(row)
        messagebox.showinfo("Success", "Post liked successfully!")

def commentOnPost():
    postID = simpledialog.askinteger("Comment on Post", "Enter the post ID to comment on:")
    comment = simpledialog.askstring("Comment on Post", "Enter your comment:")
    if postID and comment:
        lines = []
        with open(fileName, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                lines.append(row)
        with open(fileName, 'w', newline='') as file:
            writer = csv.writer(file)
            for index, row in enumerate(lines):
                if index + 1 == postID:
                    row[3] += f"; {comment}" if row[3] else comment
                writer.writerow(row)
        messagebox.showinfo("Success", "Comment added successfully!")

def initialize_window():
    window = tk.Tk()
    window.title("Motivation Hub")
    window.geometry("600x400")
    window.config(bg="#87CEEB")  # Sky blue background
    return window

def create_menu_button(parent, text, options):
    menu = tk.Menu(parent, tearoff=0)
    for label, command in options:
        menu.add_command(label=label, command=command)
    menu_button = ttk.Menubutton(parent, text=text, menu=menu, style="TButton")
    menu_button['menu'] = menu
    return menu_button

def setup_layout(window):
    style = ttk.Style()
    style.configure("TButton", font=("Helvetica", 12), padding=10, borderwidth=2, relief="solid")
    style.map("TButton", background=[('active', '#ADD8E6'), ('!active', 'light grey')])
    style.configure("TLabel", font=("Helvetica", 12), padding=10, background="#87CEEB")
    
    title_label = ttk.Label(window, text="Motivation Hub", font=("Helvetica", 24, "bold"), background="#87CEEB")
    title_label.pack(pady=20)

    options = [("Create post", createPost),
               ("View posts", viewPost),
               ("Like post", likePost),
               ("Comment on post", commentOnPost)]
    menu_button = create_menu_button(window, "Menu", options)
    menu_button.pack(pady=10)

def main():
    window = initialize_window()
    setup_layout(window)
    window.mainloop()

if __name__ == "__main__":
    main()

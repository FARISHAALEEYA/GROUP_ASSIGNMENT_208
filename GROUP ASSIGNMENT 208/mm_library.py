import tkinter as tk
import subprocess

class MainMenuLibraryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Library System")
        self.root.geometry("500x400")
        self.root.configure(background="#F8C8DC")


        welcome_label = tk.Label(root, text='HELLO ^-^ WELCOME TO LIBRARY SYSTEM ', font=("New York", 13, "bold"), bg="#F8C8DC")
        welcome_label.pack()

        login_button = tk.Button(root, text="Login", command=self.on_login_click, bg="#EEE7DA")
        login_button.pack(pady=10)

        book_entry_button = tk.Button(root, text="Book Entry Form", command=self.on_book_entry_click, bg="#EEE7DA")
        book_entry_button.pack(pady=10)

        calculation_button = tk.Button(root, text="Calculation Book", command=self.on_calculation_book_click, bg="#EEE7DA")
        calculation_button.pack(pady=10)


    def on_login_click(self):
        subprocess.run(["python", "u_login.py"])

    def on_book_entry_click(self):
        subprocess.run(["python", "book_entry.py"])

    def on_calculation_book_click(self):
        subprocess.run(["python", "calculation.py"])


if __name__ == "__main__":
    root = tk.Tk()
    app = MainMenuLibraryApp(root)
    root.mainloop()



import tkinter as tk
from tkcalendar import DateEntry
import mysql.connector

class MainMenuLibraryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("User Login")
        self.root.geometry('500x400')
        self.root.configure(bg='#a36370')

        # Your database connection and cursor initialization
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="login"
        )
        self.mycursor = self.mydb.cursor()

        # User first name
        first_name_label = tk.Label(root, text="First Name", font=("New York", 15, "bold"), bg='#a36370', fg='#ffffff')
        first_name_label.grid(row=1, column=0, padx=5, pady=5)
        self.first_name_entry = tk.Entry(root, bd=3)
        self.first_name_entry.grid(row=1, column=1, padx=5, pady=5)

        # User last name
        last_name_label = tk.Label(root, text="Last Name", font=("New York", 15, "bold"), bg='#a36370', fg='#ffffff')
        last_name_label.grid(row=2, column=0, padx=5, pady=5)
        self.last_name_entry = tk.Entry(root, bd=3)
        self.last_name_entry.grid(row=2, column=1, padx=5, pady=5)

        # User email
        user_email_label = tk.Label(root, text="Email", font=("New York", 15, "bold"), bg='#a36370', fg='#ffffff')
        user_email_label.grid(row=3, column=0, padx=5, pady=5)
        self.user_email_entry = tk.Entry(root, bd=3)
        self.user_email_entry.grid(row=3, column=1, padx=5, pady=5)

        # User password
        user_password_label = tk.Label(root, text="Password", font=("New York", 15, "bold"), bg='#a36370', fg='#ffffff')
        user_password_label.grid(row=4, column=0, padx=5, pady=5)
        self.user_password_entry = tk.Entry(root, bd=3)
        self.user_password_entry.grid(row=4, column=1, padx=5, pady=5)

        # User gender
        self.user_gender_label = tk.StringVar(root)
        self.user_gender_label.set("Gender")
        self.trip_dropdown = tk.OptionMenu(root, self.user_gender_label, "Male", "Female")
        self.trip_dropdown.grid(row=5, columnspan=2, padx=5, pady=5)

        # User date of birth
        date_birth_label = tk.Label(root, text="Date of Birth", font=("New York", 15, "bold"))
        date_birth_label.grid(pady=10, columnspan=2)
        self.date_birth_entry = DateEntry(root, date_pattern="yyyy-mm-dd", bd=3)
        date_birth_label['background'] = "#F8C8DC"
        self.date_birth_entry.grid(pady=5, columnspan=2)

        # Save Button
        save_button = tk.Button(root, text="SUBMIT", font=("New York", 15, "bold"), bg='#a36370', fg='#ffffff',
                                command=self.submit_data)
        save_button.grid(row=8, column=0, columnspan=2)

        # Edit Button
        edit_button = tk.Button(root, text="UPDATE", font=("New York", 15, "bold"), bg='#a36370', fg='#ffffff',
                                command=self.update_data)
        edit_button.grid(row=9, column=0, columnspan=2)

    def submit_data(self):
        # Accessing class attributes using self
        self.first_name = self.first_name_entry.get()
        self.last_name = self.last_name_entry.get()
        self.user_email = self.user_email_entry.get()
        self.user_password = self.user_password_entry.get()
        self.user_gender = self.user_gender_label.get()  # Extract the string value
        self.date_birth = self.date_birth_entry.get()

        # Database insertion using class attributes
        sql = "INSERT INTO user_login (First_Name, Last_Name, User_Email, User_Password, User_Gender, Date_of_Birth) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (self.first_name, self.last_name, self.user_email, self.user_password, self.user_gender, self.date_birth)
        self.mycursor.execute(sql, val)
        self.mydb.commit()

    def update_data(self):
        self.first_name = self.first_name_entry.get()
        self.last_name = self.last_name_entry.get()
        self.user_email = self.user_email_entry.get()
        self.user_password = self.user_password_entry.get()
        self.user_gender = self.user_gender_label.get()
        self.date_birth = self.date_birth_entry.get()

        update_query = "UPDATE user_login SET First_Name=%s, Last_Name=%s, User_Password=%s, User_Gender=%s, Date_of_Birth=%s WHERE User_Email=%s"
        vals = (self.first_name, self.last_name, self.user_password, self.user_gender, self.date_birth, self.user_email)
        self.mycursor.execute(update_query, vals)
        self.mydb.commit()

if __name__ == "__main__":
    root = tk.Tk()
    app = MainMenuLibraryApp(root)
    root.mainloop()
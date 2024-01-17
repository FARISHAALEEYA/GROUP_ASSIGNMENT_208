import tkinter as tk
import mysql.connector

# Connect to your MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="register"
)

# Create a cursor object to execute SQL queries
mycursor = mydb.cursor()

# Function to handle the calculation and database saving
def submit_data():
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()
    user_email = user_email_entry.get()
    user_password = user_password_entry.get()
    user_gender = user_gender_label.get()
    

# To insert your Data to your database.
    sql = "INSERT INTO user_registration (First_Name, Last_Name, User_Email, User_Password, User_Gender) VALUES (%s, %s, %s, %s, %s)"
    val = (first_name, last_name, user_email, user_password, user_gender)
    mycursor.execute(sql, val)
    mydb.commit()


root = tk.Tk()
root.title("User Register")
root.geometry('500x400')
root.configure(bg='#a36370')

label = tk.Label(root, text="USER REGISTRATION", font=("New York",20,"bold"), bg='#a36370', fg='#ffffff')
label.grid(row=0, column=1, padx=5, pady=5)

## User first name
first_name_label = tk.Label(root, text="First Name", font=("New York",15,"bold"), bg='#a36370', fg='#ffffff')
first_name_label.grid(row=1, column=0, padx=5, pady=5)
first_name_entry = tk.Entry(root, bd=3)
first_name_entry.grid(row=1, column=1, padx=5, pady=5)

# User last name
last_name_label = tk.Label(root, text="Last Name", font=("New York",15,"bold"), bg='#a36370', fg='#ffffff')
last_name_label.grid(row=2, column=0, padx=5, pady=5)
last_name_entry = tk.Entry(root, bd=3)
last_name_entry.grid(row=2, column=1, padx=5, pady=5)

# User email
user_email_label = tk.Label(root, text="Email", font=("New York",15,"bold"), bg='#a36370', fg='#ffffff')
user_email_label.grid(row=3, column=0, padx=5, pady=5)
user_email_entry = tk.Entry(root, bd=3)
user_email_entry.grid(row=3, column=1, padx=5, pady=5)

# User password
user_password_label = tk.Label(root, text="Password", font=("New York",15,"bold"), bg='#a36370', fg='#ffffff')
user_password_label.grid(row=4, column=0, padx=5, pady=5)
user_password_entry = tk.Entry(root, bd=3)
user_password_entry.grid(row=4, column=1, padx=5, pady=5)

# User gender
user_gender_label = tk.StringVar(root)
user_gender_label.set("Gender") 
trip_dropdown = tk.OptionMenu(root, user_gender_label, "Male", "Female")
trip_dropdown.grid(row=5, columnspan=2, padx=5, pady=5)


# Save Button
save_button = tk.Button(root, text="SUBMIT",font=("New York",15,"bold"), bg='#a36370', fg='#ffffff', command=submit_data)
save_button.grid(row=8, column=0, columnspan=2)

root.mainloop()
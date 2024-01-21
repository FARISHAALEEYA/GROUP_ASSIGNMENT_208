import tkinter as tk
import mysql.connector

# Connect to your MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="Book_Entry"
)
mycursor = mydb.cursor()

def enter_data():
    book_id = book_id_entry.get()
    book_title = book_title_entry.get()
    book_type = book_type_var.get()
    date_borrow = date_borrow_entry.get()

# Inserting data into a table
    sql = "INSERT INTO book_entry_form(book_id, book_title, book_type,date_borrow) VALUES (%s, %s, %s, %s)"
    val = (book_id, book_title, book_type,date_borrow)
    mycursor.execute(sql, val)
    mydb.commit()



# Your Main window, You need to have the title, geometry (MUST)
root = tk.Tk()
root.title("Book Entry")
root.geometry('500x550')
root.configure(bg="#C1B8A3")



# Page Title
label = tk.Label(root,text=" Book Entry Form", font=("Elephant",20), bg="#B6897A")
label.grid(padx=130, pady=10)

#Frame
frame = tk.Frame(root)
frame.grid(ipady=10, ipadx=10)


# Saving User Info
user_info_frame =tk.LabelFrame(frame, text="Book Information")
user_info_frame.grid(row= 0, column=0, padx=40, pady=20)

#Label
label = tk.Label(frame, text="ADD YOUR BOOK", font=("Times New Roman",11, "bold"),bg="#BFA493")
label.grid(row=0, column=0,pady=20)

# Create entry fields for the book data
book_id_label=tk.Label(frame, text="Book ID:", font=("Times New Roman",11, "bold"),bg="#BFA493")
book_id_label.grid(row=1, column=0,pady=10)
book_id_entry = tk.Entry(frame, width=30)
book_id_entry.grid(row=1, column=1, pady=20)

book_title_label=tk.Label(frame, text="Book Title:",font=("Times New Roman",11, "bold"),bg="#BFA493" )
book_title_label.grid(row=2, column=0)
book_title_entry = tk.Entry(frame, width=30)
book_title_entry.grid(row=2,column=1, pady=20 )

# Gender Dropdown
book_type_var = tk.StringVar(root)
book_type_var.set("Select Your Book Type")
book_type_dropdown = tk.OptionMenu(root, book_type_var, "Act", "Conference","Children Book", "Novel","Audio Book", "et.al")
book_type_dropdown.grid(pady=10)

# Date Borrow
date_borrow_label=tk.Label(frame, text="Date Borrow:",font=("Times New Roman",11, "bold"),bg="#BFA493")
date_borrow_label.grid(row=4, column=0)
date_borrow_entry = tk.Entry(frame, width=30)
date_borrow_entry.grid(row=4, column=1, pady=20)

# Submit Button
submit_button = tk.Button(root, text="Submit Form",font=("Amasis MT Pro Black",11, "bold"),bg="#A36370", command=enter_data)
submit_button.grid(row=7)



root.mainloop()


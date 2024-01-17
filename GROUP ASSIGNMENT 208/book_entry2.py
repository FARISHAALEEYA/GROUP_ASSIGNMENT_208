import tkinter as tk
import mysql.connector

# Connect to your MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="book_rent2"
)
# Create a cursor object to execute SQL queries
mycursor = mydb.cursor()

def enter_data():
    book_id = book_id_entry.get()
    book_title = book_title_entry.get()
    book_type = book_type_var.get()
    book_price = book_price_entry.get()
    date_borrow= date_borrow_entry.get()


 # Inserting data into a table
    sql = "INSERT INTO book_entry_form (book_id, book_title, book_type, book_price, date_borrow) VALUES (%s, %s, %s, %s, %s)"
    val = (book_id, book_title, book_type, book_price, date_borrow)
    mycursor.execute(sql,val)
    mydb.commit()

#Delete data
def delete_data():

    mydb = mysql.connector.connect(
            host="localhost",
            user="root", 
            password="",  
            database="book_rent2" 
        )

    mycursor = mydb.cursor()

    # Get the total count of rows in the database
    mycursor.execute("SELECT COUNT(*) FROM book_entry_form")
    count = mycursor.fetchone()[0]

    if count > 0:
        # Delete the last row in the database
        sql = "DELETE FROM book_entry_form ORDER BY name DESC LIMIT 1"
        mycursor.execute(sql)
        mydb.commit()
        print("Last record deleted.")
    else:
        print("No records to delete.")

    mycursor.close()
    mydb.close()

        
 # Your Main window, You need to have the title, geometry (MUST)
root = tk.Tk()
root.title("Book Rent")
root.geometry('500x550')
root.configure(bg="#C1B8A3")

# Page Title
label = tk.Label(root,text=" Book Entry Form", font=("Elephant",20), bg="#B6897A")
label.grid(padx=130, pady=10)


frame = tk.Frame(root)
frame.grid(ipady=10, ipadx=10)


# Saving User Info
user_info_frame =tk.LabelFrame(frame, text="Book Information")
user_info_frame.grid(row= 0, column=0, padx=40, pady=20)

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
               # Default value before your selection
book_type_dropdown = tk.OptionMenu(root, book_type_var, "Journal", "Encyclopedia","Special Book")
book_type_dropdown.grid(pady=10)

book_price_label=tk.Label(frame, text="Book Price:", font=("Times New Roman",11, "bold"),bg="#BFA493")
book_price_label.grid(row=3, column=0)
book_price_entry = tk.Entry(frame, width=30)
book_price_entry.grid(row=3, column=1, pady=20)

date_borrow_label=tk.Label(frame, text="Date Borrow:",font=("Times New Roman",11, "bold"),bg="#BFA493")
date_borrow_label.grid(row=4, column=0)
date_borrow_entry = tk.Entry(frame, width=30)
date_borrow_entry.grid(row=4, column=1, pady=20)

# Update Button
update_button = tk.Button(root, text="Update",font=("Amasis MT Pro Black",11, "bold"),bg="#A36370", command=enter_data)
update_button.grid(row=5,column=0, padx=10)

# Delete Button
delete_button = tk.Button(root, text="Delete",font=("Amasis MT Pro Black",11, "bold"),bg="#A36370", command= delete_data)
delete_button.grid(row=6,column=0,padx=5, pady=10)

# Submit Button
submit_button = tk.Button(root, text="Submit Form",font=("Amasis MT Pro Black",11, "bold"),bg="#A36370", command=enter_data)
submit_button.grid(row=7)

# Update data
def edit_data():
    book_id = book_id_entry.get()
    book_title = book_title_entry.get()
    book_type = book_type_var.get()
    book_price = book_price_entry.get()
    date_borrow= date_borrow_entry.get()

    mydb = mysql.connector.connect(
            host="localhost",
            user="root", 
            password="",  
            database="book_rent" 
        )
    mycursor = mydb.cursor()

    # Get the total count of rows in the database
    mycursor.execute("SELECT COUNT(*) FROM book_entry_form")
    count = mycursor.fetchone()[0]

    if count > 0:
            # Update the last row in the database (book_id, book_title, book_type, book_price, date_borrow)
            sql = "UPDATE book_entry_form SET book_id= %s, book_title = %s, book_type = %s, book_price = %s, date_borrow =%s ORDER BY name DESC LIMIT 1"
            val = (book_id, book_title, book_type, book_price, date_borrow)
            mycursor.execute(sql, val)
            mydb.commit()
            print("Record updated!!!")
    else:
            print("No records update!!!")



root.mainloop()















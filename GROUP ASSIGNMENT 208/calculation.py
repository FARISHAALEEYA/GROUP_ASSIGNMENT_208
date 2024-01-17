import tkinter as tk
import mysql.connector

# Connect to your MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="calculation_book"
)

# Create a cursor object to execute SQL queries
mycursor = mydb.cursor()

# Function to handle the calculation and database saving
def collect_data():
    book_type = book_type_var.get()
    packs = int(packs_entry.get())
    days_late = int(days_late_entry.get())  # Get the number of days late from the entry

    # The price below is defined for the values from your selections
    prices = {
        "Journal": 20,
        "Encyclopedia": 45,
        "Special Book": 10,
    }

    # Calculate the total price. This will be derived from your selection (Book category, Packs).
    total_price = (prices[book_type] * packs)

    # To insert your Data into your database, for this example, you have 3 attributes. (2 Attributes from your selection (Package, Pack) and another attribute derived from your attributes (price))
    sql = "INSERT INTO user (Book_Type, Book_Pack, Days_Late, Book_Price) VALUES (%s, %s, %s, %s)"
    val = (book_type, packs, days_late, total_price)
    mycursor.execute(sql, val)
    mydb.commit()

    # Calculate fine for late return
    fine_rate = 2  # RM2 per day
    late_return_fine = fine_rate * days_late

    # To Print back the output. It will happen in the function collect_data(). The f before the string indicates an f-string in Python.
    output_label.config(text=f"Book Type: {book_type}\nPacks: {packs}\nTotal Price: RM{total_price}\nLate Return Fine: RM{late_return_fine}")

# Your Main window, You need to have the title, geometry (MUST)
root = tk.Tk()
root.title("Book Price Calculator")
root.geometry('800x800')
root.configure(bg='#c1b8a3')

# Page Title
title_label = tk.Label(root, text='Calculate Your Book Price', font=("Bodoni MT Black", 18, "bold"), bg='#b6897a')
title_label.pack(pady=20)

# Frame for the content
frame = tk.Frame(root, bg='#E0D8B0')
frame.pack()

# Prices List using a textbox
prices_text = tk.Text(frame, height=10, width=50, font=("Times New Roman", 12), bg='#FCFFE7')
prices_text.pack(pady=10)

# The defined list using the pricebox
prices_text.insert(tk.END, "Book Types & Prices:\n\n")
prices_text.insert(tk.END, "Journal:\nPrice: RM20\n\n")
prices_text.insert(tk.END, "Encyclopedia:\nPrice: RM45\n\n")
prices_text.insert(tk.END, "Special Book:\nPrice: RM10\n\n")
prices_text.configure(state='disabled')

# Book category Dropdown (Label)
book_type_label = tk.Label(frame, text="Choose Your Book Types", font=("Bodoni MT Black", 12), bg='#FCFFE7')
book_type_label.pack()

# Book category Dropdown
book_type_var = tk.StringVar(root)
book_type_var.set("Select Your Book Types")  # Default value before your selection
book_type_dropdown = tk.OptionMenu(frame, book_type_var, "Journal", "Encyclopedia", "Special Book")
book_type_dropdown.config(font=("Times New Roman", 12,))
book_type_dropdown.pack()

# Packs Entry. Label and user can insert data through entry
packs_label = tk.Label(frame, text="Packs:", font=("Times New Roman", 12, "bold"), bg='#b6897a')
packs_label.pack()
packs_entry = tk.Entry(frame, font=("Times New Roman", 12), bg='#FFEBC1')
packs_entry.pack()

# Days Late Entry. Label and user can insert data through entry
days_late_label = tk.Label(frame, text="Days Late:", font=("Times New Roman", 12, "bold"), bg='#b6897a')
days_late_label.pack()
days_late_entry = tk.Entry(frame, font=("Times New Roman", 12), bg='#FFEBC1')
days_late_entry.pack()

# Save Button
save_button = tk.Button(root, text="Calculate Book Price", command=collect_data, font=("Bodoni MT Black", 12, "bold"), bg='#E8C07D', fg='black')
save_button.pack(pady=20)

# Output Label & result
output_label = tk.Label(root, text="Total", font=("Bodoni MT Black", 12, "bold"), bg='#a36370')
output_label.pack()

root.mainloop()

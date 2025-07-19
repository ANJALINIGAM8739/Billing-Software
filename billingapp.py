from pymongo import MongoClient# For connecting to MongoDB
import tkinter as tk# For creating the GUI
from tkinter import messagebox# For showing message boxes


# MongoDB Connection (default localhost)
client = MongoClient("mongodb://localhost:27017/")
db = client["billing_db"]
collection = db["invoices"]

# Save Invoice to MongoDB
def save_invoice():
    # Getting user input from GUI entry fields
    customer = entry_customer.get()
    item = entry_item.get()
    price = entry_price.get()
    qty = entry_qty.get()
# If any field is empty, show an error message
    if not (customer and item and price and qty):
        messagebox.showerror("Error", "Saare fields bharo bhai!")
        return
# Validate price and quantity inputs
    try:
        price = float(price)
        qty = int(qty)
    except:
        messagebox.showerror("Error", "Price number me daalo, qty integer me.")
        return
# Calculate total amount
    total = price * qty
 # Create invoice data as a dictionary
    invoice = {
        "customer": customer,
        "item": item,
        "price": price,
        "quantity": qty,
        "total": total
    }
 # Insert the invoice into MongoDB collection
    collection.insert_one(invoice)
    # Show success message
    messagebox.showinfo("Success", "Invoice saved ho gaya!")
    clear_fields()
# Function to clear input fields after saving
def clear_fields():
    entry_customer.delete(0, tk.END)
    entry_item.delete(0, tk.END)
    entry_price.delete(0, tk.END)
    entry_qty.delete(0, tk.END)

# GUI Window
app = tk.Tk()
app.title("Billing Software")
app.geometry("300x300")

tk.Label(app, text="Customer Name").pack()
entry_customer = tk.Entry(app)
entry_customer.pack()

tk.Label(app, text="Item").pack()
entry_item = tk.Entry(app)
entry_item.pack()

tk.Label(app, text="Price").pack()
entry_price = tk.Entry(app)
entry_price.pack()
 
tk.Label(app, text="Quantity").pack()
entry_qty = tk.Entry(app)
entry_qty.pack()
# Button to trigger the save_invoice function

tk.Button(app, text="Save Invoice", command=save_invoice).pack(pady=10)
# Run the GUI application loop
app.mainloop()


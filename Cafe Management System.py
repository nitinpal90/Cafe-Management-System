import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class CafeManagementSystemGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Cafe Management System")
        self.root.geometry("500x600")
        self.root.config(bg="#f0e6d2")  # Light cream background color
        
        # Cafe menu
        self.menu = {
            "Coffee": 50,
            "Tea": 30,
            "Sandwich": 100,
            "Burger": 150,
            "Pizza": 200
        }
        self.orders = {}
        
        # Header (Cafe brown)
        self.header_frame = tk.Frame(root, bg="#4b3f29", pady=10)
        self.header_frame.pack(fill="x")
        tk.Label(
            self.header_frame, 
            text="Cafe Management System", 
            font=("Helvetica", 18, "bold"), 
            fg="#ffffff", 
            bg="#4b3f29"
        ).pack()
        
        # Menu Display (Soft beige)
        self.menu_frame = tk.Frame(root, bg="#f0e6d2", pady=10)
        self.menu_frame.pack(pady=10)
        tk.Label(
            self.menu_frame, 
            text="Menu", 
            font=("Helvetica", 16, "bold"), 
            fg="#3e2a47",  # Dark purple (coffee-like)
            bg="#f0e6d2"
        ).grid(row=0, column=0, columnspan=3, pady=5)
        
        for idx, (item, price) in enumerate(self.menu.items(), start=1):
            tk.Label(
                self.menu_frame, 
                text=f"{item} - ₹{price}", 
                font=("Helvetica", 12), 
                bg="#f0e6d2",
                fg="#4b3f29"  # Dark brown text
            ).grid(row=idx, column=0, sticky="w", padx=20)
            qty_var = tk.IntVar()
            ttk.Entry(self.menu_frame, textvariable=qty_var, width=5).grid(row=idx, column=1, padx=10)
            self.orders[item] = qty_var

        # Buttons (Earthy orange for a cafe feel)
        self.button_frame = tk.Frame(root, bg="#f0e6d2")
        self.button_frame.pack(pady=20)
        self.generate_bill_button = ttk.Button(self.button_frame, text="Generate Bill", command=self.generate_bill, style="Cafe.TButton")
        self.generate_bill_button.grid(row=0, column=0, padx=10)
        
        self.clear_button = ttk.Button(self.button_frame, text="Clear", command=self.clear_orders, style="Cafe.TButton")
        self.clear_button.grid(row=0, column=1, padx=10)

        # Bill output (Light brown for a warm, readable text area)
        tk.Label(
            root, 
            text="Bill Summary", 
            font=("Helvetica", 14, "bold"), 
            bg="#f0e6d2", 
            fg="#3e2a47"
        ).pack(pady=5)
        self.bill_text = tk.Text(root, width=55, height=12, state="disabled", font=("Courier", 10), bg="#f5e1a4", fg="#4b3f29")
        self.bill_text.pack(pady=10)

    def generate_bill(self):
        total = 0
        bill_details = "----- Bill -----\n\n"
        for item, qty_var in self.orders.items():
            quantity = qty_var.get()
            if quantity > 0:
                price = self.menu[item] * quantity
                total += price
                bill_details += f"{item} x {quantity} = ₹{price}\n"
        
        if total == 0:
            messagebox.showerror("Error", "No items ordered!")
        else:
            bill_details += f"\nTotal Amount: ₹{total}\n\nThank you for visiting our cafe!"
            self.bill_text.config(state="normal")
            self.bill_text.delete("1.0", "end")
            self.bill_text.insert("1.0", bill_details)
            self.bill_text.config(state="disabled")
    
    def clear_orders(self):
        for qty_var in self.orders.values():
            qty_var.set(0)
        self.bill_text.config(state="normal")
        self.bill_text.delete("1.0", "end")
        self.bill_text.config(state="disabled")
        messagebox.showinfo("Info", "Orders cleared!")

if __name__ == "__main__":
    root = tk.Tk()
    
    # Style for buttons (earthy brown/orange style for cafe feel)
    style = ttk.Style()
    style.theme_use("clam")
    
    # Configure the button style
    style.configure("Cafe.TButton", 
                    background="#d47b3a", 
                    foreground="#ffffff", 
                    font=("Helvetica", 12, "bold"),
                    relief="flat",
                    padding=10)
    
    # Hover effect for buttons: Change color when hovered
    style.map("Cafe.TButton", 
              background=[('active', '#bc6723'), 
                          ('pressed', '#9c5024')],
              foreground=[('active', '#ffffff')])

    app = CafeManagementSystemGUI(root)
    root.mainloop()

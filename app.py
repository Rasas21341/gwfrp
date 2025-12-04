# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

class ModernApp:
    VERSION = "1.0.0"
    
    def __init__(self, root):
        self.root = root
        self.root.title(f"My Awesome App v{self.VERSION}")
        self.root.geometry("600x500")
        self.root.resizable(False, False)
        
        # Configure style
        style = ttk.Style()
        style.theme_use('clam')
        
        # Main container
        main_frame = ttk.Frame(root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Title
        title_label = tk.Label(
            main_frame, 
            text="Welcome to My App!",
            font=("Segoe UI", 20, "bold"),
            fg="#2c3e50"
        )
        title_label.pack(pady=(0, 20))
        
        # Info frame
        info_frame = ttk.LabelFrame(main_frame, text="App Features", padding="15")
        info_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        # Feature list
        features = [
            "Modern graphical interface",
            "Easy to use and navigate",
            "Lightweight and fast",
            "Built-in calculator",
            "Can be packaged as .exe"
        ]
        
        for feature in features:
            label = tk.Label(
                info_frame, 
                text="  " + feature, 
                font=("Segoe UI", 11),
                anchor="w"
            )
            label.pack(fill=tk.X, pady=5)
        
        # Input section
        input_frame = ttk.Frame(main_frame)
        input_frame.pack(fill=tk.X, pady=15)
        
        ttk.Label(input_frame, text="Enter your name:", font=("Segoe UI", 10)).pack(side=tk.LEFT, padx=(0, 10))
        self.name_entry = ttk.Entry(input_frame, width=30, font=("Segoe UI", 10))
        self.name_entry.pack(side=tk.LEFT)
        
        # Buttons frame
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(pady=10)
        
        # Action button
        greet_btn = tk.Button(
            button_frame,
            text="Greet Me!",
            command=self.greet_user,
            bg="#3498db",
            fg="white",
            font=("Segoe UI", 10, "bold"),
            padx=20,
            pady=10,
            cursor="hand2",
            relief=tk.FLAT
        )
        greet_btn.pack(side=tk.LEFT, padx=5)
        
        # Calculator button
        calc_btn = tk.Button(
            button_frame,
            text="Calculator",
            command=self.open_calculator,
            bg="#e67e22",
            fg="white",
            font=("Segoe UI", 10, "bold"),
            padx=20,
            pady=10,
            cursor="hand2",
            relief=tk.FLAT
        )
        calc_btn.pack(side=tk.LEFT, padx=5)
        
        # Info button
        info_btn = tk.Button(
            button_frame,
            text="About",
            command=self.show_about,
            bg="#95a5a6",
            fg="white",
            font=("Segoe UI", 10, "bold"),
            padx=20,
            pady=10,
            cursor="hand2",
            relief=tk.FLAT
        )
        info_btn.pack(side=tk.LEFT, padx=5)
        
        # Status bar
        self.status_label = tk.Label(
            root,
            text=f"Ready | {datetime.now().strftime('%Y-%m-%d %H:%M')}",
            bd=1,
            relief=tk.SUNKEN,
            anchor=tk.W,
            font=("Segoe UI", 9)
        )
        self.status_label.pack(side=tk.BOTTOM, fill=tk.X)
    
    def greet_user(self):
        name = self.name_entry.get().strip()
        if name:
            messagebox.showinfo(
                "Greeting", 
                f"Hello, {name}!\n\nWelcome to this awesome application!"
            )
            self.status_label.config(text=f"Greeted {name} at {datetime.now().strftime('%H:%M:%S')}")
        else:
            messagebox.showwarning("Input Required", "Please enter your name first!")
    
    def open_calculator(self):
        calc_window = tk.Toplevel(self.root)
        calc_window.title("Calculator")
        calc_window.geometry("300x400")
        calc_window.resizable(False, False)
        
        # Entry for calculator
        calc_entry = tk.Entry(calc_window, font=("Segoe UI", 18), justify="right", bd=5)
        calc_entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="ew")
        
        # Button click handler
        def button_click(value):
            current = calc_entry.get()
            calc_entry.delete(0, tk.END)
            calc_entry.insert(0, current + str(value))
        
        def calculate():
            try:
                result = eval(calc_entry.get())
                calc_entry.delete(0, tk.END)
                calc_entry.insert(0, str(result))
            except:
                calc_entry.delete(0, tk.END)
                calc_entry.insert(0, "Error")
        
        def clear():
            calc_entry.delete(0, tk.END)
        
        # Calculator buttons
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('+', 4, 2)
        ]
        
        for (text, row, col) in buttons:
            btn = tk.Button(
                calc_window, 
                text=text, 
                font=("Segoe UI", 14), 
                width=5, 
                height=2,
                command=lambda t=text: button_click(t)
            )
            btn.grid(row=row, column=col, padx=2, pady=2)
        
        # Special buttons
        equals_btn = tk.Button(calc_window, text="=", font=("Segoe UI", 14), width=5, height=2, bg="#27ae60", fg="white", command=calculate)
        equals_btn.grid(row=4, column=3, padx=2, pady=2)
        
        clear_btn = tk.Button(calc_window, text="C", font=("Segoe UI", 14), width=11, height=2, bg="#e74c3c", fg="white", command=clear)
        clear_btn.grid(row=5, column=0, columnspan=2, padx=2, pady=2)
        
        self.status_label.config(text="Calculator opened")
    
    def show_about(self):
        about_text = f"""My Awesome App v{self.VERSION}

Created with Python & Tkinter

A simple, modern desktop application
that can be packaged as a standalone
executable for Windows.

Features:
 User greeting
 Built-in calculator
 Clean interface

2025 - Built with love"""
        
        messagebox.showinfo("About", about_text)

def main():
    root = tk.Tk()
    app = ModernApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

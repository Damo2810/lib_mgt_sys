import tkinter as tk
from tkinter import ttk
import mysql.connector

class Viewbook(tk.Frame):

    def __init__(self, parent,controller):
        tk.Frame.__init__(self, parent)
        # frame_input = tk.Frame(self,highlightbackground="grey", highlightthickness=2)
        # frame_input.pack(pady=10)
        frame_table = tk.Frame(self,highlightbackground="grey", highlightthickness=2)
        frame_table.pack()
        self.display_table_data(frame_table)

        # combo1 = ttk.Combobox(frame_input, values=["Option 1", "Option 2", "Option 3"],width=30)
        # combo1.set("Book no")  # Set the initial text for the entry
        # combo1.pack(side="left",padx=5,pady=10)

        # combo2 = ttk.Combobox(frame_input, values=["Option 1", "Option 2", "Option 3"],width=30)
        # combo2.set("Book name")  # Set the initial text for the entry
        # combo2.pack(side="left",padx=5,pady=10)

        # combo3 = ttk.Combobox(frame_input, values=["Option 1", "Option 2", "Option 3"],width=30)
        # combo3.set("Book price")  # Set the initial text for the entry
        # combo3.pack(side="left",padx=5,pady=10)

        # combo4 = ttk.Combobox(frame_input, values=["Option 1", "Option 2", "Option 3"],width=30)
        # combo4.set("Book category")  # Set the initial text for the entry
        # combo4.pack(side="left",padx=5,pady=10)

        # combo5 = ttk.Combobox(frame_input, values=["Option 1", "Option 2", "Option 3"],width=30)
        # combo5.set("Book status")  # Set the initial text for the entry
        # combo5.pack(side="left",padx=5,pady=10)
        
        

    def fetch_data_with_columns(self):
            conn = mysql.connector.connect(host="127.0.0.1",user="root",password="damo@mysql33",database="LIBRARY_MANAGEMENT_SYSTEM")
            cursor = conn.cursor()

            # Replace 'your_table' with the actual table name
            cursor.execute("SELECT * FROM BOOKS")
            data = cursor.fetchall()
            columns = [description[0] for description in cursor.description]

            conn.close()
            return columns, data

    def display_table_data(self,frame_table):
        columns, data = self.fetch_data_with_columns()

            # Display column names
        for j, column_name in enumerate(columns):
                label = tk.Label(frame_table, text=column_name, font=("bold", 12),width=30,highlightbackground="grey", highlightthickness=2)
                label.grid(row=0, column=j)

            # Display table data
        for i, row in enumerate(data):
                for j, value in enumerate(row):
                    label = tk.Label(frame_table, text=value,font=('calibre',12),width=30,highlightbackground="grey", highlightthickness=2)
                    label.grid(row=i + 1, column=j)

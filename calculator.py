import customtkinter as ctk
from tkinter import *
from tkinter import messagebox


class App(ctk.CTk):
     my_font1 = ('Arial', 40)
     my_font2 = ('Arial', 15)
     def __init__(self, title, size, bg_color, btn_color):
          super().__init__()
          # Configuration
          self.title(title)
          self.geometry(f"{size[0]}x{size[1]}")
          self.minsize(width=size[0], height=size[1])
          self.config(bg=bg_color)
          
          # Create Widgets
          self.create_entry(size, bg_color)
          self.create_button(btn_color, bg_color, size)

     # Command functions
     def button_click(self, btn):
          current_entry = entry.get()
          entry.delete(0, END)
          if current_entry == "0":
               entry.insert(0, btn)
          else:
               entry.insert(0, current_entry + btn)


     def result(self):
          try:
               equation = entry.get()
               equation = equation.replace('x', '*')
               result = eval(equation)
               entry.delete(0, END)
               entry.insert(0, result)
          except ZeroDivisionError:
               messagebox.showerror("Error", "Can not divide by 0")
          except:
               messagebox.showerror("Error", "Invalid entry")


     def clear(self):
          entry.delete(0, END)
          entry.insert(0, "0")


     def delete(self):
          current_entry = entry.get()
          entry.delete(len(current_entry)-1, END)
          if entry.get() == "":
               entry.insert(0, "0")
               

     def create_entry(self, size, bg_color):
          global entry
          entry = ctk.CTkEntry(self, text_color="white", fg_color="#323334",bg_color=bg_color, font=self.my_font1, width=size[0], height=90, corner_radius=10)
          entry.grid(row=0, column=0, columnspan=4, sticky="nsew")
          entry.insert(0, "0")


     def create_button(self, btn_color, bg_color, size):
          # Layout configuration
          for row in range(5):
               self.grid_rowconfigure(row, weight=1)
          for column in range(4):
               self.grid_columnconfigure(column, weight=1)

          # Create the buttons 
          btn_width = size[0]/4.3
          btn_height = (size[1]-90)/5.5
          hover_color =  "#333844"
          button_1 = ctk.CTkButton(self, width=btn_width, height=btn_height, corner_radius=7, bg_color=bg_color, hover_color=hover_color, font=self.my_font2, text="1", fg_color=btn_color, command=lambda: self.button_click("1"))
          button_2 = ctk.CTkButton(self, width=btn_width, height=btn_height, corner_radius=7, bg_color=bg_color, hover_color=hover_color, font=self.my_font2, text="2",  fg_color=btn_color, command=lambda: self.button_click("2"))
          button_3 = ctk.CTkButton(self, width=btn_width, height=btn_height, corner_radius=7, bg_color=bg_color, hover_color=hover_color, font=self.my_font2, text="3",  fg_color=btn_color, command=lambda: self.button_click("3"))
          button_4 = ctk.CTkButton(self, width=btn_width, height=btn_height, corner_radius=7, bg_color=bg_color, hover_color=hover_color, font=self.my_font2, text="4",  fg_color=btn_color, command=lambda: self.button_click("4"))
          button_5 = ctk.CTkButton(self, width=btn_width, height=btn_height, corner_radius=7, bg_color=bg_color, hover_color=hover_color, font=self.my_font2, text="5",  fg_color=btn_color, command=lambda: self.button_click("5"))
          button_6 = ctk.CTkButton(self, width=btn_width, height=btn_height, corner_radius=7, bg_color=bg_color, hover_color=hover_color, font=self.my_font2, text="6",  fg_color=btn_color, command=lambda: self.button_click("6"))
          button_7 = ctk.CTkButton(self, width=btn_width, height=btn_height, corner_radius=7, bg_color=bg_color, hover_color=hover_color, font=self.my_font2, text="7",  fg_color=btn_color, command=lambda: self.button_click("7"))
          button_8 = ctk.CTkButton(self, width=btn_width, height=btn_height, corner_radius=7, bg_color=bg_color, hover_color=hover_color, font=self.my_font2, text="8",  fg_color=btn_color, command=lambda: self.button_click("8"))
          button_9 = ctk.CTkButton(self, width=btn_width, height=btn_height, corner_radius=7, bg_color=bg_color, hover_color=hover_color, font=self.my_font2, text="9",  fg_color=btn_color, command=lambda: self.button_click("9"))
          button_0 = ctk.CTkButton(self, width=btn_width*2.1, height=btn_height, corner_radius=7, bg_color=bg_color, hover_color=hover_color, font=self.my_font2, text="0",  fg_color=btn_color, command=lambda: self.button_click("0"))
          button_add = ctk.CTkButton(self, width=btn_width, height=btn_height*2.1, corner_radius=7, bg_color=bg_color, hover_color=hover_color, fg_color=btn_color, font=self.my_font2, text="+", command=lambda: self.button_click("+"))
          button_sub = ctk.CTkButton(self, width=btn_width, height=btn_height, corner_radius=7, bg_color=bg_color, hover_color=hover_color, font=self.my_font2, text="-",  fg_color=btn_color, command=lambda: self.button_click("-"))
          button_multi = ctk.CTkButton(self, width=btn_width, height=btn_height, corner_radius=7, bg_color=bg_color, hover_color=hover_color, font=self.my_font2, text="x",  fg_color=btn_color, command=lambda: self.button_click("x"))
          button_div = ctk.CTkButton(self, width=btn_width, height=btn_height, corner_radius=7, bg_color=bg_color, hover_color=hover_color, font=self.my_font2, text="/",  fg_color=btn_color, command=lambda: self.button_click("/"))
          button_equal = ctk.CTkButton(self, width=btn_width, height=btn_height*2.1, corner_radius=7, bg_color=bg_color, fg_color="#4071f2", font=self.my_font2, text="=", command=self.result)
          button_delete = ctk.CTkButton(self, width=btn_width, height=btn_height, corner_radius=7, bg_color=bg_color, hover_color=hover_color, font=self.my_font2, text="←",  fg_color=btn_color, command=self.delete)
          button_clear = ctk.CTkButton(self, width=btn_width, height=btn_height, corner_radius=7, bg_color=bg_color, hover_color=hover_color, font=self.my_font2, text="Clear",  fg_color=btn_color, command=self.clear)

          # Placing
          button_delete.grid(row=1, column=0, sticky="nsew", padx= 5, pady=5)
          button_div.grid(row=1, column=1, sticky="nsew", padx= 5, pady=5)
          button_multi.grid(row=1, column=2, sticky="nsew", padx= 5, pady=5)
          button_sub.grid(row=1, column=3, sticky="nsew", padx= 5, pady=5)


          button_7.grid(row=2, column=0, sticky="nsew", padx= 5, pady=5)
          button_8.grid(row=2, column=1, sticky="nsew", padx= 5, pady=5)
          button_9.grid(row=2, column=2, sticky="nsew", padx= 5, pady=5)
          button_add.grid(row=2, column=3, rowspan=2, sticky="nsew", padx= 5, pady=5)

          button_4.grid(row=3, column=0, sticky="nsew", padx= 5, pady=5)
          button_5.grid(row=3, column=1, sticky="nsew", padx= 5, pady=5)
          button_6.grid(row=3, column=2, sticky="nsew", padx= 5, pady=5)

          button_1.grid(row=4, column=0, sticky="nsew", padx= 5, pady=5)
          button_2.grid(row=4, column=1, sticky="nsew", padx= 5, pady=5)
          button_3.grid(row=4, column=2, sticky="nsew", padx= 5, pady=5)
          button_equal.grid(row=4, column=3, rowspan=2, ipady = 10, sticky="nsew", padx= 5, pady=5)

          button_0.grid(row=5, column=0, columnspan=2, sticky="nsew", padx= 5, pady=5)
          button_clear.grid(row=5, column=2, sticky="nsew", padx= 5, pady=5)
          

if __name__ == "__main__":
    app = App(title="Calculator", size=(450, 600),bg_color="#5f4b5c", btn_color="#201e1f")
    app.mainloop()
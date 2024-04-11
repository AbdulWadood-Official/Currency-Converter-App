# from currency_converter import CurrencyConverter

# import tkinter as tk

# a = CurrencyConverter()
# window = tk.Tk()
# window.geometry("500x360")

# def clicked():
#     amount = int(e1.get())
#     cur1 = e2.get()
#     cur2 = e3.get()
#     data = a.convert(amount,cur1,cur2)
#     l5 = tk.Label(window, text =data,font= "Times 25 bold").place(x= 200, y = 290)

# l1 = tk.Label(window,text="Currency Converter",font= "Times 25 bold").place(x = 100, y = 30)
# l2 = tk.Label(window,text="Enter amount : ", font= "Times 18 bold").place(x = 50, y = 80)
# e1 = tk.Entry(window)

# l3 = tk.Label(window,text="Enter currency : ", font= "Times 18 bold").place(x = 50, y = 130)
# e2 = tk.Entry(window)

# l4 = tk.Label(window,text="Enter req currency : ", font= "Times 18 bold").place(x = 50, y = 180)
# e3 = tk.Entry(window)

# button1 = tk.Button(window, text="click", command=clicked).place(x = 250, y = 240)
# e1.place(x = 300, y = 90)
# e2.place(x = 300, y = 140)
# e3.place(x = 300, y = 190)

# window.mainloop()

# a = CurrencyConverter()
# print(a.convert(10,"USD","INR"))






# **************************** Testing ************************************:

from currency_converter import CurrencyConverter
import tkinter as tk

# Initialize CurrencyConverter object
converter = CurrencyConverter()

# Custom conversion rate for PKR (Example: 1 USD = 160 PKR)
PKR_RATE = 281

# Create Tkinter window
window = tk.Tk()
window.geometry("500x360")

def clicked():
    # Retrieve user input
    amount = float(e1.get())
    cur1 = e2.get()
    cur2 = e3.get()

    # Perform currency conversion
    if cur1 == "PKR":
        converted_amount = amount / PKR_RATE
    elif cur2 == "PKR":
        converted_amount = amount * PKR_RATE
    else:
        converted_amount = converter.convert(amount, cur1, cur2)

    # Display converted amount
    l5.config(text=converted_amount)

# Create Tkinter widgets
l1 = tk.Label(window, text="Currency Converter", font="Times 25 bold")
l1.place(x=100, y=30)

l2 = tk.Label(window, text="Enter amount : ", font="Times 18 bold")
l2.place(x=50, y=80)
e1 = tk.Entry(window)

l3 = tk.Label(window, text="Enter currency : ", font="Times 18 bold")
l3.place(x=50, y=130)
e2 = tk.Entry(window)

l4 = tk.Label(window, text="Enter req currency : ", font="Times 18 bold")
l4.place(x=50, y=180)
e3 = tk.Entry(window)

button1 = tk.Button(window, text="click", command=clicked)
button1.place(x=250, y=240)

l5 = tk.Label(window, text="", font="Times 25 bold")
l5.place(x=200, y=290)

# Place Tkinter widgets
e1.place(x=300, y=90)
e2.place(x=300, y=140)
e3.place(x=300, y=190)

# Run Tkinter main loop
window.mainloop()

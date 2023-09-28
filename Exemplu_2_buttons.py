# Create a new window
import tkinter as tk



def open_window1():
    new_window = tk.Toplevel(root)
    new_window.title("New Window")
    new_window.geometry("400x300")

    # Add widgets to the new window
    label = tk.Label(new_window, text="New Window")
    label.pack()

def open_window2():
    new_window = tk.Toplevel(root)
    new_window.title("New Window")
    new_window.geometry("400x300")

    # Add widgets to the new window
    label = tk.Label(new_window, text="New Window")
    label.pack()


# Create the root window
root = tk.Tk()
root.title("Main Window")
root.geometry("800x600")

# buttons
button1 = tk.Button(root, text="Button Onw", command=open_window1)
button1.pack()

button2 = tk.Button(root, text="Button Two", command=open_window2)
button2.pack()

# main loop
root.mainloop()

button4 = tk.Button(root, text="Button 4")
button4.pack()

# main loop
root.mainloop()
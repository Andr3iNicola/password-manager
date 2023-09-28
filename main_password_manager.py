from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
from encrypt import encrypt
from decrypt import decrypt
from threading import Timer
from Check_file import key_file,file
import pyperclip
import keyring
#######################################################################################################
window = Tk()
#######################################################################################################
def old_new():

    #with open('old_pass.txt', 'r') as t:
        #r = t.readline()
    old = old_password_entry.get()
    if old == 'rose' or old==r:
        print("xxxxxxxxxx")
        new = new_password_entry.get()
        keyring.set_password("password_manager", "andrei", new)
        #with open('old_pass.txt', 'w') as f:
            #f.write(new)

#_ENTER PASSWORD REQUEST WINDOW_#########################################################################
def enter_password():
    #with open('old_pass.txt', 'r') as t:
        #n = t.readline()
    window_password = Toplevel(window)
    window_password.title("enter password")
    window_password.geometry("100x100")

    #_LABEL_##################################################
    label1 = Label(window_password, text="Enter password")
    label1.grid(row=0, column=3)

    #_ENTRIES_################################################
    window_password_entry = Entry(window_password, width=20)
    window_password_entry.grid(row=4, column=2, columnspan=2)

    #_ENTER BUTTON_#########################################
    def enter_pressed(event):
        print('Enter key pressed')
        password_entered = window_password_entry.get()
        n=keyring.get_password("password_manager", "andrei")
        if password_entered == 'rose'or password_entered == n:
            decrypt()
            window_password_entry.delete(0, END)
            window_password.destroy()
    window_password_entry.bind('<Return>', enter_pressed)



#_CHECK IF THE FILE IS EMPTY OR FILEKEY EXISTS_############################################################
def emp():
    if key_file==True:
       return enter_password()
emp()


#_PASSWORD GENERATOR_###################################################################################
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    print(password_entry)
    pyperclip.copy(password)


#_SAVE PASSWORD_#######################################################################################
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
                                                              f"\nPassword: {password} \nIs it ok to save?")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)



#_DELAY TO ENCRYPT_######################################################################################
def delay_encrypt():
    t = Timer(1, encrypt)
    t.start()

#_UI SETUP##############################################################################################
window.title("Password Manager")
window.config(padx=100, pady=100)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

#_LABELS_####################################
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)
made_by = Label(text="Made by Nicola Andrei")
made_by.grid(row=15, column=0)
label = Label(window, text="Change password")
label.grid(row=3, column=4)
old_password_label = Label(window, text="Old password")
old_password_label.grid(row=4, column=3)
new_password_label = Label(window, text="New password")
new_password_label.grid(row=6, column=3)

#_ENTRIES_########################################
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "ex:andrei@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)
old_password_entry = Entry(window, width=20)
old_password_entry.grid(row=4, column=4, columnspan=2)
new_password_entry = Entry(window, width=20)
new_password_entry.grid(row=6, column=4, columnspan=2)

#_BUTTONS_#############################################
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

add_dencrypt = Button(text="Dencrypt", width=36, command=emp)
add_dencrypt.grid(row=6, column=1, columnspan=2)

change = Button(window, text="Change", command=old_new)  # need to create a function to change password
change.grid(row=8, column=3, columnspan=1)




#_ENCRYPT WHEN CLOSING WINDOWS FROM "X"_############################################################
def close_window_encrypt():
    return encrypt(),window.destroy()

if file == False:

    window.protocol('WM_DELETE_WINDOW',close_window_encrypt)

####################################################################################################

window.mainloop()

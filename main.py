from tkinter import *
from tkinter import messagebox
from random import choice,shuffle,randint
import pyperclip
#Password Generator Project
def generate_password():
  letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

  password_letter = [choice(letters) for char in range(randint(8, 10))]

  password_symbol=[choice(symbols) for char in range(randint(2, 4))]

  password_number=[choice(numbers) for char in range(randint(2, 4)
  )]
  password_list=password_letter+password_symbol+password_number

  shuffle(password_list)

  password = "".join(password_list)
  password_entry.insert(0,password)
  pyperclip.copy(password)

# save password
def return_from_entry():
    website=website_entry.get()
    email=email_entry.get()
    password_value=password_entry.get()
    if len(website)==0 or len(email)==0 or len(password_value)==0:
        messagebox.showwarning(title="OOPS",message="Please do not leave any field empty")
    else:
        is_ok=messagebox.askokcancel(title="Saving....",message=f"Do you want to add these?\nWebsite: {website}\nEmail: {email}\nPassword: {password_value}")

        if is_ok:
            with open("data.txt","a") as f:
                f.write(f"{website} | {email} | {password_value}\n")
            website_entry.delete(0,END)
            password_entry.delete(0,END)

#UI setup 
window=Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

# creating a canvas
canvas=Canvas(width=200,height=200)
logo=PhotoImage(file="./logo.png")
canvas.create_image(100,100,image=logo)
canvas.grid(row=0,column=1)

website_label=Label(text="Website:")
website_label.grid(row=1,column=0)
website_entry=Entry(width=35)
website_entry.focus()
website_entry.grid(row=1,column=1,columnspan=2,sticky="ew")

email_label=Label(text="Email/Username:")
email_label.grid(row=2,column=0)
email_entry=Entry(width=35)
email_entry.insert(0,"sabina@gmail.com")
email_entry.grid(row=2,column=1,columnspan=2,sticky="ew")

password_label=Label(text="Password:")
password_label.grid(row=3,column=0)
password_entry=Entry(width=23)
password_entry.grid(row=3,column=1,sticky="ew")

generate_button=Button(text="Generate Password",command=generate_password)
generate_button.grid(row=3,column=2,sticky="ew")

add_button=Button(text="Add",width=36,command=return_from_entry)
add_button.grid(row=4,column=1,columnspan=2,sticky="ew")



window.mainloop()
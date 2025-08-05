from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx= 20 , pady= 20)
canvas = Canvas(window , height= 200 , width=200 )
photo = PhotoImage(file = "logo.png")
canvas.create_image(100 ,100, image = photo )
canvas.grid( row =  0  , column = 0 , pady = 20, padx = 20  ,columnspan = 3)

# Website label and entry
website_label = Label(text = "website :" )
website_label.grid(row = 1 , column = 0  )
entry_website = Entry( width= 50)
entry_website.grid( row = 1 , column = 1 , columnspan = 2  )

# Emai and Username
user_label = Label(text = "Email/Username :")
user_label.grid(row = 2 , column = 0)
entry_user = Entry(width= 50)
entry_user.grid( row = 2 , column = 1 , columnspan = 2  )

# Password
password_label = Label(text = "Password  :")
password_label.grid(row = 3 , column = 0 )
entry_password = Entry(width= 31  )
entry_password.grid( row = 3 , column = 1  )
generate_password = Button(text = "Generate Password" ,width= 15  )
generate_password.grid(row = 3 , column = 2)

# Enter the data
button_add = Button( text= "Add" ,width= 47, highlightthickness= 0)
button_add.grid(row = 4 ,column =1 ,columnspan = 2 )
window.mainloop()

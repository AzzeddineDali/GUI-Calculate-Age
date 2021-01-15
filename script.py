""" This Scrpit For Training Python By Create A Calculate Age GUI  And Tkinter """


from tkinter import *
from tkinter import messagebox

# Create The Main App Windows
age_app = Tk()

# Change App Text
age_app.title("Calculate App")

# Set Dimensions
age_app.geometry("400x250")

# Write Age Label
the_text = Label(age_app, text="Please Write Your Age", height=2, font=("Arial", 20))
the_text.pack()  # Place The Text Into The Main Windows

# Age Variable
age = StringVar()

# Set Default Value for Age
age.set('00')

# Create The Input For Age
age_input = Entry(age_app, width=2, font=("Arial", 25), textvariable=age)
age_input.pack()  # Place The Input Into The Main Windows

# Create Function

def calc():

    # Get Age In Years
    the_age_value = age.get()

    # Get Time Units
    months = int(the_age_value) * 12
    weeks = int(the_age_value) * 53
    days = int(the_age_value) * 365

    line_one = f"Your Age In Months Is: {months}"
    line_two = f"Your Age In Weeks Is : {weeks}"
    line_three = f"Your Age In Days Is : {days}"
    
    all_lines = [line_one, line_two, line_three]

    messagebox.showinfo("Your Age In All Units Time", "\n".join(all_lines))

# Create The Calculate Button
btn = Button(age_app,
        text="Calculate Age", 
        width=20, 
        height=2, 
        bg="green", 
        fg="white", 
        borderwidth=0,
        command=calc )

btn.pack()    # Place The btn Into Main Windows

# Run App Infinitely
age_app.mainloop()



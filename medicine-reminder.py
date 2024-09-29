from datetime import datetime
import time
from plyer import notification
import os 
from tkinter import *
from PIL import Image, ImageTk

def clear_screen():
    os.system("cls")

class User:
    def __init__(self):
        self.medicines = []
        self.times = []

    def enter_medicine_info(self):
        dateformat = '%H:%M'
        mname = medicine_name_entry.get()
        
        # Check if the medicine name is valid
        if not mname.isalpha():
            clear_screen()
            outputtxt.config(state=NORMAL)
            outputtxt.delete(1.0, END)  # Clear the output box
            outputtxt.insert(END, "Please Enter A Valid Medicine Name!\n")
            outputtxt.config(state=DISABLED)
            return False  # Exit if the medicine name is invalid
        
        try:
            tname = medicine_times_entry.get() 
            # Convert the input string to a datetime object
            dateobj = datetime.strptime(tname, dateformat)
            self.medicines.append(mname)
            self.times.append(dateobj)
            return True  # Medicine added successfully
        except ValueError:
            clear_screen()
            outputtxt.config(state=NORMAL)
            outputtxt.delete(1.0, END)  # Clear the output box
            outputtxt.insert(END, "Please Enter A Valid Time Format (HH:MM)!\n")
            outputtxt.config(state=DISABLED)
            return False  # Exit if the time format is wrong

class Notification:
    def __init__(self, user):
        self.user = user

    def display_output(self):
        outputtxt.config(state=NORMAL)
        outputtxt.delete(1.0, END)  # Clear the output box
        #outputtxt.insert(END, "ADDED: ")
        for i, (medicine, medicine_time) in enumerate(zip(self.user.medicines, self.user.times), 1):
            outputtxt.insert(END, f"{i:<5} {medicine:<15} at {medicine_time.strftime('%I:%M %p'):>10}\n")
        outputtxt.config(state=DISABLED)

    def check_time(self):
        while True:
            current_time = datetime.now()
            for medicine, medicine_time in zip(self.user.medicines, self.user.times):
                if current_time.hour == medicine_time.hour and current_time.minute == medicine_time.minute:
                    self.notified(medicine, medicine_time)
                    break  # Break after notification to avoid modifying list during iteration
            time.sleep(60)  # Check every 60 seconds

    def notified(self, medicine, medicine_time):
        notification.notify(
            title = f"{medicine} Time! It's {medicine_time.strftime('%I:%M %p')}",
            message = "Time to take your medicine!",
            timeout = 10
        )

# Tkinter setup
myframe = Tk()

# User instance
user = User()

# Notification instance
noti = Notification(user)

# GUI functions
def submit_medicine_gui():
    if user.enter_medicine_info():
        noti.display_output()

def reset_entries():
    medicine_name_entry.delete(0, END)
    medicine_times_entry.delete(0, END)
    outputtxt.config(state=NORMAL)
    outputtxt.delete(1.0, END)
    outputtxt.config(state=DISABLED)

# Image for the background
img = Image.open("medicines.png")
background_image = ImageTk.PhotoImage(img)

# Create a label widget to hold the image
background_label = Label(myframe, image=background_image)
background_label.place(relwidth=1, relheight=1)

# GUI TITLE LABEL
label1 = Label(myframe, text="MEDICINE REMINDER", bg="#419ebe", fg="white", pady=10, padx=10)
label1.config(font=("Helvetica", 18, "bold"))
label1.pack(pady=20)

# GUI DESCRIPTION LABEL
label2 = Label(myframe, text="A simple app to help users remember to take their medications on time.", bg="#a3dde9", padx=10, pady=10)
label2.config(font=("Helvetica", 10))
label2.pack(pady=5)

# Create a frame to hold the input fields and buttons
input_frame = Frame(myframe, bg="#419ebe")
input_frame.pack(pady=20)

# GUI LABEL FOR INPUT
label3 = Label(input_frame, text="Please Enter Your Medicine Name:", bg="#a3dde9", pady=10, padx=10, fg="black")
label3.config(font=("Helvetica", 12))
label3.grid(row=0, column=0, padx=10, pady=5)

# GUI INPUT ENTRY FOR MEDICINE NAME
medicine_name_entry = Entry(input_frame, width=20, font=("Helvetica", 14), bd=2, relief="groove")
medicine_name_entry.grid(row=0, column=1, padx=10, pady=5)

# GUI LABEL FOR MEDICINE TIMES
label4 = Label(input_frame, text="Enter Times to Take Medicine (Hours: Minutes):", bg="#a3dde9", pady=10, padx=10, fg="black")
label4.config(font=("Helvetica", 12))
label4.grid(row=1, column=0, padx=10, pady=5)

# GUI INPUT ENTRY FOR MEDICINE TIMES
medicine_times_entry = Entry(input_frame, width=20, font=("Helvetica", 14), bd=2, relief="groove")
medicine_times_entry.grid(row=1, column=1, padx=10, pady=5)

# Create a frame to hold buttons
button_frame = Frame(myframe, bg="#419ebe")
button_frame.pack(pady=20)

# Create the Add button
b1 = Button(button_frame, text="Add", height=2, width=15, bg="#a3dde9", command=submit_medicine_gui, bd=3, relief="raised")
b1.config(font=("Helvetica", 12, "bold"))
b1.pack(side="left", padx=20)

# Create the Reset button (optional)
b2 = Button(button_frame, text="Reset", height=2, width=15, bg="#a3dde9",command=reset_entries, bd=3, relief="raised")
b2.config(font=("Helvetica", 12, "bold"))
b2.pack(side="right", padx=20)

# Create a text widget to display the output
outputtxt = Text(myframe, height=8, width=40, font=("Helvetica", 12), bg="#a3dde9", fg="black", bd=2, relief="sunken", wrap=WORD)
outputtxt.pack(pady=10)
outputtxt.config(state=DISABLED)

# GUI setup
myframe.title("MEDICINE REMINDER")
myframe.geometry("600x600")
myframe.resizable(False, False)

# Tkinter main loop
myframe.mainloop()

# After closing the GUI, start checking for notifications
noti.check_time()

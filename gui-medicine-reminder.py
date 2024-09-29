from tkinter import *
from PIL import Image, ImageTk

myframe = Tk()

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

# Create a frame to hold the input fields and buttons, and match the title color
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
label4 = Label(input_frame, text="Enter Times to Take Medicine:", bg="#a3dde9", pady=10, padx=10, fg="black")
label4.config(font=("Helvetica", 12))
label4.grid(row=1, column=0, padx=10, pady=5)

# GUI INPUT ENTRY FOR MEDICINE TIMES
medicine_times_entry = Entry(input_frame, width=20, font=("Helvetica", 14), bd=2, relief="groove")
medicine_times_entry.grid(row=1, column=1, padx=10, pady=5)

# Create a frame to hold buttons, and match the title color
button_frame = Frame(myframe, bg="#419ebe")
button_frame.pack(pady=20)

# Create the Add button
b1 = Button(button_frame, text="Add", height=2, width=15, bg="#a3dde9", bd=3, relief="raised")
b1.config(font=("Helvetica", 12, "bold"))
b1.pack(side="left", padx=20)

# Create the Reset button
b2 = Button(button_frame, text="Reset", height=2, width=15, bg="#a3dde9", bd=3, relief="raised")
b2.config(font=("Helvetica", 12, "bold"))
b2.pack(side="right", padx=20)

# Create a text widget to display the output
outputtxt = Text(myframe, height=8, width=40, font=("Helvetica", 12), bg="#a3dde9", fg="black", bd=2, relief="sunken", wrap=WORD)
outputtxt.pack(pady=10)
outputtxt.config(state=DISABLED)

# GUI SETUP
myframe.title("MEDICINE REMINDER")
myframe.geometry("600x600")
myframe.resizable(False, False)  # Make the window size fixed
myframe.mainloop()

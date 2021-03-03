# Import the necessary libraries
try:
    # Python2
    from Tkinter import *
    from datetime import datetime
    from PIL import Image
except ImportError:
    # Python3
    from tkinter import *
    from datetime import datetime
    from PIL import Image, ImageTk
    import pandas as pd

# Control properties
title = "QUT Aerospace Welcome Night"

# FUNCTIONS
def process_member(evnet = None):
    student_ident = student_id.get()

    if len(student_ident) > 8:
        student_ident_check = student_ident[1:9]
    else:
        student_ident_check = student_ident[1:]

    print(f"Student Id: {student_ident}")
    print(f"Time in: {datetime.now()}")


    if student_ident_check in student_ids:
        name = csv_data.loc[csv_data['Student Number'] == student_ident[:9].upper(), 'Full Name'].iloc[0]
        print("bla")
        print(name)
        results_text['fg']='green'
        print("Existing Member")
        results_text['text'] = "Welcome, " + str(name) + "!"
        
    else:
        results_text['fg'] = 'orange'
        print("New Member")
        results_text['text'] = "Welcome, " + str(student_ident) + "!"
        

    student_id.delete(0, END)
    output_file.write(str(student_ident) + "," + str(datetime.now()) + "\n")


# File Handling
csv_data = pd.read_csv("Membership_List.csv")
ids = csv_data['Student Number']
ids.dropna(axis=0, inplace = True)
student_ids = ids.to_list()
student_ids = list(map(lambda x: x[1:], student_ids))

# Create an output file
output_file = open(str(datetime.now().date())+'_log.txt', 'x')


# Main root window to place everything on
root = Tk()
root.geometry("1920x1080")
root.configure(bg='white')

# Window title
root.title(title)

# Banner Image
canvas = Canvas(root, width = 1600, height = 400, bg='white', border = 0)      
canvas.grid(row = 0, column = 0, columnspan = 5, padx = 20, pady=5)
##banner_img = PhotoImage(file = 'banner.gif')

image = Image.open('banner.gif')
image = image.resize((1300, 350), Image.ANTIALIAS) ## The (250, 250) is (height, width)
banner_img = ImageTk.PhotoImage(image)

canvas.create_image(20,20, anchor=NW, image=banner_img)


# Create a text field to display the results (NB: On a Mac this
# text box allows vertical scrolling with the mouse wheel by
# default)
results_text = Label(root, width = 26, height = 8, font = 'halvatica 24 bold', fg='green', bg='white')
results_text.grid(row = 1, column = 0, columnspan = 2, rowspan= 4, padx = 20, pady = 5)

# Create labels for the three text entry fields
Label(root, text = 'By entering the S901 LABS you are agreeing that:', font = 'Arial 24 bold', bg='white').\
    grid(row = 1, column = 2, columnspan = 1, sticky = W, padx=20, pady=20)

rules_text="""
 1. You have not recently returned from a COVID hot spot in the last 14 days.
 2. You have not been in contact with a person confirmed sick with COVID-19. 
 3. You do not have any of the following symptoms “Having travelled overseas” in last 14 \n    days: Fever, cough, runny nose, shortness of breath & other symptoms.
 4. You do not have any of the following symptoms “Without having travelled”: Fever, \n    cough, runny nose, shortness of breath and other symptoms. 
"""

rules = Text(root, font = ('Arial', 20), wrap = WORD, width = 72, height = 10, relief = "flat")
rules.insert(INSERT, rules_text)
rules.grid(row = 2, column = 2,  columnspan = 1, rowspan=5, sticky = W, padx=25)



# Entry field
student_id = Entry(root, font = ('Courier', 20), justify = RIGHT)
student_id.grid(row = 5, column = 0, columnspan = 2, padx = 5, pady = 5)


# Allow users to start the search by typing a carriage return
root.bind('<Return>', process_member)

# Start the event loop
root.mainloop()

output_file.close()






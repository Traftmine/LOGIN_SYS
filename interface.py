from tkinter import *
import login_sys as ls

#Create an instance of Tkinter frame
window = Tk()

#Set the geometry of Tkinter frame
window.geometry("750x550")

usernameFrame = Frame(window,bg="gray",width=100,height=20)
usernameFrame.place(relx=0.5, rely=0.05,anchor='center')
LABEL=Label(usernameFrame, text="Username").pack()

passwordFrame = Frame(window,bg="gray",width=100,height=20)
passwordFrame.place(relx=0.5, rely=0.20,anchor='center')
LABEL=Label(passwordFrame, text="Password").pack()

# Create text widget and specify size.
T = Text(window, height = 5, width = 52)
T.place(relx=0.5, rely=0.60,anchor='center')

def getUsername():
    T.delete("1.0","end")
    global username_get
    global password_get
    username = username_get.get()
    password = password_get.get()
    Fact = ls.user_login(password,username)
    T.insert(END, str(Fact))

#Create an Entry widget to accept User Input
username_get = Entry(window, width= 40)
username_get.focus_set()
username_get.place(relx=0.5, rely=0.10,anchor='center')

password_get = Entry(window, width= 40)
password_get.focus_set()
password_get.place(relx=0.5, rely=0.25,anchor='center')

#Create a Button to validate Entry Widget
register = Button(window, text= "Register",width= 20, command= ls.creation_account)
register.place(relx=0.5, rely=0.4, anchor='w')

login = Button(window, text= "Login",width= 20, command= getUsername)
login.place(relx=0.5, rely=0.4, anchor='e')

exit = Button(window, text= "Exit",width= 20, command= window.quit)
exit.place(relx=0.5, rely=0.75,anchor='s')

window.mainloop()
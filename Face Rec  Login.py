from tkinter import *
from tkinter import messagebox
from PIL import ImageTk


def Login():
    if UserNameEntry.get() == '' or PasswordEntry.get() == '':
        messagebox.showerror('Error', 'Fields cannot be empty')

    elif UserNameEntry.get() == 'Batch 17' and PasswordEntry.get() == '1234':
        messagebox.showinfo('Success', 'Welcome...')
        window.destroy()
        import GUI_Face_Recoginzer
    else:
        messagebox.showerror('Error', 'Please enter correct details ')


window = Tk()

window.geometry('990x660+0+0') #('1280x700+0+0')
window.title('Login system of a Face Recgnition System ')

window.resizable(False, False)

backgroundImage = ImageTk.PhotoImage(file='bg.jpg')

bgLabel = Label(window, image=backgroundImage)
bgLabel.place(x=0, y=0)

LoginFrame = Frame(window, bg='white')
LoginFrame.place(x=550, y=150) #(x=400, y=150)

LogoImage = PhotoImage(file='AAA.png')

LogoLabel = Label(LoginFrame, image=LogoImage)
LogoLabel.grid(row=0, column=0, columnspan=2, pady=10)
UserNameImage = PhotoImage(file='user.png')
UserNameLabel = Label(LoginFrame, image=UserNameImage, text=' UserName',
                      compound=LEFT, font=('times new roman', 8, 'bold'), bg='white')

UserNameLabel.grid(row=1, column=0, pady=10, padx=20)

UserNameEntry = Entry(LoginFrame, font=(
    'times new roman', 8, 'bold'), bd=2, fg='royal blue')
UserNameEntry.grid(row=1, column=1, pady=10, padx=20)

PasswordImage = PhotoImage(file='password.png')
PasswordLabel = Label(LoginFrame, image=PasswordImage, text=' Password',
                      compound=LEFT, font=('times new roman', 8, 'bold'), bg='white')

PasswordLabel.grid(row=2, column=0, pady=10, padx=20)

PasswordEntry = Entry(LoginFrame, font=(
    'times new roman', 8, 'bold'), bd=2, fg='royal blue')
PasswordEntry.grid(row=2, column=1, pady=10, padx=20)

LoginButton = Button(LoginFrame, text='Login', font=('times new roman', 12, 'bold'), width=10, fg='white',
                     bg='cornflowerblue', activebackground='cornflowerblue', activeforeground='white', cursor='hand2', command=Login)
LoginButton.grid(row=3, column=1, pady=10)


window.mainloop()

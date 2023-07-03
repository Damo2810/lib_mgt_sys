from tkinter import *

root = Tk()
root.title("Library management system")
root.geometry('650x350')

main_lb= Label(root, text="Library management system",font=('calibre',20,'bold'))

main_lb.pack()

frame = Frame(root, highlightbackground="grey", highlightthickness=2)
frame.pack(padx= 20 ,pady= 20)

frame.place(relx=0.5,rely=0.5,anchor="center")

username_label = Label(frame, text="Username" , font=('calibre',10,'bold'))
username_entry = Entry(frame, width= 25, font=('calibre',10,'normal'))
password_label = Label(frame, text="password" ,font=('calibre',10,'bold'))
password_entry = Entry(frame, width= 25, font=('calibre',10,'bold'), show='*')

username_label.grid(row=0,column=0,padx=10,pady=10)
username_entry.grid(row=0,column=1,padx=10,pady=10)
password_label.grid(row=1,column=0,padx=10,pady=10)
password_entry.grid(row=1,column=1,padx=10,pady=10)


login_bt = Button(frame, text="LOGIN" , font=('calibre',10,'bold'))

login_bt.grid(row=2,columnspan=2 ,padx=20,pady=20)

root.mainloop()
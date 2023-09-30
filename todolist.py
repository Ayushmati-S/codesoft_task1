from tkinter import *
from tkinter.font import Font

root = Tk()
root.configure(background="Cyan")
root.title('To-Do List')
root.geometry("750x500")
my_font = Font(family="Calibri", size=22, weight="bold")
my_frame = Frame(root)
my_frame.pack(pady=10)

my_list = Listbox(my_frame, font=my_font, width=40, height=7, bg="White", bd=0, fg="Grey", highlightthickness=0, selectbackground="Cyan", activestyle="none")
my_list.pack(side=LEFT, fill=BOTH)
my_scrollbar = Scrollbar(my_frame)
my_scrollbar.pack(side=RIGHT, fill=BOTH)
my_list.config(yscrollcommand=my_scrollbar.set)
my_scrollbar.config(command=my_list.yview)
my_entry = Entry(root, font=("Calibri", 22), width=26, bg='White')
my_entry.pack(pady=20)

button_frame = Frame(root, bg='Blue')
button_frame.pack(pady=20)
def delete_item():
    my_list.delete(ANCHOR)
def add_item():
    my_list.insert(END, my_entry.get())
    my_entry.delete(0, END)


    while count < my_list.size():
        if my_list.itemcget(count, "fg") == "blue":
            my_list.delete(my_list.index(count))
        else:
            count += 1
            
delete_button = Button(button_frame, text="Delete Item", command=delete_item, bg="Blue", font=("Comic Sans MS", 12, "bold"))
add_button = Button(button_frame, text="Add Item", command=add_item, bg="Blue", font=("Comic Sans MS", 12, "bold"))

delete_button.grid(row=0, column=0)
add_button.grid(row=0, column=1, padx=20)

root.mainloop()
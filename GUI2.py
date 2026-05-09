from tkinter import*


def sum():
  try:
    n1 = int(entry1.get())
    n2 = int(entry2.get())
    result = n1 + n2
    result_label.config(text = "sum = " + str(result))
  except ValueError:
    result_label.config(text = "Error: Please enter valid numbers")

root = Tk()
root.title("Addition GUI")
root.geometry('1200x800')

entry1 = Entry(root)
entry1.pack()

entry2 = Entry(root)
entry2.pack()

button = Button(root,text = 'Add Two numbers' ,command=sum)
button.pack()

result_label = Label(root ,text = "sum = ")
result_label.pack()

root.mainloop()
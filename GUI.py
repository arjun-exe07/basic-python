from tkinter import* 
from tkinter import messagebox

'''
  CLASS :-
    1) Tk() -> Creates application window

  METHODS :-
  1) title(name) -> Gives name to the GUI.
  2) geometry(width x height)  -> Error handling : Don't give space ex. (200x400)
  ) mainloop()  -> Starts teh event Loop



  FUNCTIONS :-
  1) Label(master, option = value)
  2) Button(master, option = value)
    
  
'''


def button_clicked() :
  msg = messagebox.showinfo("Success" , "Button clicked succesfully")

root = Tk()
root.title("MY First GUI")
root.geometry('1600x1000')
label = Label(root,text = "Welcome !!!")
label.pack()
but = Button(root, text = "Stop" , command = root.destroy)
but.pack()


l2 = Label(root, text= "Click the box below")
l2.pack()

b2 = Button(root , text= "click me " ,command = button_clicked)
b2.pack()
root.mainloop()
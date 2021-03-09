from tkinter import *
root = Tk()
root.title("To Do List App")
root.geometry("400x400")

e = Entry(root)
e.grid(row=2, column=1, columnspan=2)

# to keep track of the amount of todos, so that we know on what row
# to add the new one
amountOfToDos = 1

# deletes a todo
def deleteToDo(toDoLabel, deleteButton):
    toDoLabel.destroy()
    deleteButton.destroy()


# adds a todo
def createToDo(number):
    global amountOfToDos
    # add 2, as the label is on row 2, so we want the todos
    # to appear after it
    number += 2
    toDo = e.get()
    toDoLabel = Label(root, text=toDo)
    toDoLabel.grid(row=number, column=1)
    deleteButton = Button(
        root, text="done", command=lambda: deleteToDo(toDoLabel, deleteButton))
    deleteButton.grid(row=number, column=2)
    e.delete(0, END)
    # add 1 to the amount of todos, after finshing it
    amountOfToDos += 1


label = Label(root, text="Enter your to do here: ")
label.grid(row=1, column=1)

button = Button(root, text="submit", command=lambda: createToDo(amountOfToDos))
button.grid(row=1, column=2)

root.mainloop()

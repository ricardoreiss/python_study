"""from tkinter import *

root = Tk()
scrollbar = Scrollbar(root)
scrollbar.pack( side = RIGHT, fill = Y )

mylist = Listbox(root, yscrollcommand = scrollbar.set, height=20 )
for line in range(100):
   mylist.insert(END, "This is line number " + str(line))

mylist.pack( side = LEFT, fill = BOTH )


scrollbar.config( command = mylist1.yview)

mainloop()"""
import tkinter as tk
from tkinter import *
from tkinter import ttk


root = Tk()
root.title('Codemy.com - TreeView')

style = ttk.Style()
style.theme_use("clam")
#Pick a theme
style.configure("Treeview", background="silver")
style.configure('Treeview.Heading', background="green", font=('Calibri', 20))

# Change selected color
style.map('Treeview', background=[('selected', 'blue')])

# Create Treeview Frame
tree_frame = Frame(root)
tree_frame.grid(row=0)

# Treeview Scrollbar
tree_scroll = Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT, fill=Y)

# Create Treeview
my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, height=5)
# Pack to the screen
my_tree.pack()

#Configure the scrollbar
tree_scroll.config(command=my_tree.yview)

# Define Our Columns
my_tree['columns'] = ("Name", "ID", "Favorite Pizza")

# Formate Our Columns
my_tree.column("#0", width=0, stretch=NO)
my_tree.column("Name", anchor=W, width=140)
my_tree.column("ID", anchor=CENTER, width=100)
my_tree.column("Favorite Pizza", anchor=W, width=140)

# Create Headings
my_tree.heading("#0", text="", anchor=W)
my_tree.heading("Name", text="Name", anchor=W)
my_tree.heading("ID", text="ID", anchor=CENTER)
my_tree.heading("Favorite Pizza", text="Favorite Pizza", anchor=W)

# Add Data
data = [
	["John", 1, "Pepperoni"],
	["Mary", 2, "Cheese"],
	["Tim", 3, "Mushroom"],
	["Erin", 4, "Ham"],
	["Bob", 5, "Onion"],
	["Steve", 6, "Peppers"],
	["Tina", 7, "Cheese"],
	["Mark", 8, "Supreme"],
	["John", 1, "Pepperoni"],
	["Mary", 2, "Cheese"],
	["Tim", 3, "Mushroom"],
	["Erin", 4, "Ham"],
	["Bob", 5, "Onion"],
	["Steve", 6, "Peppers"],
	["Tina", 7, "Cheese"],
	["Mark", 8, "Supreme"],
	["John", 1, "Pepperoni"],
	["Mary", 2, "Cheese"],
	["Tim", 3, "Mushroom"],
	["Erin", 4, "Ham"],
	["Bob", 5, "Onion"],
	["Steve", 6, "Peppers"],
	["Tina", 7, "Cheese"],
	["Mark", 8, "Supreme"],
	["Ruth", 9, "Vegan"]
]

# Create striped row tags




for record in data:
	my_tree.insert(parent='', index='end', text="", values=(record[0], record[1], record[2]))

add_frame = Frame(root)
add_frame.grid(row=5)

#Já deixar um item selecionado
list =  my_tree.get_children()
my_tree.selection_set(list[0])
my_tree.focus(list[0])
my_tree.focus_force()

#Labels
nl = Label(add_frame, text="Name")
nl.grid(row=0, column=0)

il = Label(add_frame, text="ID")
il.grid(row=0, column=1)

tl = Label(add_frame, text="Topping")
tl.grid(row=0, column=2)

#Entry boxes
name_box = Entry(add_frame)
name_box.grid(row=1, column=0)

id_box = Entry(add_frame)
id_box.grid(row=1, column=1)

topping_box = Entry(add_frame)
topping_box.grid(row=1, column=2)

#Cleam Boxes
def cleam_box():
	# Clear the boxes
	name_box.delete(0, END)
	id_box.delete(0, END)
	topping_box.delete(0, END)
# Add Record
def add_record():
	my_tree.insert(parent='', index='end', text="", values=(name_box.get(), id_box.get(), topping_box.get()))

	cleam_box()

# Remove all records
def remove_all():
	for record in my_tree.get_children():
		my_tree.delete(record)

	cleam_box()
# Remove one selected
def remove_one():
	x = my_tree.selection()[0]
	my_tree.delete(x)

	cleam_box()
# Remove many selected
def remove_many():
	x = my_tree.selection()
	for record in x:
		my_tree.delete(record)

# Select Record
def select_record(e):
	# Clear entry boxes
	cleam_box()

	# Grab record number
	selected = my_tree.focus()
	# Grab record values
	values = my_tree.item(selected, 'values')

	#temp_label.config(text=values[0])

	# output to entry boxes
	name_box.insert(0, values[0])
	id_box.insert(0, values[1])
	topping_box.insert(0, values[2])


# Save updated record
"""def update_record():
	# Grab record number
	selected = my_tree.focus()
	# Save new data
	my_tree.item(selected, text="", values=(name_box.get(), id_box.get(), topping_box.get()))

	# Clear entry boxes
	name_box.delete(0, END)
	id_box.delete(0, END)
	topping_box.delete(0, END)

# Create Binding Click function"""
def clicker(e):
	select_record()

# Move Row up
def up():
	rows = my_tree.selection()
	for row in rows:
		my_tree.move(row, my_tree.parent(row), my_tree.index(row)-1)

# Move Row Down
def down():
	rows = my_tree.selection()
	for row in reversed(rows):
		my_tree.move(row, my_tree.parent(row), my_tree.index(row)+1)



#Buttons

add_record = Button(root, text="Add Record", command=add_record)
add_record.grid(row=10)

# Remove all
remove_all = Button(root, text="Remove All Records", command=remove_all)
remove_all.grid(row=12)

remove_one = Button(root, text="Remove One Selected", command=remove_one)
remove_one.grid(row=14)

def teste(e):
	print('uyygu')

# Bindings
#my_tree.bind("<Double-1>", clicker)
my_tree.bind("<ButtonRelease-1>", select_record)
root.bind('<Return>', teste)

root.mainloop()
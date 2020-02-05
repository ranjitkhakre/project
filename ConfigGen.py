from tkinter import *
from jinja2 import Environment
from jinja2 import FileSystemLoader

root = Tk()
root.title("Config Generator")
root.geometry("750x750+0+0")

heading = Label(root, text="Switch Interface Config Generator", font=("arial", 25, "bold"), fg="steelblue").pack()

labell = Label(root, text="Enter Interface : ", font=("arial",12, "bold"), fg="black").place(x=10, y=50)

name= StringVar()
entry_box = Entry(root, textvariable=name, width=25, bg="lightgreen").place(x=280, y=50)

labell1 = Label(root, text="Enter Server Name: ", font=("arial",12, "bold"), fg="black").place(x=10, y=75)

name2= StringVar()
entry_box1 = Entry(root, textvariable=name2, width=25, bg="lightgreen").place(x=280, y=75)

labell2 = Label(root, text="Enter Vlan Number: ", font=("arial",12, "bold"), fg="black").place(x=10, y=100)

name3= StringVar()
entry_box2 = Entry(root, textvariable=name3, width=25, bg="lightgreen").place(x=280, y=100)


def do_it():
	#print("Hello" +str(name.get()))
    interf = str(name.get())
    sname = str(name2.get())
    vlan = str(name3.get()) 

    j2_env = Environment(loader=FileSystemLoader('templates'), trim_blocks=True)

    templates = j2_env.get_template('temp_1.j2')

    rendered_file = templates.render(interf=interf, sname=sname, vlan=vlan)
   
    #labell4 = Label(root, text=rendered_file, font=("arial",10, "bold"), fg="black").place(x=10, y=120)
         
    #print(rendered_file)
    text = Text(root,  width=500, height=600, wrap=WORD)
    text.insert(INSERT, rendered_file)
    text.pack()

Work = Button(root, text="Generate", width=9, height=3, bg="lightblue", command=do_it).place(x=550, y=50)


root.mainloop()
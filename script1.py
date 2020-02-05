import tkinter as tk
from tkinter import *
from jinja2 import Environment
from jinja2 import FileSystemLoader

ROOT = tk.Tk()

ROOT.withdraw()

interf = simpledialog.askstring(title="Interface", prompt="Enter interface :")
sname = simpledialog.askstring(title="Server name", prompt="Enter server name :")
vlan = simpledialog.askstring(title="vlan", prompt="Enter vlan no :")

j2_env = Environment(loader=FileSystemLoader('templates'), trim_blocks=True)

templates = j2_env.get_template('temp_1.j2')

rendered_file = templates.render(interf=interf, sname=sname, vlan=vlan)

print(rendered_file)
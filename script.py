
from jinja2 import Environment
from jinja2 import FileSystemLoader

interf = input("Enter interface : ")
sname = input("Enter server name : ") 
vlan = input("Enter vlan no : ") 

j2_env = Environment(loader=FileSystemLoader('templates'), trim_blocks=True)

templates = j2_env.get_template('temp_1.j2')

rendered_file = templates.render(interf=interf, sname=sname, vlan=vlan)

print(rendered_file)

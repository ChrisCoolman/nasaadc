from ursina import *

app = Ursina()

#e1 = Entity(model="quad", texture="texture_name", position=Vec3(-6.5,3.5,3), scale=(2.65,1,1))

#Define antennas
antenna1 = Text(text="Antenna 1", scale=2, x=-0.8, y=0.4, color=color.red)
antenna2 = Text(text="Antenna 2", scale=2, x=-0.2, y=0.4)
antenna3 = Text(text="Antenna 3", scale=2, x=0.4, y=0.4, color=color.blue)

#Define selection and info text
selection_text = Text(text="", scale=2, x=0, y=0.4, color=color.green)
info_text = Text(text="", x=0, y=0.3)

#Variable to keep track of the current selection
current_selection = None

def update():
    #Clear text only if no selection is made
    if current_selection is None:
        selection_text.text = ""
        info_text.text = ""

def input(key):
    global current_selection

    #Check which key is pressed and update the selection
    if key == '1':
        current_selection = "1"
        selection_text.text = "(selected)"
        selection_text.x = -0.56
        info_text.text = "info for antenna 1 here"
        info_text.x = -0.8
    elif key == '2':
        current_selection = "2"
        selection_text.text = "(selected)"
        selection_text.x = 0.05
        info_text.text = "info for antenna 2 here"
        info_text.x = -0.2
    elif key == '3':
        current_selection = "3"
        selection_text.text = "(selected)"
        selection_text.x = 0.64
        info_text.text = "info for antenna 3 here"
        info_text.x = 0.4
    elif key == 'escape':  #Allow deselecting with the escape key
        current_selection = None
        selection_text.text = ""
        info_text.text = ""

app.run()

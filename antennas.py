from ursina import *
from math_stuff import calculations
import math
import data


app = Ursina()

#variables for the equation
pt=float(10.0)
gt=float(9.0)
losses=19.43
nr=0.55
greek_11=0.136363636
kb=-228.6
ts=float(22) 
Ds54 = data.Ds54
Ds54_data = data.Ds54_data
Ds24 = data.Ds24
Ds24_data = data.Ds24_data
Ds34 = data.Ds34
Ds34_data = data.Ds34_data
i=0
for x in Ds54:
    print (x)
    i+=1
    if x == "1":
        print (Ds54_data[i])

i=0
for x in Ds24:
    print (x)
    i+=1
    if x == "1":
        print (Ds24_data[i])

i=0
for x in Ds34:
    print (x)
    i+=1
    if x == "1":
        print (Ds34_data[i])


#squares around each antenna
e1 = Entity(model="quad", texture="texture_name", position=Vec3(-6.4,3.5,3), scale=(2.65,1,1), color=color.black)
e2 = Entity(model="quad", texture="texture_name", position=Vec3(-0.75,3.5,3), scale=(2.65,1,1), color=color.black)
e3 = Entity(model="quad", texture="texture_name", position=Vec3(4.9,3.5,3), scale=(2.65,1,1), color=color.black)

#bottom left text
bottomleft = Text(text="Press 1, 2, or 3 to select an Antenna. Press Esc to deselect.", scale=2, x=-0.85, y=-0.4)

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
i=3
def input(key):
    global current_selection,i

    DR=float(70)
    #R=float(17)
    out=float(0)
    
    #Check which key is pressed and update the selection
    if key == '1':

        current_selection = "1"
        selection_text.text = "(selected)"
        selection_text.x = -0.54
<<<<<<< HEAD
        info_text.text = "info for antenna 1 here\n" + str(calculations(DR, Ds54_data[i], out))
=======
        info_text.text = "Calculations for Antenna 1: \n" + str(calculations(DR, R, out))
>>>>>>> 44e1a0e788f98f454c31f8e3a9829852a108e1ea
        info_text.x = -0.8
    elif key == '2':
        current_selection = "2"
        selection_text.text = "(selected)"
        selection_text.x = 0.06
        info_text.text = "Calculations for Antenna 2:\n" + str(calculations(DR, R, out))
        info_text.x = -0.2
    elif key == '3':
        current_selection = "3"
        selection_text.text = "(selected)"
        selection_text.x = 0.66
        info_text.text = "Calculations for Antenna 3:\n" + str(calculations(DR, R, out))
        info_text.x = 0.4
    elif key == 'escape':  #deselecting with the escape key
        current_selection = None
        selection_text.text = ""
        info_text.text = ""

app.run()

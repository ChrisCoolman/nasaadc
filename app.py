from ursina import *
import time
import math
import data


app = Ursina(title='Astroworlds')
Earth = Entity(model="sphere", texture="earth.jpg")
Moon = Entity(model="sphere", texture="moon.jpg")
Orion = Entity(model="Orion.obj")
Arrow = Entity(model="ballcam.obj", position=(-5, 39.588, -15), scale=2.6, color=color.gray)

orionSpeed = 1


txt = Text(text="X = " + str(time.dt + 1), position=(-.78, .4))
txt2 = Text(text="Z = " + str(time.dt + 1), position=(-.78, .4))
txt3 = Text(text="Y = " + str(time.dt + 1), position=(-.78, .4))
text4 = Text(text="Orion Speed = " + str(orionSpeed), position=(-78, .4))

#for time timer
elapsedTime = 0
timerText = Text(text="00:00", position=(-.78, .43))

a = Audio("woosh.mp3", loop=False, autoplay=False)

earthLock = False
moonLock = False
orionLock = False

window.color = color.black

# Set up Moon
Moon.scale = (75,75,75)
Moon.position = (float(data.orionX[6489])/100, float(data.orionY[6150])/100, float(data.orionZ[6489])/100)

# Set up Earth
Earth.scale = (39.588, 39.588, 39.588)

# Orion
Orion.scale = 0.05
orionX = data.orionX[1]
orionY = data.orionY[2]
orionZ = data.orionZ[3]
cout = 0

# Create a custom camera
camera_pivot = Entity()
camera.parent = camera_pivot
editor_camera = EditorCamera(enabled=True)

# Initial camera setup
camera.position = (0, 0, -40)
camera_pivot.enabled = False

size = len(data.orionX) - 3

points = []

for i in range(1, size):
   points.append(Vec3(float(data.orionX[i])/100, float(data.orionY[i])/100, float(data.orionZ[i])/100))

curve_renderer = Entity(model=Mesh(vertices=points, mode='line'))


#for i in range(1, len(data.orionX) - 3):
#    Entity(model="sphere", position=(float(data.orionX[i])/100, float(data.orionY[i])/100, float(data.orionZ[i])/100), scale=2, color=color.red)
def input(key):
    global earthLock, moonLock, a, orionLock, orionSpeed
    if key == 'f':
        a.play()
        moonLock = False
        earthLock = not earthLock
        # Toggle between EditorCamera and locked camera
        editor_camera.enabled = not earthLock
        camera_pivot.enabled = earthLock
    elif key == 'm':
        a.play()
        earthLock = False
        moonLock = not moonLock
        editor_camera.enabled = not moonLock
        camera_pivot.enabled = moonLock
    elif key == 'r':  # New key to focus on Orion
        a.play()
        earthLock = False
        moonLock = False
        orionLock = not orionLock
        editor_camera.enabled = not orionLock
        camera_pivot.enabled = orionLock
    elif key == 'g' and orionSpeed < 15:
        # Slow Down Time
        application.time_scale += 1
        orionSpeed += 1
        if application.time_scale >= 15:
            application.time_scale = 15
    elif key == 'h' and orionSpeed > 0:
        application.time_scale -= 1
        orionSpeed -= 1
        if application.time_scale < 0:
            application.time_scale = 0

def update():
    global orionX, orionZ, orionY, elapsedTime, cout, orionSpeed
    
    cout+=orionSpeed
    if cout > 12978:
        cout = 1
    else:
        Orion.position = (float(data.orionX[cout])/100, float(data.orionY[cout])/100, float(data.orionZ[cout])/100)


    # Rotate Earth and Moon
    Earth.rotation_y += time.dt 

    Orion.look_at(Moon)

    # Smooth camera following
    if earthLock:
        target_pos = Earth.position + Vec3(0, 3, -5)
        camera_pivot.position = lerp(camera_pivot.position, target_pos, time.dt * 5)
        camera_pivot.look_at(Earth)

    elif moonLock:
        target_pos = Moon.position + Vec3(0, 3, -5)
        camera_pivot.position = lerp(camera_pivot.position, target_pos, time.dt * 5)
        camera_pivot.look_at(Moon)

    # orionX += time.dt*5
    #Orion.position = (orionX, orionY, orionZ)
    Arrow.look_at(Orion, axis="up")
    
    txt.text="X = " + str(orionX)
    txt.position=(-.78, .4)

    txt2.text="Z = " + str(orionZ)
    txt2.position=(-.78, .37)

    txt3.text="Y = " + str(orionY)
    txt3.position=(-.78, .34)

    text4.text="Orion speed = " + str(orionSpeed)
    text4.position = (0, 0)


    
    elapsedTime += time.dt
    mins = int(elapsedTime) // 60
    secs = int(elapsedTime) % 60
    timerText.text = f"{mins:02}:{secs:02}"

skybox_image = load_texture("stars.jpg")
Sky(texture=skybox_image)

app.run()

from ursina import *
import time
import data
import speed


width = 6000
height = 4000
app = Ursina(title='Astroworlds', width = 600, height = 400)
Earth = Entity(model="sphere", texture="earth.jpg")
Moon = Entity(model="sphere", texture="moon.jpg")
Orion = Entity(model="Orion.obj")
Arrow = Entity(model="ballcam.obj", position=(-5, 39.588, -15), scale=2.6, color=color.gray)

orionSpeed = 1


key_text = Text(
    text="KEY:\nGreen: Rocket Going\nBlue: Rocket Coming Back",
    position=(-.85, .50),
    color=color.white,
    scale=0.8
)

txt = Text(text="X = " + str(time.dt + 1), position=(-.28, .4))
txt2 = Text(text="Z = " + str(time.dt + 1), position=(-.28, .4))
txt3 = Text(text="Y = " + str(time.dt + 1), position=(-.28, .4))
# orionSpeed = 5
txt4 = Text(text="Orion Speed = " + str(orionSpeed), position=(-.85, .3))


#for time timer
elapsedTime = 0
timerText = Text(text="00:00", position=(-.78, .43))

a = Audio("woosh.mp3", loop=False, autoplay=False)

earthLock = False
moonLock = False
orionLock = False

window.color = color.black

# Set up Moon
Moon.scale = (50,50,50)
Moon.position = (float(data.orionX[6489])/100, float(data.orionY[6150])/100, float(data.orionZ[6489])/100)

# Set up Earth
Earth.scale = (75,75,75)

# Orion
Orion.scale = 0.09
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

half = 6488 # i think this is half

points = []
otherPoints = []

for i in range(1, size - half):
   points.append(Vec3(float(data.orionX[i])/100, float(data.orionY[i])/100, float(data.orionZ[i])/100))

curve_renderer = Entity(model=Mesh(vertices=points, mode='line'), color=color.green)

for i in range(size-half, size):
   otherPoints.append(Vec3(float(data.orionX[i])/100, float(data.orionY[i])/100, float(data.orionZ[i])/100))

second_curve_renderer = Entity(model=Mesh(vertices=otherPoints, mode='line'), color=color.blue)


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
        txt.text = "X = " + str(data.orionX[cout])
        txt.position = (-.78, .4)

        txt2.text = "Y = " + str(data.orionY[cout])
        txt2.position = (-.78, .37)

        txt3.text = "Z = " + str(data.orionZ[cout])
        txt3.position = (-.78, .34)


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

    txt4.text="Orion speed = " + str(orionSpeed)
    # txt4.position = (0, 0)


    
    elapsedTime += time.dt
    mins = int(elapsedTime) // 60
    secs = int(elapsedTime) % 60
    timerText.text = f"{mins:02}:{secs:02}"

skybox_image = load_texture("stars.jpg")
Sky(texture=skybox_image)

app.run()

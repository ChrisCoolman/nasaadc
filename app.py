from ursina import *
import math
import data


app = Ursina(title='Astroworlds')
Earth = Entity(model="sphere", texture="earth.jpg")
Moon = Entity(model="sphere", texture="moon.jpg")
Orion = Entity(model="Orion.obj")
Arrow = Entity(model="ballcam.obj", position=(20,0,-20), scale=0.5, color=color.gray)

txt = Text(text="X = " + str(time.dt + 1), position=(-.78, .4))
txt2 = Text(text="Z = " + str(time.dt + 1), position=(-.78, .4))
txt3 = Text(text="Y = " + str(time.dt + 1), position=(-.78, .4))

a = Audio("woosh.mp3", loop=False, autoplay=False)

earthLock = False
moonLock = False
orionLock = False

window.color = color.black

moon_orbit_radius = 238
moon_orbit_speed = 0.5
moon_orbit_angle = 0

# Set up Moon
Moon.scale = (9.897, 9.897, 9.897)

# Set up Earth
Earth.scale = (395.88, 395.88, 395.88)

# Orion
Orion.scale = 0.005
orionX = 15
orionY = 0
orionZ = 15

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
    global earthLock, moonLock, a, orionLock
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
    elif key == 'g':
        # Slow Down Time
        application.time_scale += 1
        if application.time_scale >= 15:
            application.time_scale = 15
    elif key == 'h':
        application.time_scale -= 1
        if application.time_scale < 0:
            application.time_scale = 0

def update():
    global moon_orbit_angle, orionX, orionZ, orionY
    
    # Rotate Earth and Moon
    Earth.rotation_y += time.dt 
    
    # Update Moon's orbital position relative to Earth
    moon_orbit_angle += time.dt * moon_orbit_speed
    moonX = math.cos(moon_orbit_angle) * moon_orbit_radius
    moonZ = math.sin(moon_orbit_angle) * moon_orbit_radius
    
    # Update Moon's position
    Moon.position = Earth.position + Vec3(moonX, 0, moonZ)

    # Smooth camera following
    if earthLock:
        target_pos = Earth.position + Vec3(0, 3, -5)
        camera_pivot.position = lerp(camera_pivot.position, target_pos, time.dt * 5)
        camera_pivot.look_at(Earth)

    elif moonLock:
        target_pos = Moon.position + Vec3(0, 3, -5)
        camera_pivot.position = lerp(camera_pivot.position, target_pos, time.dt * 5)
        camera_pivot.look_at(Moon)

    orionX = float(data.orionX[1])
    orionY = float(data.orionY[1])
    orionZ = float(data.orionZ[1])


    # orionX += time.dt*5
    Orion.position = (orionX, orionY, orionZ)
    Arrow.look_at(Orion, axis="up")
    
    txt.text="X = " + str(orionX)
    txt.position=(-.78, .4)

    txt2.text="Z = " + str(orionZ)
    txt2.position=(-.78, .37)

    txt3.text="Y = " + str(orionY)
    txt3.position=(-.78, .34)

skybox_image = load_texture("stars.jpg")
Sky(texture=skybox_image)

app.run()

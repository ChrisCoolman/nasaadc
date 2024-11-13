from ursina import *

import math


app = Ursina(title='Astroworlds')


# Define entities

Earth = Entity(model="sphere", texture="earth.jpg")

Moon = Entity(model="sphere", texture="moon.jpg")

Orion = Entity(model="Orion.obj")


# Text information display

txt = Text(text="X = " + str(time.dt + 1), position=(-.78, .4))

txt2 = Text(text="Z = " + str(time.dt + 1), position=(-.78, .4))

txt3 = Text(text="Y = " + str(time.dt + 1), position=(-.78, .4))


# Audio setup

a = Audio("woosh.mp3", loop=False, autoplay=False)


# Camera lock variables

earthLock = False

moonLock = False

orionLock = False  # New lock variable for Orion


# Window color

window.color = color.black


# Moon orbital properties

moon_orbit_radius = 238

moon_orbit_speed = 0.5

moon_orbit_angle = 0


# Set up Moon scale

Moon.scale = (9.897, 9.897, 9.897)


# Set up Earth scale

Earth.scale = (39.588, 39.588, 39.588)


# Set up Orion position and scale

Orion.position = (15, 0, 15)

Orion.scale = 0.005


# Initial Orion coordinates

orionX = Orion.position.x

orionZ = Orion.position.z

orionY = Orion.position.y


# Create a custom camera

camera_pivot = Entity()

camera.parent = camera_pivot

editor_camera = EditorCamera(enabled=True)


# Initial camera setup

camera.position = (0, 0, -40)

camera_pivot.enabled = False


def input(key):

    global earthLock, moonLock, orionLock, a


    if key == 'f':

        a.play()

        moonLock = False

        orionLock = False

        earthLock = not earthLock

        editor_camera.enabled = not earthLock

        camera_pivot.enabled = earthLock


    elif key == 'm':

        a.play()

        earthLock = False

        orionLock = False

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

        # Slow down time

        application.time_scale += 1


    elif key == 'h':

        # Speed up time

        application.time_scale -= 1


def update():

    global moon_orbit_angle, orionX, orionZ, orionY

    

    # Rotate Earth

    Earth.rotation_y += time.dt 

    

    # Update Moon's orbital position relative to Earth

    moon_orbit_angle += time.dt * moon_orbit_speed

    moonX = math.cos(moon_orbit_angle) * moon_orbit_radius

    moonZ = math.sin(moon_orbit_angle) * moon_orbit_radius

    

    # Update Moon's position

    Moon.position = Earth.position + Vec3(moonX, 0, moonZ)


    # Smooth camera following based on lock status

    if earthLock:

        target_pos = Earth.position + Vec3(0, 3, -5)

        camera_pivot.position = lerp(camera_pivot.position, target_pos, time.dt * 5)

        camera_pivot.look_at(Earth)


    elif moonLock:

        target_pos = Moon.position + Vec3(0, 3, -5)

        camera_pivot.position = lerp(camera_pivot.position, target_pos, time.dt * 5)

        camera_pivot.look_at(Moon)


    elif orionLock:  # Camera following Orion

        target_pos = Orion.position + Vec3(0, 3, -5)

        camera_pivot.position = lerp(camera_pivot.position, target_pos, time.dt * 5)

        camera_pivot.look_at(Orion)

    

    # Update text coordinates

    txt.text = "X = " + str(orionX)

    txt.position = (-.78, .4)


    txt2.text = "Z = " + str(orionZ)

    txt2.position = (-.78, .37)


    txt3.text = "Y = " + str(orionY)

    txt3.position = (-.78, .34)


# Set up skybox

skybox_image = load_texture("stars.jpg")

Sky(texture=skybox_image)


app.run()
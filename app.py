from ursina import *
from ursina.shaders import lit_with_shadows_shader
import math

app = Ursina(title='Astroworlds')
Earth = Entity(model="sphere", texture="earth.jpg")
Sun = Entity(model="sphere", texture="sun.jpg")
Moon = Entity(model="sphere", texture="moon.jpg")

earthLock = False

window.color = color.black

earth_orbit_radius = 162 # Changed from 92.522
earth_orbit_speed = 0.1
earth_orbit_angle = 0

moon_orbit_radius = 23.8
moon_orbit_speed = 0.5
moon_orbit_angle = 0

# Create a custom camera
camera_pivot = Entity()
camera.parent = camera_pivot
editor_camera = EditorCamera(enabled=True)

def input(key):
    global earthLock
    if key == 'f':
        a = Audio("woosh.mp3", loop=False, autoplay=False)
        a.play()
        earthLock = not earthLock
        # Toggle between EditorCamera and locked camera
        editor_camera.enabled = not earthLock
        camera_pivot.enabled = earthLock
    elif key == 'g':
        # Slow Down Time
        application.time_scale += 1
    elif key == 'h':
        application.time_scale -= 1

def update():
    global earth_orbit_angle, moon_orbit_angle
    
    # Rotate Earth and Moon
    Earth.rotation_y += time.dt * 100
    Moon.rotation_y += time.dt * 1000

    # Update Earth's orbital position
    earth_orbit_angle += time.dt * earth_orbit_speed
    earthX = math.cos(earth_orbit_angle) * earth_orbit_radius
    earthZ = math.sin(earth_orbit_angle) * earth_orbit_radius
    
    # Update Earth's position
    Earth.position = (earthX, 0, earthZ)
    
    # Update Moon's orbital position relative to Earth
    moon_orbit_angle += time.dt * moon_orbit_speed
    moonX = math.cos(moon_orbit_angle) * moon_orbit_radius
    moonZ = math.sin(moon_orbit_angle) * moon_orbit_radius
    
    # Update Moon's position
    Moon.position = Earth.position + Vec3(moonX, 0, moonZ)

    # Smooth camera following
    if earthLock:
        target_pos = Earth.position + Vec3(0, 5, -10)
        camera_pivot.position = lerp(camera_pivot.position, target_pos, time.dt * 5)
        camera_pivot.look_at(Earth)

# Set up Sun
Sun.position = (0, 0, 0)
Sun.scale = (109.255, 109.255, 109.255)

# Set up Moon
Moon.scale = (0.25, 0.25, 0.25)

# Set up Earth
Earth.scale = (1, 1, 1)

# Initial camera setup
camera.position = (0, 0, -20)
camera_pivot.enabled = False

skybox_image = load_texture("stars.jpg")
Sky(texture=skybox_image)

app.run()
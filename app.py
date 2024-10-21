from ursina import *
from ursina.shaders import lit_with_shadows_shader
import math

app = Ursina()
Earth = Entity(model="sphere", texture="earth.jpg")
Sun = Entity(model="sphere", texture="sun.jpg")
Moon = Entity(model="sphere", texture="moon.jpg")

window.color = color.black

earth_orbit_radius = 92.522
earth_orbit_speed = 0.1
earth_orbit_angle = 0

moon_orbit_radius = 3  # Adjust this value to change the Moon's distance from Earth
moon_orbit_speed = 0.5  # Adjust this value to change the Moon's orbit speed
moon_orbit_angle = 0

def update():
    global earth_orbit_angle, moon_orbit_angle
    
    # Rotate Earth and Moon
    Earth.rotation_y += time.dt * 100  # Adjust the rotation speed as needed
    Moon.rotation_y += time.dt * 1000  # Adjust the rotation speed as needed

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

# Set up Sun
Sun.position = (0, 0, 0)
Sun.scale = (109.255, 109.255, 109.255)

# Set up Moon
Moon.scale = (0.25, 0.25, 0.25)

# Set up Earth
Earth.scale = (1, 1, 1)

# Set up camera
EditorCamera()
camera.position = (0, 0, 0)


skybox_image = load_texture("stars.png")
Sky(texture=skybox_image)

app.run()
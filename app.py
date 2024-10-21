from ursina import *
from ursina.shaders import lit_with_shadows_shader

app = Ursina()

def update():
    Earth.rotation_y += time.dt * 100  # Adjust the rotation speed as needed
    Moon.rotation_y += time.dt * 1000  # Adjust the rotation speed as needed
    Sun.rotation_y += time.dt * 10  # Adjust the rotation speed as needed
    

Earth = Entity(model="sphere", texture="earth.jpg")
Sun = Entity(model="sphere", texture="sun.jpg")
Moon = Entity(model="sphere", texture="moon.jpg")

Sun.position = (2000, 0, 2000)
Sun.scale = (200, 200, 200)

Moon.position = (5, 0, 5)
Earth.scale = (4, 4, 4)

EditorCamera()
sin = DirectionalLight()
sin.position = Sun.position
app.run()

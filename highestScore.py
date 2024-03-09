import math
import pyautogui
from time import sleep

def point_rotation(x, y, degrees):
    # Convert degrees to radians
    angle_radians = degrees * (math.pi / 180)

    # Rotation matrix
    rotation_matrix = [
        [math.cos(angle_radians), -math.sin(angle_radians)],
        [math.sin(angle_radians), math.cos(angle_radians)]
    ]

    # Apply rotation
    x_prime = rotation_matrix[0][0] * x + rotation_matrix[0][1] * y
    y_prime = rotation_matrix[1][0] * x + rotation_matrix[1][1] * y

    return x_prime, y_prime


center_of_circle = (960, 550) # Different on other screens
radius = 375
vertices = 0.006

sleep(2)

pyautogui.moveTo(center_of_circle[0]+radius, center_of_circle[1])
pyautogui.mouseDown()

for i in range(2*int(360*vertices)):
    

    mouse_coord = (pyautogui.position().x, pyautogui.position().y)
    rotation = 360 / (360 * vertices)

    mouse_coord_prime = point_rotation(
        mouse_coord[0]-center_of_circle[0],
        mouse_coord[1]-center_of_circle[1],
        rotation)
    
    pyautogui.moveTo(
        mouse_coord_prime[0] + center_of_circle[0],
        mouse_coord_prime[1] + center_of_circle[1],
        )
    
pyautogui.mouseUp()

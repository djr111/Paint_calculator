def wall(a, b):

    area = a * b
    return area


def door():
    door_width = input ("Please enter door width :")
    door_height = input ("Please enter door height :")
    door_area = float(door_width) * float(door_height)
    print("Door size in square meters : " + str(door_area))
    return door_area




def window():
    window_width = input ("Please enter window width")
    window_height = input("Please enter window height")
    window_area = float(window_height) * float(window_width)
    print("Window size in square meters:" + str(window_area))
    return window_area



def paint():
    wall_height = float(input("Enter height of the wall in meters: "))
    wall_lenght = float(input("Enter lenght of the wall in meters: "))

    paint_needed = (wall(wall_lenght, wall_height) - door() - window()) / 6
    return paint_needed


print("You will need : " + str(paint()) + " amount of cans to paint")


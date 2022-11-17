print ("Welcome to Paint-calculator")

def wall():
    wall_width = input("Please enter wall width you want to paint: ")
    wall_height = input("Please enter wall height you want to paint: ")
    wall_area = float(wall_width) * float(wall_height)
    print("Total surface area of wall in square meters : " + str(wall_area))
    return wall_area


def socket():
    socket_width = input ("Please enter socket's width you want to paint: ")
    socket_height = input ("Please enter socket's height you want to paint: ")
    socket_area = float(socket_width) * float(socket_height)
    print("Total surface area of sockets in square meters : " + str(socket_area))
    return socket_area


def door():
    door_width = input ("Please enter door width you want to paint: ")
    door_height = input ("Please enter door height you want to paint: ")
    door_area = float(door_width) * float(door_height)
    print("Total surface area of door in square meters : " + str(door_area))
    return door_area


def window():
    window_width = input ("Please enter window width you want to paint: ")
    window_height = input("Please enter window height you want to paint: ")
    window_area = float(window_height) * float(window_width)
    print("Total surface area of window in square meters:" + str(window_area))
    return window_area


def paint():

    paint_needed = (wall() - door() - window() - socket()) / 6
    return paint_needed


print("You will need : " + str(paint()) + " amount of cans to paint")


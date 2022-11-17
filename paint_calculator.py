print("Welcome to Paint-calculator")


def wall():
    wall_width = input("Please enter wall width you want to paint: ")
    wall_height = input("Please enter wall height you want to paint: ")
    wall_number = input("How many walls you have to paint?: ")
    wall_area = float(wall_width) * float(wall_height) * int(wall_number)
    print("Total surface area of wall in square meters : " + str(wall_area))
    return wall_area


def socket():
    socket_width = input ("Please enter socket's width : ")
    socket_height = input ("Please enter socket's height : ")
    socket_number = input("How many sockets you have ?: ")
    socket_area = float(socket_width) * float(socket_height) * int(socket_number)
    print("Total surface area of sockets in square meters : " + str(socket_area))
    return socket_area


def door():
    door_width = input ("Please enter door width : ")
    door_height = input ("Please enter door height : ")
    door_number = input("How many doors you have ?: ")
    door_area = float(door_width) * float(door_height) * int(door_number)
    print("Total surface area of door in square meters : " + str(door_area))
    return door_area


def window():
    window_width = input ("Please enter window width : ")
    window_height = input("Please enter window height : ")
    window_number = input("How many windows you have ?: ")
    window_area = float(window_height) * float(window_width) * int(window_number)
    print("Total surface area of window in square meters:" + str(window_area))
    return window_area


def coats_of_paint():
    coat_amount = int(input("Please enter amount of coats you would like to use: "))
    return coat_amount


def paint():

    paint_needed = (wall() - door() - window() - socket()) / 6 * (coats_of_paint())
    return paint_needed


print("You will need : " + str(paint()) + " amount of cans to paint")


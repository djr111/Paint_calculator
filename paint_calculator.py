import math

print("Welcome to Paint-calculator")


while True:
    proceed = input("Please type GO to proceed further with program : ")
    if proceed == "GO":
        break
    else:
        print("Wrong input Robot  ")


def wall():
    wall_width = input("Please enter wall width you want to paint: ")
#    if not isinstance(wall_width, float):
#        raise TypeError('wall width should be number')
    wall_height = input("Please enter wall height you want to paint: ")
    wall_number = input("How many walls you have to paint?: ")
    wall_area = float(wall_width) * float(wall_height) * int(wall_number)
    print("Total surface area of wall in square meters : " + str(wall_area))
    return wall_area


def socket():
    socket_width = input("Please enter socket's width : ")
    socket_height = input("Please enter socket's height : ")
    socket_number = input("How many sockets you have ?: ")
    socket_area = float(socket_width) * float(socket_height) * int(socket_number)
    print("Total surface area of sockets in square meters : " + str(socket_area))
    return socket_area


def door():
    door_width = input("Please enter door width : ")
    door_height = input("Please enter door height : ")
    door_number = input("How many doors you have ?: ")
    door_area = float(door_width) * float(door_height) * int(door_number)
    print("Total surface area of door in square meters : " + str(door_area))
    return door_area


def window():
    window_width = input("Please enter window width : ")
    window_height = input("Please enter window height : ")
    window_number = input("How many windows you have ?: ")
    window_area = float(window_height) * float(window_width) * int(window_number)
    print("Total surface area of window in square meters:" + str(window_area))
    return window_area


def coats_of_paint():
    coat_amount = int(input("Please enter amount of coats you would like to use: "))
    return coat_amount


paint_cans = {
    2.5: 30,
    5: 60,
    10: 120
}
# Dulux Silk Paint - Amazon


def painting():
    #   Modern Emulsion 60 m2 per 5 litres / 30m2 per 2.5 litres
    paint_needed = (wall() - door() - window() - socket()) / 12 * (coats_of_paint())
    return round(paint_needed)


def paint_cans_needed(area):
    big = 0
    medium = 0
    small = 0
    one = 0

    if area >= 10:
        big += math.floor(area/10)
        area -= math.floor(area/10) * 10
    if area >= 5:
        medium += math.floor(area/5)
        area -= math.floor(area/5) * 5
    if area >= 2.5:
        small += math.floor(area/2.5)
        area -= math.floor(area/2.5) * 2.5

 #   if area > 0:
 #       one += math.ceil(area/1)
 #       area -= math.ceil(area/1) * 1

    return ["10l --: " + str(big), "5l --: " + str(medium), "2.5l --: " + str(small)]


area1 = painting()
print("You will need : " + str(area1) + " amount of litres of paint")
print("Paint cans needed : " + str(paint_cans_needed(area1)) + " for the job done")


#  valid = False
#   while not valid:
#       try:
#            type(wall_width) == float
#           valid = True
#      except ValueError:
#           print("Entered value is not number")
# return wall_width

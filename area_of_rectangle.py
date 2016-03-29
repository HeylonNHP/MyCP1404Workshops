def get_rectangle_area(length,width):
    return length * width

length = float(input("Enter length "))
width = float(input("Enter width "))

print("The area is {}".format(get_rectangle_area(length, width)))

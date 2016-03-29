def calculate_body_mass_index(weight,height):
    return weight / height**2

weight = float(input("Enter weight in KG "))
height = float(input("Enter height in Meters"))

print("Your BMI is {:,.2f}".format(calculate_body_mass_index(weight,height)))

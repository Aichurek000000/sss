name = input("Enter a name: ")
surname = input("Enter a surname: ")
license_plate = input("Enter a license plate num: ")

def check_license_plate(plate):
    if plate[4].isalpha() and plate[5].isdigit() and (plate[6].isalpha() or len(plate) == 7):
        return "Your license is an old one"
    elif plate[:3].isdigit() and plate[3:].isalpha() and len(plate) == 6:
        return "Your license is a new one"
    else:
        return "No valid license plate"

plate_type = check_license_plate(license_plate)

message = f"{name} {surname}, {license_plate}, {plate_type}."
print(message)
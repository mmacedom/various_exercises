preheat = int(input("Enter the preheat temperature:"))

def convert_to_celsius(preheat):
    return (preheat - 32) * (5/9)

temp = convert_to_celsius(preheat)

def preheat_time(temp):
    room_temp = 20
    degrees_per_min = 20
    preheat_time = (temp - room_temp) // degrees_per_min
    print(preheat_time)
    
device_status = "active"
if device_status == "active":
    temperature = int(input("Enter the temperature: "))
    if(temperature > 35):
        print("High temperature alert!")
    else:
        print("Normal Temperature")
else:
    print("Device is offline")

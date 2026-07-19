# Parent Class
class SmartDevice:
    def __init__(self, name, device_id):
        self.name = name
        self.__device_id = device_id
        self.__status = "OFF"

    # Getter
    def get_device_id(self):
        return self.__device_id

    # Setter
    def set_device_id(self, device_id):
        self.__device_id = device_id

    def turn_on(self):
        self.__status = "ON"
        print(self.name, "is ON")

    def turn_off(self):
        self.__status = "OFF"
        print(self.name, "is OFF")

    def display(self):
        print("\nName:", self.name)
        print("Device ID:", self.__device_id)
        print("Status:", self.__status)


# Child Class 1
class SmartLight(SmartDevice):
    def brightness(self):
        print("Brightness changed.")


# Child Class 2
class SmartFan(SmartDevice):
    def speed(self):
        print("Fan speed changed.")


# Child Class 3
class SmartDoor(SmartDevice):
    def lock(self):
        print("Door locked.")


# Objects
light = SmartLight("Light", "L001")
fan = SmartFan("Fan", "F001")
door = SmartDoor("Door", "D001")


# Menu
while True:
    print("\nSMART DEVICE MENU")
    print("1. Display Devices")
    print("2. Turn ON")
    print("3. Turn OFF")
    print("4. Change Light Brightness")
    print("5. Change Fan Speed")
    print("6. Lock Door")
    print("7. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        light.display()
        fan.display()
        door.display()

    elif choice == "2":
        light.turn_on()
        fan.turn_on()
        door.turn_on()

    elif choice == "3":
        light.turn_off()
        fan.turn_off()
        door.turn_off()

    elif choice == "4":
        light.brightness()

    elif choice == "5":
        fan.speed()

    elif choice == "6":
        door.lock()

    elif choice == "7":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")
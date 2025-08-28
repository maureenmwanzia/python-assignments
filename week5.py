# -------------------------------
# Base Class: Device
# -------------------------------
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def device_info(self):
        return f"{self.brand} {self.model}"

    # Polymorphic method (each child will override this)
    def move(self):
        raise NotImplementedError("Subclass must implement move()")


# -------------------------------
# Smartphone Class (inherits Device)
# -------------------------------
class Smartphone(Device):
    def __init__(self, brand, model, storage, battery):
        super().__init__(brand, model)   # Inherit brand & model
        self.storage = storage
        self.__battery = battery   # Encapsulation (private)

    def call(self, contact):
        print(f"📞 Calling {contact} from {self.device_info()}...")

    def charge(self, amount):
        self.__battery = min(100, self.__battery + amount)
        print(f"🔋 Battery charged to {self.__battery}%")

    def get_battery(self):
        return self.__battery

    # Polymorphic method
    def move(self):
        print(f"📱 {self.device_info()} is portable: You can carry it anywhere!")


# -------------------------------
# Other Devices (to show polymorphism)
# -------------------------------
class Laptop(Device):
    def move(self):
        print(f"💻 {self.device_info()} moves around in a backpack!")

class Smartwatch(Device):
    def move(self):
        print(f"⌚ {self.device_info()} stays on your wrist while you move!")


# -------------------------------
# MAIN PROGRAM
# -------------------------------
if __name__ == "__main__":
    # Create some objects
    phone = Smartphone("Samsung", "Galaxy S24", "256GB", 50)
    laptop = Laptop("Dell", "XPS 15")
    watch = Smartwatch("Apple", "Watch Series 9")

    # Encapsulation demo
    phone.call("Maureen")
    phone.charge(30)
    print(f"Phone Battery: {phone.get_battery()}%")

    print("\n--- Polymorphism Demo ---")
    devices = [phone, laptop, watch]
    for d in devices:
        d.move()   # same method name, different behaviors!

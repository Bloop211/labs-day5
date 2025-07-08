from dataclasses import dataclass, field

@dataclass
class Smartlamp:
    name: str
    color: str = "white"
    brightness: int = 100
    is_on: bool = field(default=False, init=False)
        
    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def set_brightness(self, percent):
        if percent > 100 or percent < 0:
            raise ValueError("Brightness must be between 0 and 100")
        else:
            self.brightness = percent
    
    def set_color(self, color):
        self.color = color
        
    def status(self):
        return (f"{self.name} is {'on' if self.is_on else 'off'}, {self.color}, and {self.brightness}% bright")
    
    def power_outage(self):
        self.is_on = False
        print(f"{self.name} has been turned off due to power outage")

if __name__ == "__main__":
    lamp = Smartlamp("Lamp 1")
    lamp.is_on = not lamp.is_on
    lamp.set_brightness(50)
    lamp.set_color("grey")
    print(lamp.status())
    lamp = Smartlamp("Lamp 2")
    lamp.is_on = not lamp.is_on
    lamp.set_brightness(20)
    lamp.set_color("black")
    print(lamp.status())
    lamp.power_outage()

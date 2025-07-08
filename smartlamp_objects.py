from dataclasses import dataclass, field

@dataclass
class Smartlamp:
    name: str
    color: str = "white"
    brightness: int = 100
    is_on: bool = field(default=False, init=False)
    _registry = []
    
    def __post_init__(self):
        self._registry.append(self)
    
    @classmethod
    def power_outage(cls):
        for lamp in cls._registry:
            lamp.is_on = False
        print("All lamps have been turned off (power outage).")
        
    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def toggle(self):
        self.is_on = not self.is_on

    def set_brightness(self, percent):
        if percent > 100 or percent < 0:
            raise ValueError("Brightness must be between 0 and 100")
        else:
            self.brightness = percent
    
    def set_color(self, color):
        self.color = color
        
    def status(self):
        return (f"{self.name} is {'on' if self.is_on else 'off'}, {self.color}, and {self.brightness}% bright")

if __name__ == "__main__":
    lamp1 = Smartlamp("Lamp 1")
    lamp1.set_brightness(50)
    lamp1.set_color("grey")
    print(lamp1.status())
    lamp2 = Smartlamp("Lamp 2")
    lamp2.toggle()
    lamp2.set_brightness(20)
    lamp2.set_color("black")
    print(lamp2.status())
    Smartlamp.power_outage()
    print(lamp1.status())
    print(lamp2.status())
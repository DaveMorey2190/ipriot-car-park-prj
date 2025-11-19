from sensor import Sensor
from display import Display

class CarPark:
    def __init__(self, location, capacity, plates = None, display = None):
        self.location = location
        self.displays = displays or []
        
    def register(self, component):
        if not isinstance(component, (Sensor, Display)):
            raise TypeError("Object must be a sensor or display.")
        if isinstance(component, Sensor):
            self.sensors.append(component)
        elif isinstance(component, Display):
            self.displays.append(component)

    def __str__(self)
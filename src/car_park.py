from sensor import Sensor
from display import Display
from pathlib import Path
from datetime import datetime # we'll use this to timestamp entries

class CarPark:
    def __init__(self, location, capacity, plates=None, sensors=None, display=None, log_file=Path("log.txt")):
        self.location = location
        self.capacity = capacity
        self.plates = plates or []
        self.displays = display or []
        self.log_file = log_file if isinstance(log_file, Path) else Path(log_file)
        self.log_file.touch(exist_ok=True)
        
    def register(self, component):
        if not isinstance(component, (Sensor, Display)):
            raise TypeError("Object must be a sensor or display.")
        if isinstance(component, Sensor):
            self.sensors.append(component)
        elif isinstance(component, Display):
            self.displays.append(component)
            
    def add_car(self, plate):
        self.plates.append(plate)
        self.update_displays()
    
    def remove_car(self, plate):
        self.plates.remove(plate)
        self.update_displays()
        
    @property
    def available_bays(self):
        return max(0,self.capacity -len(self.plates))
    
    def update_displays(self):
        data = {"available_bays": self.available_bays,"temperature": 25}
        for display in self.displays: 
            display.update(data)  
            
    def _log_car_activity(self, plate, action):
        with self.log_file.open("a") as f:
            f.write(f"{plate} {action} at {datetime.now():%Y-%m-%d %H:%M:%S}\n")
            
    def add_car(self, plate):
        self.plates.append(plate)
        self.update_displays()
        self._log_car_activity(plate, "entered")

    def __str__(self):
        pass
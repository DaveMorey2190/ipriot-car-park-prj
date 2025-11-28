import json
from sensor import Sensor
from display import Display
from pathlib import Path
from datetime import datetime # we'll use this to timestamp entries

class CarPark:
    def __init__(self, location, capacity, plates=None, sensors=None, display=None, log_file=Path("log.txt"), config_file=Path("config.json")):
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
        self._log_car_activity(plate, "entered")
    
    def remove_car(self, plate):
        self.plates.remove(plate)
        self.update_displays()
        self._log_car_activity(plate, "exited")
        
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
            
    # def _log_car_activity(self, plate, action):
    #     with self.log_file.open("a") as f:
    #         f.write(f"{plate} {action} at {datetime.now()}\n")        
    
    def write_config(self):
        with self.config_file.open("w") as f: 
            json.dump({"location": self.location,
                        "capacity": self.capacity,
                        "log_file": str(self.log_file)}, f)
            
    @classmethod
    def from_config(cls, config_file=Path("config.json")):
        config_file = config_file if isinstance(config_file, Path) else Path(config_file)
        with config_file.open() as f:
            config = json.load(f)
        return cls(config["location"], config["capacity"], log_file=config["log_file"])
        

    def __str__(self):
        pass
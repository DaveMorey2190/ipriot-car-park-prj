from abc import ABC, abstractmethod

class Sensor(ABC):
    def __init__(self, id, is_active, car_park):
        self.id = id
        self.is_active = is_active
    
    @abstractmethod
    def update_car_park(self, plate):
        pass

    def _scan_plate(self):
        return 'FAKE' + format(rand.randint(0,999),"03d")
    
    def detect_vehicle(self):
        plate = self.scan_plate()
        self.update_car_park(plate)
    
    def __str__(self):
        pass
    
class EntrySensor(Sensor):
    def update_car_park(self, plate):
        self.car_park.add_car(plate)
        print(f"Incoming 🚘 vehicle detected. Plate: {plate}")
    
class ExitSensor(Sensor):
    def update_car_park(self, plate):
        self.car_park.remove_car(plate)
        print(f"Outgoing 🚗 vehicle detected. Plate: {plate}")
        
    def _scan_plate(self):
        return random.choice(self.car_park.plates)
import random
from abc import ABC, abstractmethod

class Sensor(ABC):
    """
    Base class for all sensors that interact with the car park.

    Sensors detect vehicles and update the CarPark object by calling update_car_park().
    Concrete subclasses must implement the update_car_park() method to define whether
    the sensor handles entry, exit, or other behaviour.

    Arguments
    ---------
    id : int
        Unique ID assigned to the sensor.
    is_active : bool
        Whether the sensor is currently enabled or not.
    car_park : CarPark
        Reference to the CarPark that this sensor updates.

    Returns
    -------
    Sensor
        An initialised sensor ready to detect vehicles and interact with the car park.

    Examples
    --------
    >>> sensor = EntrySensor(1, True, moondalup_carpark)
    >>> sensor.detect_vehicle()
    Incoming 🚘 vehicle detected. Plate: FAKE123
    """
    def __init__(self, id, is_active, car_park):
        self.id = id
        self.is_active = is_active
        self.car_park = car_park

    @abstractmethod
    def update_car_park(self, plate):
        pass

    def _scan_plate(self):
        return 'FAKE' + format(random.randint(0,999),"03d")
    
    def detect_vehicle(self,plate = None):
        plate = self._scan_plate()
        self.update_car_park(plate)
    
    def __str__(self):
        pass
    
class EntrySensor(Sensor):
    """
    Sensor responsible for detecting vehicles entering the car park.

    When a vehicle is detected, the sensor scans a licence plate and instructs the
    CarPark to add the vehicle. This updates internal tracking, displays, and logs.

    Arguments
    ---------
    id : int
        Unique sensor identifier.
    is_active : bool
        Whether the sensor is currently enabled or not.
    car_park : CarPark
        The car park is updated when a vehicle enters.

    Returns
    -------
    EntrySensor
        A configured entry sensor capable of detecting incoming vehicles.

    Examples
    --------
    >>> entry_sensor = EntrySensor(1, True, moondalup_carpark)
    >>> entry_sensor.detect_vehicle()
    Incoming 🚘 vehicle detected. Plate: FAKE042
    """
    def update_car_park(self, plate):
        self.car_park.add_car(plate)
        print(f"Incoming 🚘 vehicle detected. Plate: {plate}")
    
class ExitSensor(Sensor):
    """
    Sensor responsible for detecting vehicles exiting the car park.

    Unlike entry sensors, this sensor overrides _scan_plate() so the scanned plate
    is selected from vehicles currently inside the car park, ensuring only valid
    vehicles can be removed.

    Arguments
    ---------
    id : int
        Unique sensor identifier.
    is_active : bool
        Whether the sensor is currently enabled or not.
    car_park : CarPark
        The car park is updated when a vehicle exits.

    Returns
    -------
    ExitSensor
        A configured exit sensor capable of detecting outgoing vehicles.

    Examples
    --------
    >>> moondalup_carpark.add_car("CAR-001")
    >>> exit_sensor = ExitSensor(2, True, cp)
    >>> exit_sensor.detect_vehicle()
    Outgoing 🚗 vehicle detected. Plate: CAR-001
    """

    def update_car_park(self, plate):
        self.car_park.remove_car(plate)
        print(f"Outgoing 🚗 vehicle detected. Plate: {plate}")
        
    def _scan_plate(self):
        return random.choice(self.car_park.plates)
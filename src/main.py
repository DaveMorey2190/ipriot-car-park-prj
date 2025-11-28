from car_park import CarPark
from sensor import EntrySensor, ExitSensor
from display import Display
from pathlib import Path

def main():
    CarPark(location = "Moondalup", capacity=100, log_file="moondalup.txt", config_file=Path("moondalup_config.json"))
    car_park = CarPark.from_config(Path("moondalup_config.json"))
    # TODO: Reinitialize the car park object from the "moondalup_config.json" file
    # TODO: create an entry sensor object with id 1, is_active True, and car_park car_park
    # TODO: create an exit sensor object with id 2, is_active True, and car_park car_park
    # TODO: create a display object with id 1, message "Welcome to Moondalup", is_on True, and car_park car_park
    # TODO: drive 10 cars into the car park (must be triggered via the sensor - NOT by calling car_park.add_car directly)
    # TODO: drive 2 cars out of the car park (must be triggered via the sensor - NOT by calling car_park.remove_car directly)
    
    
    pass

if __name__ == "__main__":
    main()
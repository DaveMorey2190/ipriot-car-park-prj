from car_park import CarPark
from sensor import EntrySensor, ExitSensor
from display import Display
from pathlib import Path

def main():
    moondalup_car_park = CarPark(location="Moondalup", capacity=100, log_file="moondalup.txt")
    
    moondalup_car_park.config_file = Path("moondalup_config.json")
    moondalup_car_park.write_config()
    moondalup_car_park = CarPark.from_config(Path("moondalup_config.json"))

    entry_sensor = EntrySensor(id=1, is_active=True, car_park=moondalup_car_park)
    exit_sensor = ExitSensor(id=2, is_active=True, car_park=moondalup_car_park)

    display = Display(id=1, message="Welcome to Moondalup", is_on=True, car_park=moondalup_car_park)

    for car_count in range(10):
        plate = f"CAR-{car_count:03d}"
        entry_sensor.detect_vehicle(plate)

    for car_count in range(2):
        plate = f"CAR{car_count:03d}"
        exit_sensor.detect_vehicle(plate)


if __name__ == "__main__":
    main()
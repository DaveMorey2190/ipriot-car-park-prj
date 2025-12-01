# North Metro Software Python Project Template

Overview

A simple Python program that models a car park with sensors, displays, logging, and configuration saving/loading.

Class Summary

CarPark

    Stores location, capacity, current plates, sensors, and displays.

    Logs vehicle entries/exits to a text file.

    Saves configuration to JSON via write_config().

    Recreates an instance from a JSON file using from_config().

Sensor 

    Shared behaviour for all sensors.

    Holds an ID, activation state, and a reference to the CarPark.

EntrySensor

    Inherits from Sensor.

    Detects an incoming vehicle and tells the CarPark to add it.

ExitSensor

    Inherits from Sensor.

    Detects an outgoing vehicle and tells the CarPark to remove it.

Display

    Represents an on-site message board.

    Shows messages and updates when the car park's status changes.

Main 

    Creates a CarPark instance.

    Writes a config file and reloads the CarPark from it.

    Creates an EntrySensor, ExitSensor, and Display.

Simulates:

    10 entries, each adding a new plate.

    2 exits, attempting to remove existing plates.

## Additional Examples
Creating a car park with custom capacity and log file.

Loading a car park from an existing JSON config.

Simulating a vehicle entry using an EntrySensor.

Simulating a vehicle exit using an ExitSensor.

Updating a display after the bay count changes.

# Note
In this simulation, sensors generate licence plates automatically rather than relying on user input. Entry sensors create random "FAKE###" plates, while exit sensors randomly select a plate from the cars currently parked.


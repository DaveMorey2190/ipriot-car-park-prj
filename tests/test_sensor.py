import unittest
from sensor import Sensor
from sensor import ExitSensor
from car_park import CarPark

class TestExitSensor(unittest.TestCase):
    """
    Tests the ExitSensor class for correct initialization and vehicle removal functionality.

    Arguments
    ---------
    N/A

    Returns
    -------
    TestExitSensor
        A test suite verifying ExitSensor inherits from Sensor, initializes correctly, 
        and removes vehicles from the CarPark as expected.

    Examples
    --------
    >>> test_suite = TestExitSensor()
    >>> test_suite.test_sensor_initialized_with_all_attributes()
    """
    def setUp(self):
        self.carpark = CarPark("Example Location", 100)
        self.exit_sensor = ExitSensor( 2, is_active = True, car_park = self.carpark)

    def test_sensor_initialized_with_all_attributes(self):
        self.assertIsInstance(self.exit_sensor, ExitSensor)
        self.assertIsInstance(self.exit_sensor, Sensor)
        self.assertEqual(self.exit_sensor.id, 2)
        self.assertEqual(self.exit_sensor.is_active, True)
        self.assertEqual(self.exit_sensor.car_park, self.carpark)
        self.carpark.plates.append("TEST123")
        self.exit_sensor.detect_vehicle()
        self.assertNotIn("TEST123", self.carpark.plates)


        
   

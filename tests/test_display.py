import unittest
from display import Display
from car_park import CarPark

class TestDisplay(unittest.TestCase):
    """
    Tests the Display class for correct initialization and update behaviour.

    Arguments
    ---------
    N/A

    Returns
    -------
    TestDisplay
        A test suite verifying Display attribute initialization and that updates correctly 
        modify the display state.

    Examples
    --------
    >>> test_suite = TestDisplay()
    >>> test_suite.test_display_initialized_with_all_attributes()
    >>> test_suite.test_update()
    """
    def setUp(self):
        self.car_park = CarPark("Example Bay", 100)
        
        self.display = Display(id=1, message="Welcome to the car park", is_on=True, car_park = self.car_park)
    
    def test_display_initialized_with_all_attributes(self):
        self.assertIsInstance(self.display, Display)
        self.assertEqual(self.display.id, 1)
        self.assertEqual(self.display.message, "Welcome to the car park")
        self.assertEqual(self.display.is_on, True)
        
    def test_update(self):
        self.display.update({"message": "Goodbye"})
        self.assertEqual(self.display.message, "Goodbye")
class Display:
    """
    Represents a display device that shows live information from the car park.

    Displays can show available bays, temperature readings, messages, and other
    status updates. They maintain their own local state and print updates when
    new data is pushed to them.

    Arguments
    ---------
    id : int
        Identifier for the display unit.
    message : str, optional
        Initial message shown on the display.
    is_on : bool, optional
        Whether the display is currently powered on or not.
    car_park : CarPark, optional
        Reference to the CarPark providing data updates.

    Returns
    -------
    Display
        A display unit that is capable of receiving and showing updates.

    Examples
    --------
    >>> display = Display(1, "Welcome", True, cp)
    >>> display.update({"available_bays": 87})
    available_bays: 87
    """
    def __init__(self, id, message = "", is_on = False, car_park = None):
        self.id = id
        self.message = message
        self.is_on = is_on
        self.car_park = car_park
        
    def update(self, data):
        for key, value in data.items():
            print(f"{key}: {value}")    
            if key == "message":
                self.message = value
            elif key == "is_on":
                self.is_on = value
            else:
                self.data_values[key] = value
            
    def __str__(self):
        pass

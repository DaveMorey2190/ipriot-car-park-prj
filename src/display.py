class Display:
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

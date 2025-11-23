class Display:
    def __init__(self, id, message = "", is_on = False):
        self.id = id
        
    def update(self, data):
        for key, value in data.items():
            print(f"{key}: {value}")    
            
    def __str__(self):
        pass

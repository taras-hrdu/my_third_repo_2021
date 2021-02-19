class Camera:
    best_сamera = "GoPro"
    @staticmethod
    def best_camera():
        return Camera.best_сamera

    def __init__(self, name="No Values", memory_capacity=0, zoom_ratio=0, color="No Values", price=0, producer="No Values"): 
        self.name = name
        self.memory_capacity = memory_capacity
        self.zoom_ratio = zoom_ratio
        self.color = color
        self.price = price 
        self.producer = producer
        
    def __del__(self):
        print("Deleting an instance")
        
    def __str__(self):
        result = ("Name: "+self.name+ "\nMemory_capacity: "+str(self.memory_capacity)+ "\nZoom_ratio: "+str(self.zoom_ratio)+ "\nColor: "+self.color+
        "\nPrice: "+str(self.price)+ "\nProducer: "+self.producer)
        return result


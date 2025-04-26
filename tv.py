class TV:
    def __init__(self, channel=1, volumeLevel=1, on=False):
        # instance variables
        self.channel = channel
        self.volumeLevel = volumeLevel
        self.on = on
    
    def turnOn(self): # turn the tv on
        self.on = True
        print("turn on")
    
    def turnOff(self): # turn the tv off
        self.on = False
        print("turn off")
    
class TV:
    def __init__(self, channel=1, volumeLevel=1, on=False):
        # instance variables
        self.channel = channel
        self.volumeLevel = volumeLevel
        self.on = on
    
    def turnOn(self): # turn the tv on
        self.on = True
        print("turn on") # checking
    
    def turnOff(self): # turn the tv off
        self.on = False
        print("turn off") # checking
    
    def getChannel(self): # return the current channel
        return self.channel
    
    def setChannel(self, channel): # if the tv is on, set the channel number
        if self.on and 1 <= channel <= 120:
            self.channel = channel
            print(channel) # checking
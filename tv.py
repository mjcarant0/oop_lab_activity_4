class TV:
    def __init__(self, channel=1, volumeLevel=1, on=False):
        # instance variables
        self.channel = channel
        self.volumeLevel = volumeLevel
        self.on = on
    
    def turnOn(self): # turn the tv on
        self.on = True
    
    def turnOff(self): # turn the tv off
        self.on = False
    
    def getChannel(self): # return the current channel
        return self.channel
    
    def setChannel(self, channel): # if the tv is on, set the channel number
        if self.on and 1 <= channel <= 120:
            self.channel = channel
    
    def getVolume(self): # return the current volume
        return self.volumeLevel
    
    def setVolume(self, volumeLevel): # if the tv is on, set the volume level
        if self.on and 1 <= volumeLevel <= 7:
            self.volumeLevel = volumeLevel
    
    def channelUp(self): # increase the channel
        self.setChannel(self.channel + 1)
    
    def channelDown(self): # decrease the channel
        self.setChannel(self.channel - 1)
    
    def volumeUp(self): # increase the volume level
        self.setVolume(self.volumeLevel + 1)
    
    def volumeDown(self): # decrease the volume level
        self.setVolume(self.volumeLevel - 1)
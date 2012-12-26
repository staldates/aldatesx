from org.muscat.staldates.aldatesx.devices.SerialDevice import SerialDevice

class KramerVP703(SerialDevice):
    '''
    Kramer VP703-SC scan converter.
    '''


    def __init__(self, deviceID, serialDevice):
        super(KramerVP703, self).__init__(deviceID, serialDevice)
        
    def initialise(self):
        super(KramerVP703, self).initialise()
        self.overscanOn()
        
    def overscanOn(self):
        return self.sendCommand("Overscan = 1\r\n")
        
    def overscanOff(self):
        return self.sendCommand("Overscan = 0\r\n")
    
    def freeze(self):
        return self.sendCommand("Image Freeze = 1\r\n")
    
    def unfreeze(self):
        return self.sendCommand("Image Freeze = 0\r\n")
from org.muscat.staldates.aldatesx.devices.Device import Device
from serial import Serial, SerialException
import logging
from threading import Thread
import atexit


class SerialDevice(Device):
    '''
    A device we connect to over a serial port.
    '''

    def __init__(self, deviceID, serialDevice, baud=9600):
        '''
        Create a SerialDevice with a given device ID, using a new Serial with the given device address
        (e.g. "/dev/ttyUSB0") if given as a string, else assume serialDevice is a Serial and use that.
        If we fail to create a Serial with the given device, log an error and use a fake port.
        '''
        super(SerialDevice, self).__init__(deviceID)
        if isinstance(serialDevice, str) or isinstance(serialDevice, unicode):
            try:
                self.port = Serial(serialDevice, baud, timeout=2)
            except SerialException:
                logging.exception("Could not open serial device " + serialDevice + " for " + deviceID)
                self.port = FakeSerialPort()
        else:
            self.port = serialDevice

    def sendCommand(self, commandString):
        try:
            logging.debug("Sending " + commandString.encode('hex_codec') + " to " + self.port.portstr)
            sentBytes = self.port.write(commandString)
            logging.debug(str(sentBytes) + " bytes sent")
            return sentBytes
        except SerialException:
            logging.exception("Failed sending command to " + self.deviceID + " on " + self.port.portstr)

    @staticmethod
    def byteArrayToString(byteArray):
        return ''.join(chr(b) for b in byteArray)


class SerialListener(Thread):
    ''' Class to listen to and interpret incoming messages from a serial device.
        Should implement a process(message) method where message is the hex array received.
    '''

    dispatchers = []
    running = False

    def __init__(self, deviceID, parentDevice, messageSize=4):
        ''' parentDevice should be an already initialised SerialDevice. '''
        Thread.__init__(self)
        self.parentDevice = parentDevice
        self.deviceID = deviceID
        self.messageSize = messageSize
        atexit.register(self.stop)

    def registerDispatcher(self, dispatcher):
        self.dispatchers.append(dispatcher)

    def start(self):
        if not self.running:
            self.running = True
            Thread.start(self)

    def stop(self):
        self.running = False

    def initialise(self):
        self.start()

    def run(self):
        logging.info("Listening to serial port " + self.parentDevice.port.portstr)
        while self.running:
            message = [int(elem.encode("hex"), base=16) for elem in self.parentDevice.port.read(self.messageSize)]
            if len(message) == self.messageSize:
                mapp = self.process(message)
                for d in self.dispatchers:
                    d.updateOutputMappings({self.parentDevice.deviceID: mapp})
            elif len(message) != 0:
                logging.warn("Malformed packet from " + self.deviceID + ": " + SerialDevice.byteArrayToString(message).encode('hex_codec'))
        logging.info("No longer listening to serial port " + self.parentDevice.port.portstr)


class FakeSerialPort(object):
    '''
    A class that quacks like a Serial if you try and write to it, but just throws everything away.
    '''
    portstr = "FAKE"

    def write(self, stuff):
        return 0

    def read(self, length):
        return []

    def flushInput(self):
        return 0

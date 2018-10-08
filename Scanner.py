from bluepy.btle import Scanner, DefaultDelegate

class scanner(DefaultDelegate):



    def __init__(self,_,_,_): # creation and initialization of object
        pass
        super.__init__(self)


    def withDelegate(self): # to store  the reference of delegate object
        pass


    def scan(self): # scan for ble devices
        pass


    def clear(self):  # clear all the current discovered devices
        pass

    def start(self):  #  make it enable to start receving broadcast from the peripherals
        pass

    def stop(self):   #  Disable the reception of broadcast
        pass

    def getDevices(self):  # Return the list of all devices which have been discovered.
        pass



# constructor for creation and initialization of a new scanner object
scan = scanner(arguments)



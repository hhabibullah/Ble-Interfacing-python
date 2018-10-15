import bluepy
from bluepy.btle import DefaultDelegate, Peripheral
import struct

class batt_levelDelegate(DefaultDelegate):

    def __init__(self):
        self.data = None

    def  handleNotification(self, cHandle, data):
        self.data = self.battery_level(data)

    def battery_level(self,data):
        if len(data) == 3:
            (_, _, batt) = struct.unpack('<BBB', data)

            return { "batt": batt}
        else:
            return False


class NewConnectionTest:
    def __init__(self, name="", mac_addr="", addr_type="public", iface=0):
        self.p = Peripheral(mac_addr, addrType=addr_type, iface=iface)
        self.bleDelegate = batt_levelDelegate()
        self.p.withDelegate(self.bleDelegate)


    def get_data(self):
        self.p.waitForNotifications(1.0)
        #        print ("Notification Recieved: ", self.name)
        return self.bleDelegate.data

    def disconnect(self):
        self.p.disconnect()


print('Connecting to ec70')

try:
    a = NewConnectionTest(mac_addr='7C:EC:79:E4:5F:89', iface=0)
    #    for i in range(0,3):
    while True:
        data = a.get_data()
        print 'ec000 ', data

except Exception as e:
    print "Error %s" % str(e)


import nest
from nest import utils as nest_utils
import sys
import requests

class Nest:
    def __init__(self, username = None, password = None):
        self.username = 'ericmaras@gmail.com'
        self.password = 'Eric12!@'
        napi = nest.Nest(self.username, self.password)
        for structure in napi.structures:
            print 'Structure %s' % structure.name
            print '    Away: %s' % structure.away
            print '    Devices:'

            for device in structure.devices:
                print '        Device: %s' % device.name
                print '            Temp: %0.1f' % device.temperature
                print '            Humidity : %0.1f%%' % device.humidity
                print '            Target   : %0.1fC' % device.target
                print '            battery_level         : %s' % device.battery_level
        
        self.device = device
        self.temperature = self.c_to_f(device.temperature)
        self.target = device.target
        self.humidity = device.humidity
        self.battery_level = device.battery_level
        
        
    def set_target(self, temp):
        self.device.temperature = f_to_c(temp)
    
    def f_to_c(self, temp):
        return nest_utils.f_to_c(temp)

    def c_to_f(self, temp):
        return nest_utils.c_to_f(temp)

if __name__ == "__main__":
    nest = Nest()
    print 'Number of arguments:', len(sys.argv), 'arguments.'
    print 'Argument List:', str(sys.argv)
    print "The temperature in fucking Eric's house is " + str(nest.temperature)
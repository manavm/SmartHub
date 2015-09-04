
# coding: utf-8

# In[1]:

import nest
from nest import utils as nest_utils
import requests


# In[2]:

username = 'ericmaras@gmail.com'
password = 'Eric12!@'


# In[3]:

napi = nest.Nest(username, password)


# In[19]:

def fahrenheit_to_celsius(temp):
    return nest_utils.f_to_c(temp)

def celsius_to_fahrenheit(temp):
    return nest_utils.c_to_f(temp)


# In[29]:

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


# In[20]:

current_temp = celsius_to_fahrenheit(device.temperature)


# In[21]:

current_temp


# In[17]:

device.temperature = 24.444


# In[23]:

def get_temperature():
    return celsius_to_fahrenheit(temperature)

def set_temperature(temp):
    target_temp = temp


# In[ ]:




# In[ ]:




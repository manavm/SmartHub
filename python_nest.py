
# coding: utf-8

# In[1]:

import nest
import requests


# In[2]:

username = 'ericmaras@gmail.com'
password = 'Eric12!@'


# In[3]:

napi = nest.Nest(username, password)


# In[5]:

for structure in napi.structures:
    print 'Structure %s' % structure.name
    print '    Away: %s' % structure.away
    print '    Devices:'

    for device in structure.devices:
        print '        Device: %s' % device.name
        print '            Temp: %0.1f' % device.temperature


# In[6]:

device.temperature


# In[17]:

device.temperature = 24.444


# In[ ]:




# In[ ]:




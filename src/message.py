# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 00:51:31 2018

@author: abhis
"""
import time
import paho.mqtt.client as mqtt
from multiprocessing.managers import SyncManager

##################################################################
######code for syncronising payload when new location arrives#####
######send to flask app

class MyManager(SyncManager):
    pass

MyManager.register("syncdict")


manager = MyManager(("127.0.0.1", 8000), authkey="password")
manager.connect()
syncdict = manager.syncdict()
print ("dict = %s" % (dir(syncdict)))



def sync_payload(lat,lon):
    try:
        #updae latitutde 
        #if the key doesn't exist create it
         key='lat'
         if not syncdict.has_key(key):
             syncdict.update([(key, 0)])
         else:
              syncdict.update([(key,lat) ])
        #update longitude
         key='lon'
         if not syncdict.has_key(key):
             syncdict.update([(key, 0)])
         #increment key value every sleep seconds
         #then print syncdict
         else:
              syncdict.update([(key,lon) ])

    except KeyboardInterrupt:
         print ("Killed client")

##########################################################################
         
#######################code to connect with MQTT broker####################
broker = 'm11.cloudmqtt.com'
port  = 14037
client = mqtt.Client('api')
client.username_pw_set('api','test')
topic = 'owntracks/phone/phone'
mqtt.Client.connected_flag = False
mqtt.Client.bad_connection_flag=False


#callback response functions
def on_log(client, userdata, level, buf):
    print('log:',buf)
    
def on_connect(client,userdata,flags,rc):    
    if (rc==0):
        print ('connected')
        client.connected_flag=True
    else:
        print ('connection error:',rc)
        client.bad_connection_flag=True        

def on_disconnect(client,userdata,rc):
    client.connected_flag=False

def on_message(client, userdata, msg):
    payload = eval(msg.payload)
    lon = payload['lon']
    lat = payload['lat']
    print ('%s : lat=%f,lon=%f'%(msg.topic,lat,lon))
    sync_payload(lat,lon)
    
#assigning manual callbacks
client.on_connect = on_connect
client.on_log = on_log
client.on_message = on_message
client.on_disconnect=on_disconnect

##########################################

#try connection
print ('connecting to {}'.format(broker))

try:
    client.connect(broker,port)
except:
    print('error connecting')

client.loop_start()
while(not client.connected_flag and not client.bad_connection_flag):
    print ('waiting for connection')
    time.sleep(1)

client.subscribe(topic)
raw_input("Press any key to kill server".center(50, "-"))
client.loop_stop()


client.disconnect()




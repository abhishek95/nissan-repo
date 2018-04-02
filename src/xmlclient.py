# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 00:51:31 2018

@author: abhis
"""


import time
import xmlrpclib


server = xmlrpclib.ServerProxy('http://localhost:8000')
print (server)
try:
    print (server.update_loc(50,40))
    print('success')
except:
    print ('failed')
time.sleep(10)
try:
    print (server.update_loc(20,30))
    print('success')
except:
    print('failed')
    


import paho.mqtt.client as mqtt

broker = 'm11.cloudmqtt.com'
port  = 14037
client = mqtt.Client('api')
client.username_pw_set('api','test')
topic = 'owntracks/phone/phone'
mqtt.Client.connected_flag = False
mqtt.Client.bad_connection_flag=False
buffer =  [(32,-72),(52,-72)]


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
    

client.on_connect = on_connect
client.on_log = on_log
client.on_message = on_message
client.on_disconnect=on_disconnect
##########################################
print ('connecting to {}'.format(broker))

try:
    client.connect(broker,port)
except:
    print('error connecting')
########################################

client.loop_start()
while(not client.connected_flag and not client.bad_connection_flag):
    print ('waiting for connection')
    time.sleep(1)

client.subscribe(topic)
time.sleep(50)
client.loop_stop()


client.disconnect()

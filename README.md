# nissan-repo

## Run 3 servers: syncmanger, sokcettestserver, message in given order
## used Owntracks and MQTT cloud broker to recieve locations

update1:
working on connecting Owntracks with mqtt

update2:
connected mqtt broker with owntracks
working on message API in python which can connect to broker

update3:
message API is connected with broker, and recieving location info from Owntracks
issue with reconnecting, fixing that

update4:
message API done. working smoothly to collect location every time it is updated.

update5:
learning about Flask.

update6:
built a trial Flask app. running smoothly

update7:
learning react and html integration
integrated react comp in html page. running smoothly.


update 8:
working on integrating mapbox with my react component.
passing manual loc in the mapbox.

update9:
adding a pointer image on map.
webpage now loads the map through react and points the level

update10:
learning how to auto update webpage if location is changed in flask (through sockets)

update11:
found a way of sharing location (hopefully) through xmlrpc. client side is failing. sorting it out.

update12:
added JS code to continuously request loaction update from Web client.
Sockets are used

update13:
XMLRPC was failing for client side on message.py
Implementing backup method- pickling files

update14:
pickling was not happening at run-time
Trying 'memcache' now

update15:
Previous method also failed for syncronising.
Moving to Multi-processing managers.

update16:
Multiprocessing managers working well. 
All components now working fully

update17:
adding comments

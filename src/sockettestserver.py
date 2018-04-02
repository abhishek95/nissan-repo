'''
main flask server for hosting app
'''
from flask import Flask, render_template
from flask_socketio import SocketIO, emit,send
from multiprocessing.managers import SyncManager
import logging


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
####################################################################
'''
Code to syncronise incoming location from MQTT client
'''
class MyManager(SyncManager):
    pass

MyManager.register("syncdict")


manager = MyManager(("127.0.0.1", 8000), authkey="password")
manager.connect()
syncdict = manager.syncdict()
###########################################################################

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

values = {
    'lat': 25,
    'lon': 0,
}

@app.route('/')
def index():
    logger.info('Serving root')
    return render_template('sockettestclient.html', **values)

#socket connection from Web client
@socketio.on('client_connected')
def handle_client_connect_event(json):
    logger.info('responding to request')
    print('received json: {0}'.format(str(json)))

@socketio.on('value changed')
def value_changed(message):
    try:
        values['lat'] = syncdict.get('lat')
        values['lon'] = syncdict.get('lon')
        #line = fp.readline()[:-1].split(",")
        #values['lat'] =line[0]
        #values['lon'] =line[1]
        print (values)  
    except:
        print ('no update')
        
    update_message = values
    emit('update value', update_message, broadcast=True)
        
#run app
if __name__ == '__main__':
    logger.info('Running socket IO')
    socketio.run(app, host='localhost')
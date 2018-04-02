
from flask import Flask, render_template
from flask_socketio import SocketIO, emit,send
import pickle
import logging



logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

#fp = open("shared.pkl",'rb')
fp = open("sample_loc.txt",'r')

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

@socketio.on('client_connected')
def handle_client_connect_event(json):
    logger.info('responding to request')
    print('received json: {0}'.format(str(json)))

@socketio.on('value changed')
def value_changed(message):
    try:
        #shared = pickle.load(fp)
        #values['lat'] = shared['lat']
        #values['lon'] = shared['lon']
        line = fp.readline()[:-1].split(",")
        values['lat'] =line[0]
        values['lon'] =line[1]
        print (values)
        
    except:
        print ('no update')
        
    update_message = values
    emit('update value', update_message, broadcast=True)
        

if __name__ == '__main__':
    logger.info('Running socket IO')
    socketio.run(app, host='localhost')
from flask import Flask, render_template, jsonify
import time
import pickle
from flask.ext.socketio import SocketIO, emit

fp = open("shared.pkl",'rb')


values = {
    'lat': 23,
    'lon': -72,
}

#################################################################################


###################################################################################

app = Flask(__name__)
socketio = SocketIO(app)


@app.route("/loc/")
def index():
    #return jsonify(lat=lat,lon=lon)
    return render_template("webpage.html",**values)

@socketio.on('value changed')
def value_changed(message):
    try:
        shared = pickle.load(fp)
        values['lat'] = shared['lat']
        values['lon'] = shared['lon']
        print (values)
    except:
        print ('no update')
    emit('update value', message, broadcast=True)
    
    

if __name__=="__main__":
        socketio.run(app,host='127.0.0.1')
        
        
        
        
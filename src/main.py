from flask import Flask, render_template, jsonify
import time
import pickle

fp = open("shared.pkl",'rb')



lat,lon = 23,-72
#################################################################################


###################################################################################

app = Flask(__name__)

@app.route("/loc/",methods=['GET'])
def index():
    try:
        shared = pickle.load(fp)
        lat = shared['lat']
        lon = shared['lon']
        print (lat,lon)
    except:
        print ('no update')
    time.sleep(1)
    return jsonify(lat=lat,lon=lon)
    #return render_template("webpage.html",lat=lat,lon=lon)
    

if __name__=="__main__":
        app.run()
        
        
        
        
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/loc/")
def index():
    return render_template("webpage.html",lat=lat,lon=lon)
    
lat=42
lon =-72

if __name__=="__main__":
        app.run()
        
        
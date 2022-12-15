from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient(port=27017)
db = client["Sender"]

# route to get data from html form and insert data into database
@app.route('/sender', methods=["GET", "POST"])
def home_page():
    data = {}
    if request.method == "GET":
        return render_template("sender.html")
    if request.method == "POST":
        data['name'] = request.form['name'] 
        data['weight'] = request.form['pweight'] 
        data['Items'] = request.form['pitems'] 

        data['plat']  = translate_address(request.form['paddress'])[0]
        data['plong'] = translate_address(request.form['paddress'])[1]
        data['dlat'] = translate_address(request.form['daddress'])[0]
        data['dlong'] = translate_address(request.form['daddress'])[1]
        
        db.searchData.insert_one(data)
  
    return render_template("sender_confirm.html")

from geopy.geocoders import Nominatim
def translate_address(location):
    print(location)
    geolocator = Nominatim(user_agent="app")
    location = geolocator.geocode(location)
    return (location.latitude, location.longitude)

if __name__ == '__main__':
    app.run(debug=True)
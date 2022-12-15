from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient(port=27017)
db = client["TruckDriver"]


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

# route to get data from html form and insert data into database
@app.route('/start', methods=["GET", "POST"])
def start_page():
    data = {}
    if request.method == "GET":
        return render_template("start.html")
    if request.method == "POST":
        data['hlat']  = translate_address(request.form['haddress'])[0]
        data['hlong'] = translate_address(request.form['haddress'])[1]
        data['dlat'] = translate_address(request.form['daddress'])[0]
        data['dlong'] = translate_address(request.form['daddress'])[1]
        data['truckMaker'] = request.form['truckMaker']
        data['truckModel'] = request.form['truckModel']  
        data['weight'] = int(request.form['truckWeight'])
        print(data['weight'])
        db.searchData.insert_one(data)
    return render_template("search.html", data=[data['hlat'], data['hlong'],data['dlat'],data['dlong'],data['weight']])


from geopy.geocoders import Nominatim
def translate_address(location):
    print(location)
    geolocator = Nominatim(user_agent="app")
    location = geolocator.geocode(location)
    return (location.latitude, location.longitude)

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask,render_template,request
import folium
from twitter_api import twitter2
import json
from geopy import Nominatim
import time
import shutil

def geocoding(location):
    """
    Geocodes location to coordinates
    """
    geocoder = Nominatim(user_agent='Programming project')
    time.sleep(1)
    loc = geocoder.geocode(location)
    return loc.latitude,loc.longitude

site = Flask(__name__)

@site.route('/',methods=['GET'])
def base():
    request.form['name']
    print(username)
    return render_template('base.html')
@site.route('/map')
def drawmap():
    data = twitter2.get_data(username)
    location_list = []
    info = json.loads(data)
    for el in info['users']:
        if el['location'] == '':
            continue
        location_list.append((el['name'],geocoding(el['location'])))
    map = folium.Map(location_list[0][1])
    for el in location_list:
        folium.Marker(el[1],el[0]).add_to(map)
    map.save('friendmap.html')
    shutil.move('friendmap.html','templates/friendmap.html')
    return render_template('friendmap.html')

if __name__=='__main__':
    username = []
    site.run(debug=True)


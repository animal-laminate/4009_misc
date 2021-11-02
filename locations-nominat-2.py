import sqlite3 as sql
import math, os
from geopy.geocoders import Nominatim
import time

geolocator = Nominatim(user_agent="aa1910@coventry.ac.uk")

DB = 'locations-tst.db'   

def get_addresses(geolocator):
    locations = get_locations()
    for i in range (len(locations)):	
        loc = geolocator.reverse(str(locations[i][0])+','+str(locations[i][1]))
        print (loc.address)
        time.sleep(1.0)
          
def get_locations():
    locations = []
    latitudes = get_latitudes()
    longitudes = get_longitudes()
    for i in range(len(latitudes)):
        locations.append([latitudes[i],longitudes[i]])  #make list of lists to enable jinja render as columns  
    return locations
   
def get_latitudes():
    latitudes = []
    with sql.connect(DB) as cur:
        results = cur.execute('''SELECT latitude FROM Location;''')
        for latitude, in results:
            latitudes.append(str(latitude))
    return latitudes

def get_longitudes():
    longitudes = []
    with sql.connect(DB) as cur:
        results = cur.execute('''SELECT longitude FROM Location;''')
        for longitude, in results:
            longitudes.append(str(longitude))
    return longitudes
    
get_addresses(geolocator)



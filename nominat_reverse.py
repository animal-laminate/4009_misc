#from geopy.geocoders import Nominatim
#from geopy.exc import GeocoderTimedOut
'''
from geopy.geocoders import Nominatim
longlat = [[52.407996],[-1.503806]]
varlola1 = str(longlat[0][0])
varlola2 = ","
varlola3 = str(longlat[1][0])
varlola = varlola1+varlola2+varlola3
print(varlola)
geolocator = Nominatim(user_agent="aa1910@coventry.ac.uk")
location = geolocator.reverse(varlola)
print(location.address)
'''
import time

from geopy.geocoders import Nominatim
longlat = [[[52.407996],[-1.503806]],[[52.6],[-1.49]]]
for i in range(len(longlat)):
    varlo = str(longlat[i][0][0])+","+str(longlat[i][1][0])
    print(varlo)
    geolocator = Nominatim(user_agent="aa1910@coventry.ac.uk")
    location = geolocator.reverse(varlo)
    print(location.address)
    time.sleep(1)
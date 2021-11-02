import cherrypy
import jinja2
import sqlite3 as sql
import math, os
import time

JINJA_ENVIRONMENT = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__),'templates')),extensions=['jinja2.ext.autoescape'])

DB = 'locations-tst.db'   

class LocationsWebsite(object):
    @cherrypy.expose
    @cherrypy.tools.gzip()
    def index(self):
        template = JINJA_ENVIRONMENT.get_template('points-and-lines.html')
        template_values = {
			'locations': self.get_locations()} #template_values is a dict. key is 'locations', values is a list of lists of two items (long, lat)
        return template.render(template_values) #make and serve the webpage
    

            
    def get_locations(self):
        locations = []
        latitudes = self.get_latitudes()
        longitudes = self.get_longitudes()
        timestamps = self.get_report_times()
        dates = self.get_dates()
        times = self.get_times()
        for i in range(len(latitudes)):
            locations.append([latitudes[i],longitudes[i],timestamps[i], dates[i], times[i]])  #make list of lists to enable jinja render as columns  
        return locations
   
    def get_latitudes(self):
        latitudes = []
        with sql.connect(DB) as cur:
            results = cur.execute('''SELECT latitude FROM Location;''')
            for latitude, in results:
                latitudes.append(str(latitude))
        return latitudes

    def get_longitudes(self):
        longitudes = []
        with sql.connect(DB) as cur:
            results = cur.execute('''SELECT longitude FROM Location;''')
            for longitude, in results:
                longitudes.append(str(longitude))
        return longitudes
    
    def get_report_times(self):
        timestamps = []
        with sql.connect(DB) as cur:
            results = cur.execute('''SELECT timestamp FROM Location;''')
            for timestamp, in results:
                readabletime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timestamp))
                timestamps.append(str(readabletime))
        return timestamps

    def get_dates(self):
        dates = []
        with sql.connect(DB) as cur:
            results = cur.execute('''SELECT date FROM Location;''')
            for date, in results:
                dates.append(str(date))
        return dates
    
    def get_times(self):
        times = []
        with sql.connect(DB) as cur:
            results = cur.execute('''SELECT time FROM Location;''')
            for time, in results:
                times.append(str(time))
        return times

class LocationsWebsite2(object):
    @cherrypy.expose
    @cherrypy.tools.gzip()
    def index(self):
        template = JINJA_ENVIRONMENT.get_template('points-and-lines.html')
        template_values = {
			'locations': self.get_locations()} #template_values is a dict. key is 'locations', values is a list of lists of two items (long, lat)
        return template.render(template_values) #make and serve the webpage
    

            
    def get_locations(self):
        locations = []
        latitudes = self.get_latitudes()
        longitudes = self.get_longitudes()
        timestamps = self.get_report_times()
        dates = self.get_dates()
        times = self.get_times()
        for i in range(len(latitudes)):
            locations.append([latitudes[i],longitudes[i],timestamps[i], dates[i], times[i]])  #make list of lists to enable jinja render as columns  
        return locations
   
    def get_latitudes(self):
        latitudes = []
        with sql.connect(DB) as cur:
            results = cur.execute('''SELECT latitude FROM Location;''')
            for latitude, in results:
                latitudes.append(str(latitude))
        return latitudes

    def get_longitudes(self):
        longitudes = []
        with sql.connect(DB) as cur:
            results = cur.execute('''SELECT longitude FROM Location;''')
            for longitude, in results:
                longitudes.append(str(longitude))
        return longitudes
    
    def get_report_times(self):
        timestamps = []
        with sql.connect(DB) as cur:
            results = cur.execute('''SELECT timestamp FROM Location;''')
            for timestamp, in results:
                readabletime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timestamp))
                timestamps.append(str(readabletime))
        return timestamps

    def get_dates(self):
        dates = []
        with sql.connect(DB) as cur:
            results = cur.execute('''SELECT date FROM Location;''')
            for date, in results:
                dates.append(str(date))
        return dates
    
    def get_times(self):
        times = []
        with sql.connect(DB) as cur:
            results = cur.execute('''SELECT time FROM Location;''')
            for time, in results:
                times.append(str(time))
        return times

if __name__ == '__main__':
    cherrypy.config.update({'server.socket_host': '0.0.0.0'})
    cherrypy.config.update({'server.socket_port': 3000})
    #cherrypy.quickstart(LocationsWebsite(), '/', {'/': {'tools.gzip.on': True}})
    cherrypy.quickstart(LocationsWebsite2(), '/', {'/': {'tools.gzip.on': True}})

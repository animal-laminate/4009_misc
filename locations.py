import cherrypy
import sqlite3 as sql

DB = 'locations.db'   

class LocationsWebsite(object):
    @cherrypy.expose
    @cherrypy.tools.gzip()
    def index(self):
        longitudes = []
        with sql.connect(DB) as cur:
            results = cur.execute('''SELECT DISTINCT longitude FROM Location;''')
            for longitude, in results:
                longitudes.append(str(longitude))
        print(longitudes)
        return longitudes

if __name__ == '__main__':
    cherrypy.config.update({'server.socket_host': '0.0.0.0'})
    cherrypy.config.update({'server.socket_port': 3000})
    cherrypy.quickstart(LocationsWebsite(), '/', {'/': {'tools.gzip.on': True}})

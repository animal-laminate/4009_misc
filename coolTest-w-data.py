from flask import Flask, request, url_for, redirect, render_template
import jinja2
import sqlite3 as sql
import math, os
import time

app = Flask(__name__)

JINJA_ENVIRONMENT = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__),'templates')),extensions=['jinja2.ext.autoescape'])

DB = 'locations-tst.db'   

@app.route('/')
def index():
    locations = {get_locations()} 
    #print(template_values)

    return render_template('index.html',locations=locations)

@app.route('/cool_form', methods=['GET', 'POST'])
def cool_form():
    if request.method == 'POST':
        # do stuff when the form is submitted
        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('index'))

    # show the form, it wasn't submitted
    return render_template('cool_form.html')

def get_locations():
        locations = []
        latitudes = get_latitudes()
        longitudes = get_longitudes()
        timestamps = get_report_times()
        dates = get_dates()
        times = get_times()
        for i in range(len(latitudes)):
            locations.append([latitudes[i],longitudes[i],timestamps[i], dates[i], times[i]])  #make list of lists to enable jinja render as columns  
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
    
def get_report_times():
        timestamps = []
        with sql.connect(DB) as cur:
            results = cur.execute('''SELECT timestamp FROM Location;''')
            for timestamp, in results:
                readabletime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timestamp))
                timestamps.append(str(readabletime))
        return timestamps

def get_dates():
        dates = []
        with sql.connect(DB) as cur:
            results = cur.execute('''SELECT date FROM Location;''')
            for date, in results:
                dates.append(str(date))
        return dates
    
def get_times():
        times = []
        with sql.connect(DB) as cur:
            results = cur.execute('''SELECT time FROM Location;''')
            for time, in results:
                times.append(str(time))
        return times



if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 3000)
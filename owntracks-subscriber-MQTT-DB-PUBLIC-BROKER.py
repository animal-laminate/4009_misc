""" connect to MQTT and write owntracks data to a database """

import paho.mqtt.client as mqtt                                         #necessary imports
import sqlite3 as sql
import json, os
from datetime import date, datetime
import time

""" callback function for connection """    
def on_connect(client, userdata, flags, rc):                            #client method to connect
    if rc == 0:
        client.connected_flag = True                                    #set flag
        print("connected OK")                                           #let us know we connected to the broker
        client.subscribe("owntracks/4009user/#")                        #my topic is 4009teacher. Yours will be different - see owntracks public broker setup
    else:
        print("Bad connection. Returned code = ", rc)                   #if we can't connect

""" callback function for messages received """
def on_message( client, userdata, msg ):                                #client method to get messages from topic
    con = sql.connect('locations-with-tid.db')                          #name of the database. You might want to change it. 
    cur = con.cursor()
    try:                                                                #the example here gets the tid; so we need 5 fields
        cur.execute("CREATE TABLE Location(tid VARCHAR2(4), longitude NUMBER(10,6), latitude NUMBER(10,6), date VARCHAR2(20), time VARCHAR2(20));") 
    except:
        pass                                                            #if it already exists
    data = json.loads(msg.payload.decode("utf8"))                       #decode message
    day = date.today()                                                  #time functions
    clock = datetime.now()
    time = datetime.time(clock)
    cur.execute("INSERT INTO Location values(?,?,?,?,?);", (data["tid"], data["lon"], data["lat"], str(day), str(time)))
                                                                        #puts the tid, latitude, longitude from the posted message as well as the date and time when it was posted into the database
    print ("TID = {0} is currently at {1}, {2},{3},{4}".format(data['tid'], data['lat'], data['lon'], str(day), str(time)))
                                                                        #print tid, latitude and longitude from the message; add time data (same as db)
    print(str(data))                                                    #print the entire message just for fun
    con.commit()
    cur.close()
    con.close()                                                         #close the database


client = mqtt.Client("Client-001" )                                     
client.on_connect = on_connect
client.on_message = on_message
client.connect( "broker.hivemq.com" )                                   #connect to the broker. no authentication or certificate needed
client.loop_forever()                                                   #keep looping forever - allows realtime subscription

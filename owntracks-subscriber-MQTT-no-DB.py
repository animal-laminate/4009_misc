import paho.mqtt.client as mqtt                                         #necessary imports
import json, os
from datetime import date, datetime
import time

""" callback function for connection """    
def on_connect(client, userdata, flags, rc):                            #client method to connect
    if rc == 0:
        client.connected_flag = True                                    #set flag
        print("connected OK")                                           #let us know we connected to the broker
        client.subscribe("owntracks/4009user/#")                        #we are connected, so subscribe to the topic. wildcard means any device
    else:
        print("Bad connection. Returned code = ", rc)                   #if we can't connect

""" callback function for messages received """
def on_message( client, userdata, msg ):                                #client method to get messages from topic         
    topic = msg.topic                                                   #for use when we can't decode
    try:
        data = json.loads(msg.payload.decode("utf8"))                   #decode message
        day = date.today()                                              #time functions
        clock = datetime.now()
        time = datetime.time(clock)
        print ("TID = {0} is currently at {1}, {2},{3},{4}".format(data['tid'], data['lat'], data['lon'], str(day), str(time)))
                                                                        #print device, latitude and longitude from the message; add time data
        print(str(data))                                                #print the entire message just for fun
    except:
        print ("Cannot decode data on topic {0}".format(topic))         #cannot decode; print the topic for the non-decodable message

client = mqtt.Client()                                                  #bind all functions to mqtt class
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set("4009user", "mqttBROKER")                        #associate authentication details with the client
client.tls_set("mqtt.coventry.ac.uk.crt")                               #certificate for client. needs to be in the same directory as this script
client.connect("mqtt.coventry.ac.uk", 8883)                             #connect to the broker on an appropriate port
client.loop_forever()                                                   #keep looping forever (allows realtime subscription)

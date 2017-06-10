#!/usr/bin/python

import sys
import time
import http.client
import urllib
import re
import serial


def upload(temperature, humidity, light_value):
        params = urllib.urlencode({'field1': temperature, 'field2': humidity, 'field3': UV_value, 'key':'JG4TQO6QP1ALOVFY'})
        
        headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
        conn = httplib.HTTPConnection("api.thingspeak.com:80")
        conn.request("POST", "/update", params, headers)
        response = conn.getresponse()
        print (response.status, response.reason)
        data = response.read()
        conn.close()

def WriteFile(current_weather):
    fp = open("data.txt", 'a')
    fp.write(current_weather)    
    fp.close()
    
def GetAnalogIndex():
    #Open Serial Port To Arduino nano
    ser = serial.Serial('COM7', 9600, timeout=1)
    ser.isOpen()
    
    try:
        while True:
        #print 'RPi is sending request to arduino'
            print ('connecting to MCU...')
            ser.write(to_bytes('L'))
            response1 = ser.readline()
            #ser.write('U')
            #response2 = ser.readline()
            ser.write('H')
            response2 = float(ser.readline())
            ser.write('T')
            response3 = float(ser.readline())
            #ser.write('D')
            #response5 = ser.readline()
            #print(request) #debug only
            #print (response1) #debug only
            #print (response2) #debug only
            if response1 and response2 and response3 != '':
                break
            
    except KeyboardInterrupt:
        ser.close()
    return response1,response2,response3



#while True:
light_value, humidity, temperature = GetAnalogIndex()
light_value=1023-int(light_value,10)
    
    #if humidity is not None and temperature is not None:
current_weather=time.strftime("%Y/%m/%d %H:%M:%S ")+'Temp={0:0.1f}* Humidity={1:0.1f}% light_value={2:0.1f}'.format(temperature, humidity, light_value)
print(current_weather)
#	print(UV_value)
WriteFile(current_weather+'\n')
upload(temperature, humidity, light_value)
    #time.sleep(52)

    #else:
    #	print('Failed to get reading. Try again!')
    #	sys.exit(1)
 

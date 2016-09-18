from __future__ import print_function
import sys
import os
import pylab as pl
import json
import urllib.request as ulr
import pylab
import requests

if __name__ == '__main__':
        # key = 'cf4e7f89-cb4b-43be-ab66-1888e24b7dd1'                                  
        # busname = 'B52'  
        key = sys.argv[1]
        LineRef = sys.argv[2]
        url = 'http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s' % (sys.argv[1],sys.argv[2]) 
        
        response = ulr.urlopen(url)
        data = response.read().decode("utf-8")
        data = json.loads(data) 
        
        Busdata = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
        Buscount = len(data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'])
        print "Bus Line : %s" % (sys.argv[2])
        print "Number of Active Buses : %d" % (Buscount)
        for i in range(Buscount):
            latitude = Busdata[i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
            longitude = Busdata[i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
            print "Bus %d is at latitude %f and longitude %f" % (i, latitude, longitude)

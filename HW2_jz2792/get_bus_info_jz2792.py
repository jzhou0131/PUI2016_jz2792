from __future__ import print_function
import os
import sys
import json
import pandas as pd
import urllib2

if __name__ == '__main__':
    # key = 'cf4e7f89-cb4b-43be-ab66-1888e24b7dd1'                                  
    # busname = 'B52' 
    key = sys.argv[1]
    LineRef = sys.argv[2]
    url = 'http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s' % (sys.argv[1],sys.argv[2]) 

    response = urllib2.urlopen(url)
    data = response.read().decode("utf-8")
    data = json.loads(data)

    Busdata = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
    Buscount = len(data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'])
    
    #Initialize Columns
    Latitude = []
    Longitude = []
    Stop_name = []
    Stop_status = []
    
    
    # Retrieve bus info
    for i in range (Buscount):
        lati = Busdata[i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
        longi = Busdata[i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
        stopname = Busdata[i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName']
        stopstatus = Busdata[i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance']
        
        #Append to columns
        Latitude.append(lati)
        Longitude.append(longi)
        if Busdata[i]['MonitoredVehicleJourney']['OnwardCalls'] == {}:
            Stop_name.append('N/A')
            Stop_status.append('N/A')
        else:
            Stop_name.append(stopname)
            Stop_status.append(stopstatus)
    
    bus_info = pd.DataFrame({'Latitude':Latitude,'Longitude':Longitude,'Stop_name':Stop_name,'Stop_status':Stop_status})
    filename = sys.argv [3]
    bus_info.to_csv(filename,index=False)

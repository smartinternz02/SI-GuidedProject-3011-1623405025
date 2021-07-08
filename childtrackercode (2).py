import json
import wiotp.sdk.device
import time

myConfig = {
    "identity": {
        "orgId": "x62vx4",
        "typeId": "data",
        "deviceId": "1001"},
    "auth": {"token": "1234567890"}
}
client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
client.connect()

while True:
        name= "Srikanth"
        #in area location

        #latitude= 17.4225176
        #longitude= 78.5458842

        #out area location

        latitude= 17.4219272
        longitude= 78.5488783
        mydata={'name':name, 'lat':latitude,'lon':longitude}
        client.publishEvent(eventId="status", msgFormat="json", data=mydata, qos=0, onPublish=None)
        print("Dta published to IBM IoT platform: ",mydata)
        time.sleep(5)

client.disconnect()

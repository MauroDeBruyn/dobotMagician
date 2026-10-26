# Enable color Sensor
dType.SetColorSensor(api, 1, 1, version=1) 
# Parameters: 
# Api: api
# isEnable: 0=disable ; 1=enable
# colorPort: Plug your sensor in GP2. Fill in the corrensponding number here, wich is 2.
# Version: version = 0 (Version 1 of sensor) ; version = 1 (Version 2 of sensor), we will use this one.

while True:
    RGB_value = dType.GetColorSensor(api)
    print("Sensor output: {}".format(RGB_value))
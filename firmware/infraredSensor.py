# Enable IR Sensor
dType.SetInfraredSensor(api, 1, 2, version=1) 
# Parameters: 
# Api: api
# isEnable: 0=disable ; 1=enable
# InfraredPort: Plug your sensor in GP4. Fill in the corrensponding number here, wich is 2.
# Version: version = 0 (Version 1 of sensor) ; version = 1 (Version 2 of sensor), we will use this one.

while True:
    ir_value = dType.GetInfraredSensor(api, 2)
    print("Sensor output: {}".format(ir_value))
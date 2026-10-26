#Run Conveyor
import time

print("Start Conveyor")

dType.SetEMotor(api, 0, 1, 2000, 0) #Speed value: 2000 - 20000

time.sleep(5000)

print("Conveyor stoppen")

dType.SetEMotor(api, 0, 0, 0, 0)




#Color sens getting rgb vlue
import time
dType.SetColorSensor(api, 1, 1, 1)

while True:
    kleur = dType.GetColorSensor(api)
    print(kleur)
    time.sleep(0.2)

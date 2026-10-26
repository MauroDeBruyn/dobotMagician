#Run Conveyor

print("Start Conveyor")
dType.SetEMotor(api, 0, 1, 2000, 0) #Speed value: 2000 - 20000
# Parameters
# Api: api
# index: Motoroutput, 0 = Stepper1, 1 = Stepper2
# isEnabled: 0=disable ; 1=enable
# speed: Speed in pulses per second, NOT RPM
# isQueued: 0 = execute immediately; 1 = add to the command queue. The default is 0


dType.SetWAITCmd(api, 1000, isQueued=0)
# Parameters
# waitTime: Delay in ms
# isQueued: 0 = execute immediately; 1 = add to the command queue. The default is 0

print("Conveyor stoppen")

dType.SetEMotor(api, 0, 1, 0, 0)

# ---------------- Enable Sensors ----------------
# Enable IR Sensor
dType.SetInfraredSensor(api, 1, 2, version=1) 

# Enable color Sensor
dType.SetColorSensor(api, 1, 1, version=1) 



# ---------------- Hoofdprogramma ----------------
m = int('0')

#Run Conveyor

print("Start Conveyor")
dType.SetEMotor(api, 0, 1, 10000, 0) #Speed value: 2000 - 20000


while True:
	dType.SetEMotor(api, 0, 1, 10000, 0) #Speed value: 2000 - 20000
	# Read IR Sensor data and print in terminal
	ir_value = dType.GetInfraredSensor(api, 2)[0] # Sensor output returns a list, use [0] to remove the unnecessary data from the list
	m = 1

	# If IR sensor reads an object
	if ir_value == 1 and m == 1: 

		# Stop conveyor
		dType.SetEMotor(api, 0, 1, 0, 0)

		# Move arm above the object.
		dType.SetPTPCmd(api, 2, 67, 221.5, 100, 0, 1)

		# Pick up object.
		dType.SetPTPCmd(api, 2, 67, 221.5, 9.5, 0, 1)

		# Zuignap aan
		dType.SetEndEffectorSuctionCup(api, 1, 1, 1)
		dType.SetWAITCmd(api, 1000, isQueued=0)
		# Pick up
		dType.SetPTPCmd(api, 2, 67, 221.5, 100, 0, 1)

		# Move to color sensor
		dType.SetPTPCmd(api, 2, 156.5, 141.3, 100, 0, 1)
		dType.SetPTPCmd(api, 2, 156.5, 141.3, 34.7, 0, 1)

		dType.SetWAITCmd(api, 1000, isQueued=0)

		RGB_value = dType.GetColorSensor(api)
		# print("sensor output: {}".format(RGB_value))
		dType.SetWAITCmd(api, 1000, isQueued=0)

		if RGB_value == [0, 0, 1]:
			print("BLAUW gedetecteerd")
			dType.SetPTPCmd(api, 2, 234, -75, 60, 0, 1)
			dType.SetEndEffectorSuctionCup(api, 1, 0, 1)
			dType.SetPTPCmd(api, 2, 234, -75, -43, 0, 1)

		elif RGB_value == [1, 0, 0]:
			print("RED gedetecteerd")
			dType.SetPTPCmd(api, 2, 250, 0, 60, 0, 1)
			dType.SetPTPCmd(api, 2, 250, 0, -43, 0, 1)
			dType.SetEndEffectorSuctionCup(api, 1, 0, 1)

		elif RGB_value == [0, 1, 0]:
			print("GREEN gedetecteerd")
			dType.SetPTPCmd(api, 2, 178, -170, 60, 0, 1)
			dType.SetPTPCmd(api, 2, 178, -170, -43, 0, 1)
			dType.SetEndEffectorSuctionCup(api, 0, 0, 1)
			dType.SetPTPCmd(api, 2, 227, 16, 46, 0, 1)

		else:
			print("Geen bruikbare kleur gedetecteerd")
			dType.SetPTPCmd(api, 2, 250, 0, 40, 0, 1)
			dType.SetEndEffectorSuctionCup(api, 1, 0, 1)
		
		dType.SetPTPCmd(api, 2, 156.5, 141.3, 100, 0, 1)
		print("Wachten op laatste robotbeweging")
		m = 0

	else:
		print("do nothing")
		dType.SetQueuedCmdClear(api)
		m = 0
		
	




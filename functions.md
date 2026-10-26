<h1 align="center">
  <a href="#"> Dobot Studio Functions </a>
</h1>


<p align="center">
 <a href="#other">Other</a> •
 <a href="#pose">Pose</a> • 
 <a href="#home">HOME</a> • 
 <a href="#endeffector">EndEffector</a> •  
 <a href="#loststep">LostStep</a> • 
 <a href="#jog">JOG</a> • 
 <a href="#ptp">PTP</a> • 
 <a href="#arc">ARC</a> • 
 <a href="#wait">WAIT</a> •
 <a href="#eio">EIO</a> •
 <a href="#sensors">Sensors</a> •
 <a href="#linearrail">LinearRail</a>
</p>

---


### Other <a name="other"></a>
---

```pyton
dType.dSleep(ms)
```
**Description:**
This funtion is used to delay

**Params:**
- `ms` - miliseconds

**Returns:**
None

---


```python
dType.SetCmdTimeout(api, times)
```
**Description:**

**Params:**
- none

**Returns:**

---


```python
dType.DobotExec(api)
```
**Description:**

**Params:**
- none

**Returns:**

---

### Pose <a name="pose"></a>
---

```python
dType.GetPose(api)
```
**Description:**
Get current pose of Dobot

**Params:**
- api: The object of Dobot Library

**Returns:**
- list[0]: The value of x-axis.
- list[1]: The value of y-axis.
- list[2]: The value of z-axis.
- list[3]: The value of r-axis.
- list[4]: The value of joint1.
- list[5]: The value of joint2.
- list[6]: The value of joint3.
- list[7]: The value of joint4.

---
### HOME <a name="home"></a>
---

```bash
dType.SetHOMEParams(api,  x,  y,  z,  r,  isQueued=0)
```
**Description:**

**Params:**
- none

**Returns:**

---


```bash
dType.GetHOMEParams(api)
```
**Description:**

**Params:**
- none

**Returns:**

---


```bash
dType.SetHOMECmd(api, temp, isQueued=0)
```
**Description:**

**Params:**
- none

**Returns:**

---

### EndEffector <a name="endeffector"></a>
---

```bash
dType.SetEndEffectorParams(api, xBias, yBias, zBias, isQueued=0)
```
**Description:**

**Params:**
- none

**Returns:**

---


```bash
dType.GetEndEffectorParams(api)
```
**Description:**

**Params:**
- none

**Returns:**

---


```bash
dType.SetEndEffectorLaser(api, enableCtrl,  on, isQueued=0)
```
**Description:**

**Params:**
- none

**Returns:**

---


```bash
dType.GetEndEffectorLaser(api)
```
**Description:**

**Params:**
- none

**Returns:**

---


```bash
dType.SetEndEffectorSuctionCup(api, enableCtrl,  on, isQueued=0)
```
**Description:**

**Params:**
- none

**Returns:**

---


```bash
dType.GetEndEffectorSuctionCup(api)
```
**Description:**

**Params:**
- none

**Returns:**

---


```bash
dType.SetEndEffectorGripper(api, enableCtrl,  on, isQueued=0)
```
**Description:**

**Params:**
- none

**Returns:**

---


```bash
dType.GetEndEffectorGripper(api)
```
**Description:**

**Params:**
- none

**Returns:**

---



---
### LostStep <a name="loststep"></a>
---

```bash
dType.SetLostStepParams(api, threshold)
```
**Description:**

**Params:**
- none

**Returns:**

---


```bash
dType.SetLostStepCmd(api, isQueued=0)
```
**Description:**

**Params:**
- none

**Returns:**




---
### JOG <a name="jog"></a>
---

```bash
dType.SetJOGJointParams(api, j1Velocity, j1Acceleration, j2Velocity, j2Acceleration, j3Velocity, j3Acceleration, j4Velocity, j4Acceleration, isQueued=0)
```
**Description:**

**Params:**
- none

**Returns:**

---


```bash
dType.GetJOGJointParams(api)
```
**Description:**

**Params:**
- none

**Returns:**

---


```bash
dType.SetJOGCoordinateParams(api, xVelocity, xAcceleration, yVelocity, yAcceleration, zVelocity, zAcceleration, rVelocity, rAcceleration, isQueued=0)
```
**Description:**

**Params:**
- none

**Returns:**

---


```bash
dType.GetJOGCoordinateParams(api)
```
**Description:**

**Params:**
- none

**Returns:**

---


```bash
dType.SetJOGCommonParams(api, value_velocityratio, value_accelerationratio, isQueued=0)
```
**Description:**

**Params:**
- none

**Returns:**

---


```bash
dType.GetJOGCommonParams(api)
```
**Description:**

**Params:**
- none

**Returns:**

---


```bash
dType.SetJOGCmd(api, isJoint, cmd, isQueued=0)
```
**Description:**

**Params:**
- none

**Returns:**

---



---
### PTP <a name="ptp"></a>
---

```bash
dType.SetPTPJointParams(api, j1Velocity, j1Acceleration, j2Velocity, j2Acceleration, j3Velocity, j3Acceleration, j4Velocity, j4Acceleration, isQueued=0)
```
**Description:**

**Params:**
- none

**Returns:**

---


```bash
dType.GetPTPJointParams(api)
```
**Description:**

**Params:**
- none

**Returns:**

---


```bash
dType.SetPTPCoordinateParams(api, xyzVelocity, xyzAcceleration, rVelocity,  rAcceleration,  isQueued=0)
```
**Description:**

**Params:**
- none

**Returns:**

---


```bash
dType.GetPTPCoordinateParams(api)
```
**Description:**

**Params:**
- none

**Returns:**

---


```bash
dType.SetPTPJumpParams(api, jumpHeight, zLimit, isQueued=0)
```
**Description:**

**Params:**
- none

**Returns:**

---


```bash
dType.GetPTPJumpParams(api)
```
**Description:**

**Params:**
- none

**Returns:**

---


```bash
dType.SetPTPCommonParams(api, velocityRatio, accelerationRatio, isQueued=0)
```
**Description:**

**Params:**
- none

**Returns:**

---


```bash
dType.GetPTPCommonParams(api)
```
**Description:**

**Params:**
- none

**Returns:**

---


```bash
dType.SetPTPCmd(api, ptpMode, x, y, z, rHead, isQueued=0)
```
**Description:**

**Params:**
- none

**Returns:**

---



---
### ARC <a name="arc"></a>
---

```bash
dType.SetARCParams(api,  xyzVelocity, rVelocity, xyzAcceleration, rAcceleration,  isQueued=0)
```
**Description:**

**Params:**
- none

**Returns:**

---


```bash
dType.GetARCParams(api)
```
**Description:**

**Params:**
- none

**Returns:**

---


```bash
dType.SetARCCmd(api, cirPoint, toPoint,  isQueued=0)
```
**Description:**

**Params:**
- none

**Returns:**

---


```bash
dType.SetCircleCmd(api, cirPoint, toPoint, count, isQueued=0)
```
**Description:**

**Params:**
- none

**Returns:**

---



### WAIT <a name="wait"></a>
```bash
dType.SetWAITCmd(api, waitTime, isQueued=0)
```
**Description:**

**Params:**
- none

**Returns:**

---



---
### EIO <a name="eio"></a>
---

```bash
dType.SetIOMultiplexing(api, address, multiplex, isQueued=0)
```
**Description:**

**Params:**
- none

**Returns:**

---


```bash
dType.GetIOMultiplexing(api,  addr)
```
**Description:**

**Params:**
- none

**Returns:**

---


```bash
dType.SetIODO(api, address, level, isQueued=0)
```
**Description:**

**Params:**
- none

**Returns:**

---


```bash
dType.GetIODO(api, addr)
```
**Description:**

**Params:**
- none

**Returns:**

---


```bash
dType.SetIOPWM(api, address, frequency, dutyCycle,  isQueued=0)
```
**Description:**

**Params:**
- none

**Returns:**

---


```bash
dType.GetIOPWM(api, addr)
```
**Description:**

**Params:**
- none

**Returns:**

---


```bash
dType.GetIODI(api, addr)
```
**Description:**

**Params:**
- none

**Returns:**

---


```bash
dType.SetEMotor(api, index, isEnabled, speed,  isQueued=0)
```
**Description:**

**Params:**
- none

**Returns:**

---


```bash
dType.SetEMotorS(api, index, isEnabled, speed, distance, isQueued=0)
```
**Description:**

**Params:**
- none

**Returns:**

---

```bash
dType.GetIOADC(api, addr)
```
**Description:**

**Params:**
- none

**Returns:**




---
### Sensors <a name="sensors"></a>
---

```bash
dType.SetColorSensor(api, isEnable, colorPort, version=0)
```
**Description:**

**Params:**
- none

**Returns:**

---


```bash
dType.GetColorSensor(api)
```
**Description:**

**Params:**
- none

**Returns:**

---


```bash
dType.SetInfraredSensor(api,  isEnable, infraredPort, version=0)
```
**Description:**

**Params:**
- none

**Returns:**

---


```bash
dType.GetInfraredSensor(api, infraredPort)
```
**Description:**

**Params:**
- none

**Returns:**

---



---
### LinearRail <a name="linearrail"></a>
---

```bash
dType.SetDeviceWithL(api, isWithL, version)
```
**Description:**

**Params:**
- none

**Returns:**

---


```bash
dType.GetDeviceWithL(api)
```
**Description:**

**Params:**
- none

**Returns:**

---


```bash
dType.GetPoseL(api)
```
**Description:**

**Params:**
- none

**Returns:**

---


```bash
dType.SetJOGLParams(api, velocity, acceleration, isQueued=0)
```
**Description:**

**Params:**
- none

**Returns:**

---


```bash
dType.GetJOGLParams(api)
```
**Description:**

**Params:**
- none

**Returns:**

---


```bash
dType.SetPTPLParams(api, velocity, acceleration, isQueued=0)
```
**Description:**

**Params:**
- none

**Returns:**

---


```bash
dType.GetPTPLParams(api)
```
**Description:**

**Params:**
- none

**Returns:**

---


```bash
dType.SetPTPWithLCmd(api, ptpMode, x, y, z, rHead, l, isQueued=0)
```
**Description:**

**Params:**
- none

**Returns:**

---




import math


# Movement settings
dType.SetPTPJointParams(api, 200, 200, 200, 200, 200, 200, 200, 200, 0)
dType.SetPTPCoordinateParams(api, 200, 200, 200, 200, 0)
dType.SetPTPJumpParams(api, 10, 200, 0)
dType.SetPTPCommonParams(api, 100, 100, 0)

# Read current position
pos = dType.GetPose(api)
x = pos[0]
y = pos[1]
z = pos[2]
rHead = pos[3]

while(1):

    # Position 1
    dType.SetPTPCmd(api, 2, 150, 150, 30, rHead, 1)

    # Position 2
    dType.SetPTPCmd(api, 2, 180, 180, 60, rHead, 1)

    # Position 3
    dType.SetPTPCmd(api, 2, 180, -100, 60, rHead, 1)

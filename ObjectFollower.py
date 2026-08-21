from irobot_edu_sdk.backend.bluetooth import Bluetooth
from irobot_edu_sdk.robots import event, hand_over, Color, Robot, Root, Create3
from irobot_edu_sdk.music import Note

robot = Create3(Bluetooth()) # Put robot name here.

# --------------------------------------------------------
# Implement the first two functions so that the robot
# will stop and turn on a solid red light
# when any button or bumper is pressed.
# --------------------------------------------------------

# EITHER BUTTON
@event(robot.when_touched, [True, True])  # User buttons: [(.), (..)]
async def when_either_touched(robot):
    pass

# EITHER BUMPER
@event(robot.when_bumped, [True, True])  # [left, right]
async def when_either_bumped(robot):
    pass

# --------------------------------------------------------
# Implement followObject() so the robot:
#   - Uses IR proximity readings (4095 / (ir + 1))
#   - Responds to the CENTER sensor:
#         > 15.0 units ---> plate far
#         5.0–15.0 units ---> alignment zone
#         < 5.0 units ---> plate close
#   - In alignment zone, compare sensor 1 and sensor 5
#     (aligned if difference within + or - 25.0)
#   - Include a fail-safe (collision or button press ---> stop)
# --------------------------------------------------------

@event(robot.when_play)
async def followObject(robot):
    pass

# start the robot
robot.play()

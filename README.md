# CS1301-Robotics-Lab1

In the following files, I used the installable iRobot Education Python SDK library for robot-specific functions and the Python Bluetooth library to wirelessly connect to the iRobot Create 3.

Robots are increasingly common in warehouses and distribution centers, where they work alongside humans to improve efficiency. A typical scenario is item collection: robots follow workers as they pick merchandise from shelves and assemble orders. When operating in close proximity to people, it is also important for robots to provide clear feedback. Sounds and visual cues, such as lights, help signal the robot's state or intentions so nearby workers understand what it is about to do.

In CodeBreaker.py, I designed a system that allows users to input a predefined code sequence (password) via touch buttons and bumpers on the robot. The robot should be able to recognize button and bumper presses as input and check whether the inputted code matches the correct passcode. If the robot is successfully unlocked, a "happy" tune is played. If the inputted password is incorrect, a "sad" tune is played.

In ObjectFollower.py, I designed a system that uses the robot to simulate a worker-following task with a plate. The robot should track the plate using infrared (IR) proximity measurements and adjust its speed, lights, and sound feedback in response. Additionally, the robot should have various fail-safe event-driven mechanisms. Fail-safe mechanisms ensure the robot stops if it collides with an object, preventing it from enduring or causing damage.

In bumpers_and_buttons.py, I programmed the robot to perform simple tasks when either a bumper or a button is pressed such as rotating the robot, changing the robot's speed, playing notes and sounds, and changing the color of the robot's ring light.

In closestSensor.py, I collected and analyzed the data from the robot's 7 positioning sensors. Then, I used the data in this script to determine which color the robot's ring light should shine. If the robot senses the closest object to its left, the light should shine red. If the robot senses the closest object to its right, the light should shine green.

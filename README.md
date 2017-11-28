# Engine control unit for autonomous vehicle.

This repository contains the Throttle control unit of an IC engine using ROS. The system controller is built using ROS PID nodelet. The throttle control mechanism is also simulated using rviz.

## Hardware required:
1. An IC engine (Used here is a Four stroke engine of Hero Pleasure.
2. Throttle control mechanism. (To pull the throttle cable, The system I implemented is present in the repository for reference)
3. Rotary encoder (Feedback to control the position of throttle cable)
4. Hall effect sensor (For engine RPM feedback)
5. Raspberry pi (controller)

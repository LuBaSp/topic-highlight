# ⚠️ IMPORTANT ⚠️

👉 **Before you start**, go to the **`TUTORIAL_FOR_EXECUTION`** folder to see **how to build and set up the project**.  
It contains all the necessary instructions to run the system correctly.

---

# TIAGO SLAM and Tracking

## Overview

This project presents the development of an autonomous robotic mission divided into two main phases: **environment exploration** and **target tracking**. It has been implemented using the **TIAGO** robot in a simulated environment with **ROS2** and **Gazebo**. The system integrates sensor modeling, object recognition, SLAM, and autonomous navigation.

---

## Project Phases

### 1. Environment Exploration

The first phase focuses on autonomous mapping and navigation in an unknown environment using:

- **NAV2 (ROS2 Navigation Stack)** for path planning and localization.
- **M-Explore-ROS2**, a package for frontier-based exploration.
- **2D LiDAR (SICK TiM571)** for obstacle detection and mapping.
- **State Machine and Mission Manager** for structured task execution.

Algorithms used include **Frontier Point Exploration** and **RRT (Rapidly-exploring Random Tree)** for efficient space coverage.

### 2. Target Tracking

The second phase begins when the **RGB-D camera** detects a moving target (e.g., a vehicle). Key features:

- **YOLOv5** for object detection based on RGB-D input.
- **Proportional controller** for heading correction.
- Distance estimation from point clouds.
- Computation of new waypoints based on relative target position and orientation.

A series of ROS2 nodes manage image acquisition, object localization, heading control, and waypoint publishing.

---

## Hardware Simulation

- **LiDAR**: SICK TiM571-2050101, simulated for 2D obstacle sensing.
- **RGB-D Camera**: Orbbec Astra S, used for object detection and depth sensing.
- **Field of View and Sensor Modeling** were carefully configured for realistic simulation performance.

---

## Results and Analysis

- The robot successfully maps unknown environments using SLAM.
- Object detection and tracking were integrated with autonomous movement.
- ROSBAG and Foxglove were used to analyze:
  - Trajectory and velocity.
  - Mapping accuracy.
  - Tracking robustness.
  - Distance estimation quality.

---

## Future Developments

To extend the system's capabilities, several research directions are proposed:

- **Active Perception**: Adaptive camera and motion control to optimize information gain.
- **Multi-Robot Collaboration**: Distributed SLAM and coordinated exploration/tracking.
- **Sensor Networks**: Integration with fixed sensors using optimization approaches (e.g., Art Gallery Problem).
- **PTZ Camera Scenarios**: Replacing mobile robots with pan-tilt-zoom cameras for infrastructure monitoring.
- **Reinforcement Learning**: Adaptive behavior strategies for exploration and pursuit.

---


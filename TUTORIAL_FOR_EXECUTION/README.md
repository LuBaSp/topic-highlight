# TIAGO SLAM and Tracking Setup

## Setup Instructions

Before running the project, you need to build and set up the ROS2 workspaces. Follow the steps below:

### 1. **Build and Setup ROS2 Workspace**

First, navigate to your **ros2_ws** folder and build the workspace.

```bash
cd ~/exam_ws/ros2_ws
colcon build
source install/setup.bash
```

This will compile your ROS2 packages and source the setup script.

### 2. **Build and Setup TIAGO Workspace**

Next, navigate to the **tiago_ws** folder and repeat the build and setup steps.

```bash
cd ~/exam_ws/tiago_ws
colcon build
source install/setup.bash
```

This will set up the TIAGO robot workspace.

### 3. **Launch the Mission**

Finally, you can launch the mission bring-up.

```bash
ros2 launch mission_bringup mission_bringup.launch.py
```

This command will start the system for both environment exploration and target tracking.

---

### 4. **Start the Mission**

Open a second terminal, then run the following message.

```bash
ros2 topic pub /start_mission std_msgs/msg/Empty "{}" --once
```

### Notes:
- Make sure you have ROS2 installed and properly configured before proceeding with the steps.
- The `colcon build` commands might take some time depending on the size of your packages.
- If you encounter any issues, please refer to the **GUIDE** folder for troubleshooting and setup details.

#!/usr/bin/env bash
USER_HOME=$(eval echo ~${SUDO_USER})
source $USER_HOME/Harrold/catkin_ws/devel/setup.bash

export ROS_IP=169.254.7.78
export ROS_HOSTNAME=169.254.7.78

export ROS_MASTER_URI=http://mast:11311
exec "$@"
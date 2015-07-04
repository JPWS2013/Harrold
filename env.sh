#!/usr/bin/env bash
USER_HOME=$(eval echo ~${SUDO_USER})
source $USER_HOME/Harrold/catkin_ws/devel/setup.bash
sudo exec "$@"
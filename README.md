# Walk
Repository for NAO V6 walking code

## Walk Forward

A node for webots. 

# How to install
cd ~/dev_ws

it clone https://github.com/Starkit-SPL/Walk/tree/main src/walk_forward
git checkout Walk_back

colcon build --packages-select walk_forward

. install/setup.bash

# How to run (another terminal)

1. start webots, run world nao_robocup.wbt
2. ros2 run nao_lola nao_lola

##Again another terminal
. install/setup.bash

ros2 run walk_forward walk_forward

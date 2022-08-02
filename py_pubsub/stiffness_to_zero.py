# Copyright 2016 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import rclpy
from rclpy.logging import LoggingSeverity
from rclpy.node import Node
import time

from std_msgs.msg import String
from nao_sensor_msgs.msg import Touch
from std_msgs.msg import ColorRGBA
from nao_command_msgs.msg import ChestLed
from nao_command_msgs.msg import JointStiffnesses




class MyNode(Node):
    def __init__(self):
        super().__init__('my_node')
        self.count = 0
        self.subscription = self.create_subscription(
            Touch,
            'sensors/touch',
            self.listener_callback,
            10)
        self.publisher_chest_led = self.create_publisher(ChestLed, 'effectors/chest_led', 10)
        self.publisher_jointstiffnesses = self.create_publisher(JointStiffnesses, 'effectors/joint_stiffnesses', 10)

    def listener_callback(self, msg):
        if msg.head_middle:
            chestled_color = ChestLed()
            chestled_color.color.r = 1.0 if self.count % 3 == 0 else 0.0
            chestled_color.color.g = 1.0 if self.count % 3 == 1 else 0.0
            chestled_color.color.b = 1.0 if self.count % 3 == 2 else 0.0
            self.publisher_chest_led.publish(chestled_color)
            joint_msg = JointStiffnesses()
            joint_msg.indexes = range(25)
            joint_msg.stiffnesses = [0.0] * 25
            print(joint_msg)
            self.publisher_jointstiffnesses.publish(joint_msg)
            time.sleep(0.3)
            self.count += 1



def main(args=None):
    rclpy.init(args=args)
    node = MyNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

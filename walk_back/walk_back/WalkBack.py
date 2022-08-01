from time import sleep
import numpy as np

from multiprocessing.dummy import JoinableQueue
from posixpath import supports_unicode_filenames
from std_msgs.msg import String
from nao_sensor_msgs.msg import Touch
from std_msgs.msg import ColorRGBA
from nao_command_msgs.msg import ChestLed
from nao_command_msgs.msg import JointStiffnesses
from nao_command_msgs.msg import JointPositions as JPOUT
from nao_sensor_msgs.msg import JointPositions as JPIN
from nao_command_msgs.msg import JointStiffnesses

import rclpy
from rclpy.logging import LoggingSeverity
from rclpy.node import Node

from walk_back.poses import PoseInfo, ReadStatus


class WalkBack(Node):
    def __init__ (self):
        super().__init__('WalkBack')
        self.PublisherPose = self.create_publisher(JPOUT, 'effectors/joint_positions', 10)
        self.PublisherStiffness = self.create_publisher(JointStiffnesses, 'effectors/joint_stiffnesses', 10)
        # self.SubscriptionPose = self.create_subscription(JPIN, '/sensors/joint_positions', self.receive_pose, 10)
        self.wait_time = 0.01

        nao_pose = PoseInfo()
        dir_name = '/home/siburai/Robosoccer/nao_walk/Walk/walk_back/fast_walk/'
        nao_pose.fill_pose_info (dir_name, 'txt')
        self.pose = nao_pose

        self.stiffness_to_one()
        self.move_from_start_pose(dir_name)

        while(1):
            for i in range(self.pose.frame_quantity):
            # Need to make here the choice of walk (for example fast or slow)
            # After the choice need to go to the chosen directory and get pose
                self.frame_div(i)

    def fill_start_pose_info(self, frame, dir_name):
        frame_filename = "start_pose.txt"
        frame_path = "%s%s" % (dir_name, frame_filename)

        nao_pose = PoseInfo()
        frame_info = nao_pose.read_frame(frame_path, 0, ReadStatus.start_frame)
        for i in range(25):
            frame[i] = int(frame_info[i])

    def move_from_start_pose(self, dir_name):
        frame = [0] * 25
        self.fill_start_pose_info(frame, dir_name)

        for cycle in range(self.pose.frame_duration[0]):
            data = self.calc_frame(frame, self.pose.frame[0], self.pose.frame_duration[0], cycle)
            sleep(self.wait_time)
            print(data)
            self.publish_pose(data)
        # Нужно взять начальную позицию и перейти из нее в фрейм 0. Подправить функцию чтения позы.

    def publish_pose (self, data):
        joint_positions = JPOUT()
        joint_positions.indexes = range(25)
        joint_positions.positions = list(map(np.deg2rad, data))
        self.PublisherPose.publish(joint_positions)

    def calc_frame(self, cur_frame, next_frame, frame_dur, cycle):
        data = [0.0] * 25
        for i in range(25):
            diff = next_frame[i] - cur_frame[i]
            data[i] = diff / frame_dur * cycle + cur_frame[i]
        return data

    def frame_div (self, frame_num):
        data = [0.0] * 25
        for cycle in range(self.pose.frame_duration[frame_num]):
            data = self.calc_frame(self.pose.frame[frame_num],
                                   self.pose.frame[(frame_num + 1) % self.pose.frame_quantity], 
                                   self.pose.frame_duration[frame_num], cycle)
            sleep(self.wait_time)
            self.publish_pose(data)

    def stiffness_to_one(self):
        joint_stiffnesses = JointStiffnesses()
        joint_stiffnesses.indexes = range(25)
        joint_stiffnesses.stiffnesses = [1.0] * 25
        self.PublisherStiffness.publish(joint_stiffnesses)
        

def main(args=None):
    rclpy.init(args = args)
    Node = WalkBack()

    try:
        rclpy.spin(Node)
    except KeyboardInterrupt:
        pass

    Node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

# Poses will be readed from the walk_back_pose.xml or walk_back_pose.txt file through special function
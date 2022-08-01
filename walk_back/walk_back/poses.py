import enum

class ReadStatus(enum.Enum):
    start_frame = 1
    pose_frame = 2

class PoseInfo:
    def __init__(self):
        self.frame_quantity = -1

    def create_array (self):
        self.frame = [0] * self.frame_quantity #check if frame_quantity equals -1
        for i in range(self.frame_quantity):
            self.frame[i] = [i] * 25
        
        self.frame_duration = [0] * self.frame_quantity

    def read_frame(self, frame_filename, frame_num, read_mode):
        with open(frame_filename, 'r') as frame_file:
            data = [row.strip() for row in frame_file]
                
            if read_mode == ReadStatus.start_frame:
                return data
            elif read_mode == ReadStatus.pose_frame:
                for i in range (25):
                    self.frame[frame_num][i] = int(data[i])
                self.frame_duration[frame_num] = int(data[25])

    def fill_pose_info (self, dir_name, extension):
        quantity_filename = "%sframe_quantity.%s" % (dir_name, extension)
        
        data = [0] * 1
        
        with open(quantity_filename, 'r') as pose_quant_file:
            data = [row.strip() for row in pose_quant_file]
            self.frame_quantity = int(data[0])        
            
        self.create_array()

        for i in range(self.frame_quantity):
            frame_filename = "%sframe_%d.%s" % (dir_name, i, extension)
            self.read_frame(frame_filename, i, ReadStatus.pose_frame)
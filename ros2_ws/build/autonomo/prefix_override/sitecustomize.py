import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/frock/code/AyDpVA/ros2_ws/install/autonomo'

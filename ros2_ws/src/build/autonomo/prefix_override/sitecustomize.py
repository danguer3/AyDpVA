import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/emmanuel13/code/AyDpVA/ros2_ws/src/install/autonomo'

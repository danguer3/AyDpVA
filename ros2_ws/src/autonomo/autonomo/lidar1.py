import rclpy
from rclpy.node import node
from sensor_msgs.msg import laserScan
THRESHOLD_DISTANCE = 0.4 
def lidar_callback(msg):
    num_ranges= len(msg.ranges)
    right_index = num_ranges // 4 
    back_index = num_ranges // 2
    left_index = (3* num_ranges)//4
    front_index = 0 
    Distancias
    front_distance = msg.ranges[front_index]
    left_deistance = msg.ranges[left_index]
    back_distance = msg.ranges[back_index]
    right_distance = msg.ranges[right_index]
    chequamos 
    if front_distance< THRESHOLD_DISTANCE:
        print('obstaculo adelante')
        if left_distance < THRESHOLD_DISTANCE:
            print('obstaculo a la izquierda')
            if left_distance < THRESHOLD_DISTANCE:
                if back_distance < THRESHOLD_DISTANCE:
                    print('obstaculo atras')
                    if right_distance < THRESHOLD_DISTANCE:
                        print('obstaculo a la derecha')
                        print(len(msg.ranges))
                        def main(args = None):
                            rclpy.init(args=args)
                            node = rclpy.create_node('simple_lidar_subscriber')
                            node.create_subcription(LaserScan, lidar_callback, 10)
                            rclpy.spin(node)
                            node.destroy_node()
                            rclpy.shutdown()
                            if __name__ == '__main__':



import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64
import random

class TemperaturePublisher(Node):

    def __init__(self):
        super().__init__('temperature_publisher')

        self.publisher_ = self.create_publisher(Float64, '/temperature', 10)

        timer_period = 1.0
        self.timer = self.create_timer(timer_period, self.publish_temperature)

    def publish_temperature(self):

        msg = Float64()

        temperature = 20 + random.uniform(-1,1)

        msg.data = temperature

        self.publisher_.publish(msg)

        self.get_logger().info(f"Temperature: {temperature:.2f} °C")


def main(args=None):
    rclpy.init(args=args)

    node = TemperaturePublisher()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

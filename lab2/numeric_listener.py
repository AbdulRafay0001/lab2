import rclpy
from rclpy.node import Node
from std_msgs.msg import String, Int8  # Import Int8 along with String

class NumericListener(Node):
    def __init__(self):
        super().__init__('numeric_listener')
        # Subscriber for the original chatter topic (String messages)
        self.subscription = self.create_subscription(
            String,
            'chatter',
            self.listener_callback,
            10
        )
        self.subscription  # Prevent unused variable warning

        # Subscriber for the numeric_chatter topic (Int8 messages)
        self.numeric_subscription = self.create_subscription(
            Int8,
            'numeric_chatter',
            self.numeric_callback,
            10
        )
        self.numeric_subscription  # Prevent unused variable warning

    def listener_callback(self, msg):
        self.get_logger().info(f'I heard (String): {msg.data!r}')

    def numeric_callback(self, msg):
        self.get_logger().info(f'I heard (Numeric): {msg.data}')

def main(args=None):
    rclpy.init(args=args)
    numeric_listener = NumericListener()
    rclpy.spin(numeric_listener)
    # Optional cleanup if desired:
    # numeric_listener.destroy_node()
    # rclpy.shutdown()

if __name__ == '__main__':
    main()

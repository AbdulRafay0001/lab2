import rclpy
from rclpy.node import Node
#Modified the import line to include Int 8 message type
from std_msgs.msg import String, Int8



#Inside here we already have a publisher for the /chatter topic, now let's add another publisher for the numeric topic 
class NumericTalker(Node):
    def __init__(self):
        super().__init__('numeric_talker')
        self.publisher = self.create_publisher(String, 'chatter', 10)
        #Add another publisher here for numeric
        self.numeric_publisher = self.create_publisher(Int8, 'numeric_chatter', 10)

        timer_in_seconds = 0.5
        self.timer = self.create_timer(timer_in_seconds, self.talker_callback)
        self.counter = 0

    def talker_callback(self):
        #Publish the original "Hello world" string message
        msg = String()
        msg.data = f'Hello World, {self.counter}'
        self.publisher.publish(msg)
        self.get_logger().info(f'Publishing: {msg.data}')
        self.counter += 1

        # Publish the numeric counter value
        numeric_msg = Int8()
        numeric_msg.data = self.counter
        self.numeric_publisher.publish(numeric_msg)
        self.get_logger().info(f'Publishing numeric: {numeric_msg.data}')

        # Increment and reset counter, once it gets to 127
        self.counter += 1
        if self.counter > 127:
            self.counter = 0

def main(args=None):
    #
    rclpy.init(args=args)

    talker = NumericTalker()
    rclpy.spin(talker)


if __name__ == '__main__':
    main()





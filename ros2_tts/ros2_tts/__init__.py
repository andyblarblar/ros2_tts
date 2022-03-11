import imp
import rclpy
from .tts_service import TtsService

def main(args=None):
    rclpy.init(args=args)

    tts_service = TtsService()

    rclpy.spin(tts_service)

    tts_service.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
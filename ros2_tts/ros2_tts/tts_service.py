import rclpy
from rclpy.node import Node
from tts_interfaces.srv import TtsSpeak
from tts_interfaces.msg import Tts
import pyttsx3
import pyttsx3.voice

class TtsService(Node):

    def __init__(self):
        super().__init__('tts_service')
        self.create_service(TtsSpeak, 'tts_speak', self.tts_callback)

        self.engine = pyttsx3.init()
        self.engine.setProperty('voice', 'en-scottish')
    
    def tts_callback(self, req: TtsSpeak.Request, res: TtsSpeak.Response):
        self.engine.say(req.msg.words)
        self.engine.runAndWait()
        return res

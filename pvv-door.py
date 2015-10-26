import time
import RPi.GPIO as GPIO
import http.server as http
import json

GPIO_PIN = 7
TIMEOUT = 5

class DoorHandler(http.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("charset", "utf-8")
        self.end_headers()
        self.wfile.write(json.dumps({'door': bool(not GPIO.input(GPIO_PIN))}).encode("utf-8"))

def run():
    httpd = http.HTTPServer(('', 8000), DoorHandler)
    httpd.serve_forever()

def initialise():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(GPIO_PIN, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

if __name__ == '__main__':
    initialise()
    run()
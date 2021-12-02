import camera
from machine import Pin
import time
import os
import picoweb

def init_camera():
    camera.init(0, format=camera.JPEG)
    camera.quality(10)
    camera.framesize(camera.FRAME_UXGA)
    
def take_picture():
    picture = camera.capture()
    file_jpg = open("/static/cam10.jpeg", "wb")
    file_jpg.write(picture)
    file_jpg.close()


def web_server():
    
    #flash = Pin(4, Pin.OUT)
    #take_picture()

    app = picoweb.WebApp(__name__)

    @app.route("/")
    def index(req, resp):
        yield from picoweb.start_response(resp)
        yield from resp.awrite(b"Static image: <img src='static/cam10.jpg'><br />")

    @app.route("/take_photo")
    def squares(req, resp):
        yield from picoweb.start_response(resp)
        #flash.value(1)
        take_picture()
        #flash.value(0)
        yield from resp.awrite('OK')


    import ulogging as logging
    logging.basicConfig(level=logging.INFO)

    app.run(debug=True, host = '192.168.1.10', port='8888')
    
#print('main loaded')
try:
    init_camera()
except:
    print('Ya se ha inicializado la camara')
web_server()
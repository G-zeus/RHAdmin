from qrcode import QRCode
from decouple import config
import os

class QR:

    def __init__(self):
        self.url = config('APP_DOMAIN')
        self.storage = 'var/storage/'

    def make_qr(self, uri: str = ''):
        print('utils: '+uri)
        qr = QRCode()
        qr.add_data(self.url + uri)
        img = qr.make_image()
        path = 'var/storage/'+uri.replace('/', '_')+'.png'
        if os.path.exists(path):
            os.remove(path)
        img.save(path)


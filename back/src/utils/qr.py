from qrcode import QRCode
from decouple import config


class QR:

    def __init__(self):
        self.qr = QRCode()
        self.url = config('API_DOMAIN')
        self.storage = 'var/storage/'

    def make_qr(self, uri: str):
        self.qr.add_data(self.url + uri)
        img = self.qr.make_image()
        name = uri.replace('/', '_')

        img.save('var/storage/'+name+'.png')


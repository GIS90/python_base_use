# -*- coding: utf-8 -*-
"""
__author__ = 'Administrator'
__time__ = '2016/4/15'
"""

import qrcode


import qrcode
import qrcode.image.svg


qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=1,
)
qr.add_data('https://www.baidu.com/')
qr.make(fit=True)

img = qr.make_image()
img.save('tb.jpg')

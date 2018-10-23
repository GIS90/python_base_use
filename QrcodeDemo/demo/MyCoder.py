# -*- coding: utf-8 -*-

"""
------------------------------------------------
@version: ??
@author: PyGoHU
@contact: gaoming971366@163.com
@software: PyCharm Community Edition
@file: MyCoder.py
@time: 2016/9/14 15:09
@describe: 
@remark: 
------------------------------------------------
"""


import os
import qrcode
from PIL import Image


# 生成二维码图片
def make_qr(str, save):
    qr = qrcode.QRCode(
            version=4,  # 生成二维码尺寸的大小 1-40  1:21*21（21+(n-1)*4）
            error_correction=qrcode.constants.ERROR_CORRECT_M,  # L:7% M:15% Q:25% H:30%
            box_size=6,  # 每个格子的像素大小
            border=2,  # 边框的格子宽度大小
    )
    qr.add_data(str)
    qr.make(fit=True)

    img = qr.make_image()
    img.save(save)


# 生成带logo的二维码图片
def make_logo_qr(data, logo, save):
    # 参数配置
    qr = qrcode.QRCode(
            version=4,
            error_correction=qrcode.constants.ERROR_CORRECT_Q,
            box_size=6,
            border=2
    )
    # 添加转换内容
    qr.add_data(data)
    #
    qr.make(fit=True)
    # 生成二维码
    img = qr.make_image()
    #
    img = img.convert("RGBA")

    # 添加logo
    if logo and os.path.exists(logo):
        icon = Image.open(logo)
        # 获取二维码图片的大小
        img_w, img_h = img.size

        factor = 4
        size_w = int(img_w / factor)
        size_h = int(img_h / factor)

        # logo图片的大小不能超过二维码图片的1/4
        icon_w, icon_h = icon.size
        if icon_w > size_w:
            icon_w = size_w
        if icon_h > size_h:
            icon_h = size_h
        icon = icon.resize((icon_w, icon_h), Image.ANTIALIAS)
        # 详见：http://pillow.readthedocs.org/handbook/tutorial.html

        # 计算logo在二维码图中的位置
        w = int((img_w - icon_w) / 2)
        h = int((img_h - icon_h) / 2)
        icon = icon.convert("RGBA")
        img.paste(icon, (w, h), icon)
        # 详见：http://pillow.readthedocs.org/reference/Image.html#PIL.Image.Image.paste

    # 保存处理后图片
    img.save(save)


if __name__ == '__main__':
    save_path_lp = 'qrcode_lp.png'  # 生成后的保存文件
    logo_lp = 'logo.jpg'  # logo图片
    content_lp = """
武雅楠：
                                 中秋快乐，我爱你
                                            ^ _ ^
                                               zl
        """

    content_ts = """
各同事们：
                         中秋快乐，“必有红包”
                                 ^ _ ^开心就好
                                       高明亮
        """
    save_path_ts = 'qrcode_ts.png'
    logo_ts = "PAM.jpg"

    content_wx = """
各位帅哥美女们：
                         中秋快乐，“必有红包”
                                 ^ _ ^开心就好
                                       PyGoHUR
        """
    save_path_wx = 'qrcode_wx.png'
    logo_wx = "hb.png"

    make_logo_qr(content_lp, logo_lp, save_path_lp)
    make_logo_qr(content_ts, logo_ts, save_path_ts)
    make_logo_qr(content_wx, logo_wx, save_path_wx)
    print "ok"

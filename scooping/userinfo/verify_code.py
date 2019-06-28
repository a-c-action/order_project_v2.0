from PIL import Image, ImageDraw, ImageFont, ImageFilter
from io import BytesIO
import random

def verify_code(width=120, height=30, char_length=5, font_file='/scooping/static/fonts/KumoFont.ttf', font_size=28):
    code = []
    img = Image.new(mode='RGB', size=(width, height), color=(255, 255, 255))
    draw = ImageDraw.Draw(img, mode='RGB')

    def rndChar():
        """
        生成随机字符（包括大小写字母和数字）
        :return:
        """
        ranNum = str(random.randint(0, 9))
        ranLower = chr(random.randint(65, 90))
        ranUpper = chr(random.randint(97, 120))
        return random.choice([ranNum, ranLower, ranUpper])

    def rndColor():
        """
        生成随机颜色
        :return:
        """
        return (random.randint(0, 255), random.randint(10, 255), random.randint(64, 255))

    # 写文字
    font = ImageFont.truetype(font_file, font_size)
    for i in range(char_length):
        char = rndChar()
        code.append(char)
        h = ( height - font_size ) / 2
        draw.text([i * width / char_length, h], char, font=font, fill=rndColor())

    # 写干扰点
    for i in range(40):
        draw.point([random.randint(0, width), random.randint(0, height)], fill=rndColor())

    # 写干扰圆圈
    for i in range(40):
        draw.point([random.randint(0, width), random.randint(0, height)], fill=rndColor())
        x = random.randint(0, width)
        y = random.randint(0, height)
        draw.arc((x, y, x + 4, y + 4), 0, 90, fill=rndColor())

    # 画干扰线
    for i in range(5):
        x1 = random.randint(0, width)
        y1 = random.randint(0, height)
        x2 = random.randint(0, width)
        y2 = random.randint(0, height)
        draw.line((x1, y1, x2, y2), fill=rndColor())

    # 对图像加滤波 - 深度边缘增强滤波
    img = img.filter(ImageFilter.EDGE_ENHANCE_MORE)
    codes = ''.join(code)
    return img,codes
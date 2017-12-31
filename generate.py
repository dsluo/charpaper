import argparse
import random

from PIL import ImageFont, Image, ImageDraw

parser = argparse.ArgumentParser(description='Generate a desktop background using random characters and colors.')


def size(s):
    defaults = {
        '4k': (3840, 2160),
        '2k': (2048, 1080),
        '1440p': (2560, 1440),
        '1080p': (1920, 1080),
        '720p': (1280, 720)
    }
    if defaults.get(s.lower()) is not None:
        return defaults[s.lower()]
    try:
        width, height = map(int, s.split('x'))
        return width, height
    except:
        raise argparse.ArgumentTypeError('Size must be "WIDTHxHEIGHT"')


parser.add_argument('-s', '--size', type=size, default=(1920, 1080), metavar='WIDTHxHEIGHT',
                    help='WIDTHxHEIGHT or 4k/2k/1440p/1080p/720p.')
parser.add_argument('-f', '--font', type=str, metavar='PATH', help='Path to font file.')
parser.add_argument('-fs', '--font-size', type=int, default=24, help='Font size in pixels.')
parser.add_argument('-vp', '--vertical-padding', type=int, default=8, dest='v_padd', metavar='HORIZONTAL',
                    help='Vertical padding in pixels.')
parser.add_argument('-hp', '--horizontal-padding', type=int, default=4, dest='h_padd', metavar='VERTICAL',
                    help='Horizontal padding in pixels.')


def color(s):
    try:
        s = s.lstrip('#')
        r, g, b = tuple(int(s[i:i + 2], 16) for i in (0, 2, 4))
        if len(s) == 8:
            a = int(s[-2:], 16)
        else:
            a = 255
        return r, g, b, a
    except:
        raise argparse.ArgumentTypeError('Color must be in hexadecimal format.')


parser.add_argument('-bg', '--background', type=color, default=(40, 43, 53, 255), dest='bg', metavar='BACKGROUND',
                    help='Background color in hexadecimal.')
parser.add_argument('-ch', '--characters', type=str, default="""`~!@#$%^&*()_+=-[]\{}|;':",./<>?""", dest='chars',
                    help='Characters to use in generation.')

default_colors = [
    (95, 80, 74, 255),
    (81, 98, 79, 255),
    (105, 55, 63, 255),
    (38, 94, 109, 255),
    (133, 100, 78, 255),
    (92, 51, 89, 255),
    (57, 99, 69, 255)
]
parser.add_argument('-c', '--colors', type=color, nargs='+', default=default_colors,
                    help='Colors to use in generation.')

parser.add_argument('-o', '--output', type=str, default='./output.png', metavar='PATH')

args = parser.parse_args()

txt = Image.new('RGBA', args.size, args.bg)

try:
    if args.font is None:
        raise IOError
    font = ImageFont.truetype(args.font, args.font_size)
except IOError:
    font = ImageFont.load_default()

draw_ctx = ImageDraw.Draw(txt)

for x in range(-args.h_padd, txt.size[0], args.h_padd + args.font_size):
    for y in range(-args.v_padd, txt.size[1], args.v_padd + args.font_size):
        draw_ctx.text((x, y), random.choice(args.chars), random.choice(args.colors), font)

txt.save(args.output)

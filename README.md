# Charpaper

Generates desktop backgrounds using random characters and colors.

## Requirements

Uses Pillow v4.3.0 to generate images. Written in Python 3, but *might* work with Python 2 (untested).

## Usage

```
usage: generate.py [-h] [-s WIDTHxHEIGHT] [-f PATH] [-fs FONT_SIZE]
                   [-vp HORIZONTAL] [-hp VERTICAL] [-bg BACKGROUND]
                   [-ch CHARS] [-c COLORS [COLORS ...]] [-o PATH]

Generate a desktop background using random characters and colors.

optional arguments:
  -h, --help            show this help message and exit
  -s WIDTHxHEIGHT, --size WIDTHxHEIGHT
                        WIDTHxHEIGHT or 4k/2k/1440p/1080p/720p.
  -f PATH, --font PATH  Path to font file.
  -fs FONT_SIZE, --font-size FONT_SIZE
                        Font size in pixels.
  -vp HORIZONTAL, --vertical-padding HORIZONTAL
                        Vertical padding in pixels.
  -hp VERTICAL, --horizontal-padding VERTICAL
                        Horizontal padding in pixels.
  -bg BACKGROUND, --background BACKGROUND
                        Background color in hexadecimal.
  -ch CHARS, --characters CHARS
                        Characters to use in generation.
  -c COLORS [COLORS ...], --colors COLORS [COLORS ...]
                        Colors to use in generation.
  -o PATH, --output PATH
```

## Screenshot

![screenshot](screenshot.png)
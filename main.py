#!/usr/local/bin/python3.7

from PIL import Image, ImageDraw
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("-n","--number",help="the number of lines to draw on the image.", type=int, default=10)
parser.add_argument("-w","--width",help="the width of line to draw.", type=int, default=0)
parser.add_argument("image",help="the source image file to draw lines on.")
parser.add_argument("output",help="the output image file name to save the result to.")
args = parser.parse_args()

if not os.path.exists(args.image):
    exit("Input image does not exist.")

if not args.number > 0:
    exit("Number of lines must be greater than zero.")

if not args.width >= 0:
    exit("Width must not be less than zero.")

IMAGE = args.image
OUTPUT = args.output 
N = args.number
W = args.width 

im = Image.open(IMAGE)
draw = ImageDraw.Draw(im)

# Get the image sizes and find out the box width
w, h = im.size 
bw = min(w, h)/N 

# Horizontal lines
x = bw
while x < h:
    draw.line((0, x, w, x), fill=128, width=W)
    x += bw

y = bw
while y < w:
    draw.line((y, 0, y, h), fill=128, width=W)
    y += bw

im.save(OUTPUT)
    

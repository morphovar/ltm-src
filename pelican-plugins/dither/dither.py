#!/usr/bin/env python
# -*- coding: utf-8 -*- #

#adds advanced dithering effect to images
# Copyright (C) 2018  Roel Roscam Abbing

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


import os, logging
from pelican import signals
from bs4 import BeautifulSoup
logger = logging.getLogger(__name__)

try:
    from PIL import Image
    import hitherdither
    enabled = True
except:
    logging.warning("Unable to load PIL or hitherdither, disabling thumbnailer")
    enabled = False

DEFAULT_IMAGE_DIR = "images"
DEFAULT_DITHER_DIR = "dithers"
DEFAULT_THRESHOLD = [96, 96, 96] # this sets the contrast of the final image, rgb
DEFAULT_TRANSPARENCY= True
DEFAULT_TRANSPARENT_COLOR = [(125,125,125)]
DEFAULT_DITHER_PALETTE = [(25,25,25), (75,75,75),(125,125,125),(175,175,175),(225,225,225),(250,250,250)] # 6 tone palette

#11 tone palette, heavier, more detail, less visible dither pattern
#[(0,0,0),(25,25,25),(50,50,50),(75,75,75),(100,100,100),(125,125,125),(150,150,150),(175,175,175),(200,200,200),(225,225,225),(250,250,250)]

#3 tone palette, lighter, heavier dithering effect
# [(0,0,0), (125,125,125), (250,250,250)]


def _image_path(pelican):
    return os.path.join(pelican.settings['PATH'],
        pelican.settings.get("IMAGE_PATH", DEFAULT_IMAGE_DIR)).rstrip('/')

def _out_path(pelican):
    return os.path.join(pelican.settings['OUTPUT_PATH'],
                         pelican.settings.get('DITHER_DIR', DEFAULT_DITHER_DIR))

def calculate_savings(image_dir, dither_dir):
    original = 0
    dithered = 0
    for i in os.listdir(image_dir):
        original = original + os.stat(os.path.join(image_dir, i)).st_size

    for i in os.listdir(dither_dir):
        dithered = dithered + os.stat(os.path.join(dither_dir, i)).st_size

    return 'dither plugin:\ntotal size image directory  :{}KiB\ntotal size dithered directory:{}KiB'.format(original/1000, dithered/1000)

def color_to_transparent(img, color):
    #make all pixels of a certain color transparent
    # color needs to be (255,255,255) format 
    rgba = img.convert('RGBA')
    pixels = rgba.load()

    for x in range(img.size[0]):
        for y in range(img.size[1]):
            if pixels[x,y] == color + (255,):
                pixels[x,y] = color + (0,)
    return rgba


def dither(pelican):
    global enabled
    if not enabled:
        return

    in_path = _image_path(pelican)
    out_path = _out_path(pelican)

    transparency = pelican.settings.get("TRANSPARENCY",DEFAULT_TRANSPARENCY)

    if not os.path.exists(out_path):
        os.mkdir(out_path)

    for dirpath, _, filenames in os.walk(in_path):
        for filename in filenames:
            file_, ext = os.path.splitext(filename)
            fn= os.path.join(dirpath,filename)
            of = os.path.join(out_path, filename.replace(ext,'.png'))
            if not os.path.exists(of):
                logging.debug("dither plugin: dithering {}".format(fn))

                img= Image.open(fn).convert('RGB')
                
                palette = hitherdither.palette.Palette(pelican.settings.get('DITHER_PALETTE', DEFAULT_DITHER_PALETTE))
                
                threshold = pelican.settings.get('THRESHOLD', DEFAULT_THRESHOLD)
                
                img_dithered = hitherdither.ordered.bayer.bayer_dithering(img, palette, threshold, order=8) #see hither dither documentation for different dithering algos

                if transparency:
                    #pick a color to become transparent, make sure you pick a tint in the middle of the palette for optimum effect
                    # you can also rerun the function to make more colros transparent
                    transparent_color= pelican.settings.get('TRANSPARENT_COLOR',DEFAULT_TRANSPARENT_COLOR)
                    for colorset in transparent_color:
                        logging.debug("dither plugin: Replaced color {},{},{} by transparency on {}".format(colorset[0],colorset[1],colorset[2], fn))
                        transparent_image = color_to_transparent(img_dithered, colorset)
                        img_dithered = transparent_image
         
                img_dithered.save(of)
    logging.debug(calculate_savings(in_path,out_path))

def parse_for_images(instance):
    #based on better_figures_and_images plugin by @dflock, @phrawzty,@if1live,@jar1karp,@dhalperi,@aqw,@adworacz
    #https://github.com/getpelican/pelican-plugins/blob/master/better_figures_and_images/better_figures_and_images.py
    global DEFAULT_IMAGE_DIR
    global DEFAULT_DITHER_DIR
    global enabled

    if not enabled:
        return

    image_dir = instance.settings.get("IMAGE_PATH", DEFAULT_IMAGE_DIR)
    dither_dir = instance.settings.get('DITHER_DIR', DEFAULT_DITHER_DIR)


    if instance._content is not None:
        content = instance._content
        soup = BeautifulSoup(content, 'html.parser')
        for img in soup(['img', 'object']):
            fn, ext = os.path.splitext(img['src'])
            if ext.startswith('.'):
                img['src'] = img['src'].replace(ext, '.png') 
            img['src'] = img['src'].replace(image_dir,dither_dir)
                # logger.debug('dither plugin: rewrote image source to {}'.format(img['src']))
        instance._content = soup.decode()



def register():
    signals.finalized.connect(dither)
    signals.content_object_init.connect(parse_for_images)

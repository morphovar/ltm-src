# Dither plugin for Pelican

## dependencies
depends on [Pillow](https://pillow.readthedocs.io), [hitherdither](https://github.com/hbldh/hitherdither) and [BeautifulSoup 4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

`pip install Pillow bs4 git+https://www.github.com/hbldh/hitherdither`

## use
TODO
## configuration
TODO

DEFAULT_IMAGE_DIR = "images"
DEFAULT_DITHER_DIR = "dithers"
DEFAULT_THRESHOLD = [96, 96, 96] # this sets the contrast of the final image, rgb
DEFAULT_TRANSPARENCY= True
DEFAULT_TRANSPARENT_COLOR = (125,125,125)
DEFAULT_DITHER_PALETTE = [(25,25,25), (75,75,75),(125,125,125),(175,175,175),(225,225,225), (250,250,250)] # 6 tone palette

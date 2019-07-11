#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 23:21:05 2019

@author: robertweigel
"""

from PIL import Image
from PIL import ImageChops

from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

fig = Figure()
FigureCanvas(fig) # Not used directly, but calling attaches canvas to fig which is used later.
textbox = fig.text(0.5,0.5,'0000000000\n0', color='white', bbox=dict(boxstyle='square,pad=0', fc='black', ec='none'))
f1 = '/Users/robertweigel/Desktop/a.jpg'
fig.canvas.print_figure(f1, dpi=100, bbox_inches='tight')


fig = Figure()
FigureCanvas(fig) # Not used directly, but calling attaches canvas to fig which is used later.
textbox = fig.text(0.5,0.51,'333\n0', color='white', bbox=dict(boxstyle='square,pad=0', fc='black', ec='none'))
f2 = '/Users/robertweigel/Desktop/b.jpg'
fig.canvas.print_figure(f2, dpi=100, bbox_inches='tight')

i1 = Image.open(f1)
i2 = Image.open(f2)

d = ImageChops.difference(i1, i2)
d.show()

if False:
    from matplotlib.figure import Figure
    from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
    fig = Figure()
    FigureCanvas(fig) # Not used directly, but calling attaches canvas to fig which is used later.
    textbox = fig.text(0.5,0.5,'0000000000\n0', color='white', bbox=dict(boxstyle='square,pad=0', fc='black', ec='none'))
    fig.canvas.print_figure('/Users/robertweigel/Desktop/a.jpg', dpi=100, bbox_inches='tight')
    
    from PIL import Image
    import numpy as np
    
    im = Image.open("/Users/robertweigel/Desktop/a.jpg")
    pix = np.asarray(im)
    
    pix = pix[:,:,0:3] # Drop the alpha channel
    idx = np.where(pix-255)[0:2] # Drop the color when finding edges
    box = list(map(min,idx))[::-1] + list(map(max,idx))[::-1]
    
    region = im.crop(box)
    region_pix = np.asarray(region)
    print(region_pix.shape)
    from pylab import *
    imshow(region_pix)
    
    def numsize():
        '''Returns (width, height) of number '0' in pixels'''
        # Not used.
        # Based on https://stackoverflow.com/q/5320205
        # TODO: numsize(fig, dir) should inspect fig to get used fonts
        # for dir='x' and dir='y' and get bounding box for x and y labels.
        from matplotlib import pyplot as plt
        r = plt.figure().canvas.get_renderer()
        t = plt.text(0.5, 0.5, '0')    
        bb = t.get_window_extent(renderer=r)
        w = bb.width
        h = bb.height
        plt.close()
        return (w,h)
    
    #print(numsize())
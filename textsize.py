#def textsize_test():

if False:
    from matplotlib.figure import Figure
    from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
    fig = Figure()
    canvas = FigureCanvas(fig)
    ax = fig.add_subplot(111)
    ax.plot([1,2], [1,2])
    ax.set(ylabel='y', xlabel='x', title='Title\nsubtitle')
    #fig.show()

#def textsize():
'''Returns (width, height) of number '0' in pixels'''
# Not used.
# Based on https://stackoverflow.com/q/5320205
# TODO: numsize(fig, dir) should inspect fig to get used fonts
# for dir='x' and dir='y' and get bounding box for x and y labels.

from matplotlib import pyplot as plt

fig = plt.figure()
r = fig.canvas.get_renderer()
t = plt.title('0\n0')    
ax = fig.gca()

ax.set_ylabel('a')
ax.set_xlabel('b\n\n\nb')
ax.get_xlabel().get_position().get_points()

bb = t.get_window_extent(renderer=r)

dpi = fig.dpi
fw = fig.get_figwidth()
fh = fig.get_figheight()

ax.get_yticklabels()[0].get_window_extent(r).get_points()


yt.set(text='aaa') # Does not work.
ylabels = [item.get_text() for item in ax.get_yticklabels()]
ylabels[0] = 'aaa'
ax.set_yticklabels(ylabels)
 
# Need to iterate over all labels to set properties for each.
yt = ax.get_yticklabels()[0]
yt.set(color='yellow')


ytick.labels = {
alpha
color
backgroundcolor
fontfamily
fontsize
fontstrech
fontvariant
fontweight
rotation
rotation_mode
horizontalalignment
verticalalignment
linespacing

wrap

snap
sketch_params
transform
rasterized
multialignment
picker
}



axbb = ax.get_position().get_points()

ac = ax.get_children()
b = ax.get_children()[0].get_window_extent(r).get_points()

ax.get_yticklabels()[0].get_window_extent(r).get_points()

ax.get_children()

ax.get_ylabel()
w = bb.width
h = bb.height
plt.show()
#plt.close()
print("Figure dpi: %d" % dpi)
print("Figure wxh: %dx%d inches" % (fw,fh))
print("Figure wxh: %dx%d pixels" % (fw*dpi,fh*dpi))
print("Text   wxh: %dx%d px" % (w,h))
#return (w,h)

#textsize()        

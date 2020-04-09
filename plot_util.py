from pylab import *

def plot_bands(image,figKwargs={},imshowKwargs={}):
    f = figure(**figKwargs)
    for band in range(image.shape[2]):
        subplot(1,image.shape[2],band+1)
        imshow(image[:,:,band],**imshowKwargs)
    return f

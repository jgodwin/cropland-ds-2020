import common
import tqdm
import numpy as np

def loadZValues():
    '''Load the numpy data, and convert each band of each image to it's corresponding
    Z-values.
    returns a list of (key, normalized image)
    '''
    images = []
    for key in tqdm.tqdm(common.NUMPY_KEYS):
        im = common.loadNumpy(key)
        for k in range(im.shape[2]):
            u = np.nanmean(im[:,:,k])
            sig = np.nanstd(im[:,:,k])
            im[:,:,k] = (im[:,:,k]-u)/sig # convert to Z-value
        images.append((key,im))
    return images
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

# the features that we selected from Feature Selection notebook.
KEEP_FEATURES = np.array(['20170306_0', '20170306_4', '20170410_0', '20170410_2',
       '20170410_3', '20170410_4', '20170601_0', '20170601_3',
       '20170601_4', '20170615_4', '20170708_3', '20170708_4',
       '20170807_2', '20170807_3', '20170807_4', '20170905_4',
       '20170923_0', '20170923_4', '20171015_4', '20171207_4'],
      dtype='<U10')

def getKeyFeatures():
    '''
    Get the key features (images; z-values), as determined through feature selection, as a dictionary of file_bandno : band image . 
    '''
    zImages = loadZValues()
    keepKeys = [(name.split('_')[0],int(name.split('_')[1])) for name in KEEP_FEATURES]
    
    zImageMap = {}
    for key, im in zImages:
        for j in range(im.shape[2]):
            zImageMap[(key,j)] = im[:,:,j]
    
    keepMap = { '_'.join([key[0],'{:02d}'.format(key[1])]): zImageMap[key] for key in keepKeys}
    return keepMap

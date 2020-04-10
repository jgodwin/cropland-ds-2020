'''
Utility methods to load and save data to S3
'''

import boto3
import numpy
from io import BytesIO

BUCKET='cropland-ds'

IMAGE_FOLDER = 'cropland/data'
NUMPY_FOLDER = 'cropland/numpy'

# use this command to generate this list:
# ! aws s3 ls cropland-ds/cropland/data/ | awk '{ print $4 }'
IMAGE_KEYS = '''20170306.tiff
20170410.tiff
20170601.tiff
20170615.tiff
20170708.tiff
20170807.tiff
20170905.tiff
20170923.tiff
20171015.tiff
20171207.tiff'''.split('\n')

NUMPY_KEYS = [key.split('.')[0] for key in IMAGE_KEYS]

LABEL_KEY = 'cdl2017.tiff'

LABEL_NUMPY_KEY = 'labels'

def saveBytes(byteData,key):
    s3 = boto3.client('s3')
    response = s3.put_object(Key=key,Body=byteData,Bucket=BUCKET)
    # should check response code here
    return response

def loadBytes(key):
    s3 = boto3.client('s3')
    response = s3.get_object(Key=key,Bucket=BUCKET)
    # should check response code here
    return response['Body'].read()

def saveArray(array,key):
    bio = BytesIO()
    numpy.save(bio,array)
    bio.flush()
    bio.seek(0)
    saveBytes(bio.getvalue(), key)
    
def loadArray(key):
    bytez = loadBytes(key)
    bio = BytesIO(bytez)
    return numpy.load(bio)

def readTIFF(key):
    return loadBytes('/'.join([IMAGE_FOLDER,key]))
                            
def saveNumpy(im, key):
    return saveArray(im,'/'.join([NUMPY_FOLDER,key]))

def loadNumpy(key):
    return loadArray('/'.join([NUMPY_FOLDER,key]))

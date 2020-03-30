import urllib
import requests, io, os
import numpy as np
import tarfile, zipfile, gzip
def unzip_from_UCI(UCI_url, dest=''):
# Downloads and unpacks datasets from UCI in zip format
    response = requests.get(UCI_url)
    compressed_file = io.BytesIO(response.content)
    z = zipfile.ZipFile(compressed_file)
    print ('Extracting in %s' % os.getcwd()+os.sep+dest)

    for name in z.namelist():
            if '.csv' in name:
                print ('\tunzipping %s' %name)
                z.extract(name, path=os.getcwd()+os.sep+dest)
                
def gzip_from_UCI(UCI_url, dest=''):
# Downloads and unpacks datasets from UCI in gzip format
    response = urllib.request.urlopen(UCI_url)
    compressed_file = io.BytesIO(response.read())
    decompressed_file = gzip.GzipFile(fileobj = compressed_file)
    filename = UCI_url.split('/')[-1][:-3]
    
    with open(os.getcwd()+os.sep+filename, 'wb') as outfile:
        outfile.write(decompressed_file.read())
        print ('File %s decompressed' % filename)     
           

UCI_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/00275/Bike-Sharing-Dataset.zip'
unzip_from_UCI(UCI_url, dest='bikesharing')
UCI_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/covtype/covtype.data.gz'
gzip_from_UCI(UCI_url)
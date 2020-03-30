import pandas as pd 
import numpy as np 
import os

def disk_shuffle(filename_in , filename_out , header=True, \ CHUNK_SIZE=10000, SEP= ' , ' ): 
    with open(filename_out , 'a' ) as W: 
        with open(filename_in , 'r' ) as R: 
            iterator = pd.read_csv(R, chunksize=CHUNK_SIZE)
            for n, df in enumerate( iterator ): 
                if n==0 and header: 
                    df. iloc [np.random.permutation(len(df ))]. to_csv(W, \ index = False , header = True, sep = SEP) 
                    else : 
                        df. iloc [np.random.permutation(len(df ))]. to_csv(W, \ index = False , header = False , sep = SEP)
